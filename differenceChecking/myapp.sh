#!/bin/bash

# Define the folders
production_folder="production"
disaster_recovery_folder="disaster_recovery"

# Define the output file
output_file="environment_variable_diff.txt"

# Function to extract environment variables from YAML file
extract_env_variables() {
    local yaml_file="$1"
    # Extract lines starting with '- env:' or '- envFrom:'
    grep -E '^\s+-\s+(env|envFrom):' "$yaml_file" -A 1000 | grep -E '^\s+-\s+[A-Za-z0-9_]+\s*:' | \
    sed -E 's/^\s+-\s+([A-Za-z0-9_]+)\s*:(.*)$/\1=\2/'

# ^: Anchors the match to the beginning of a line.
# \s+: Matches one or more whitespace characters.
# -: Matches a hyphen character.
# (env|envFrom): Matches either "env" or "envFrom".
# :: Matches a colon.
# -A 1000: Prints 1000 lines after each matching line.
# ([A-Za-z0-9_]+): Captures one or more uppercase letters, lowercase letters, digits, or underscores.
# \s*: Matches zero or more whitespace characters.
# :: Matches a colon.
# (.*)$: Captures everything after the colon until the end of the line.
# \1=\2: Replaces the entire matched line with the content of the first captured group (\1), an equals sign, and the content of the second captured group (\2).

}

# Function to compare environment variables between two YAML files
compare_yaml_files() {
    local production_yaml="$1"
    local disaster_recovery_yaml="$2"

    # Extract environment variables from YAML files
    extract_env_variables "$production_yaml" > "$output_file.production"
    extract_env_variables "$disaster_recovery_yaml" > "$output_file.disaster_recovery"

    # Compare the environment variables and save the difference to the output file
    diff "$output_file.production" "$output_file.disaster_recovery" > "$output_file.tmp"

    # Check if there are differences
    if [ -s "$output_file.tmp" ]; then
        echo "Differences found between $production_yaml and $disaster_recovery_yaml:" >> "$output_file"
        echo "Variables present only in $production_folder:" >> "$output_file"
        comm -23 "$output_file.production" "$output_file.disaster_recovery" >> "$output_file"
        echo "" >> "$output_file"
        echo "Variables present only in $disaster_recovery_folder:" >> "$output_file"
        comm -13 "$output_file.production" "$output_file.disaster_recovery" >> "$output_file"
        echo "" >> "$output_file"
    fi

    # Clean up temporary files
    rm -f "$output_file.production" "$output_file.disaster_recovery" "$output_file.tmp"
}

# Main script

# Check if the folders exist
if [ ! -d "$production_folder" ] || [ ! -d "$disaster_recovery_folder" ]; then
    echo "Error: Production or Disaster Recovery folder does not exist."
    exit 1
fi

# Loop through all subdirectories in the production folder
for subdirectory in "$production_folder"/*; do
    # Check if it is a directory
    if [ -d "$subdirectory" ]; then
        # Extract the subdirectory name
        subdirectory_name=$(basename "$subdirectory")
        
        # Check if the disaster recovery subdirectory exists
        disaster_recovery_subdirectory="$disaster_recovery_folder/$subdirectory_name"
        if [ -d "$disaster_recovery_subdirectory" ]; then
            # Loop through all YAML files in the subdirectory
            for production_yaml_file in "$subdirectory"/*.yaml; do
                # Extract the corresponding file name
                file_name=$(basename "$production_yaml_file")
                
                # Check if the disaster recovery file exists
                disaster_recovery_yaml_file="$disaster_recovery_subdirectory/$file_name"
                if [ -f "$disaster_recovery_yaml_file" ]; then
                    echo "Comparing $production_yaml_file and $disaster_recovery_yaml_file..."
                    compare_yaml_files "$production_yaml_file" "$disaster_recovery_yaml_file"
                else
                    echo "Warning: File $disaster_recovery_yaml_file not found."
                fi
            done
        else
            echo "Warning: Subdirectory $disaster_recovery_subdirectory not found."
        fi
    fi
done

echo "Comparison completed. Differences saved to $output_file."
