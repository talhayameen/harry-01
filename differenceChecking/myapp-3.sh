#!/bin/bash

# Define the folders
production_folder="./pilot"
disaster_recovery_folder="./production-dr"

# Define the output file
output_file="environment_variable_diff.txt"

# Function to extract environment variables from YAML file
extract_env_variables() {
    local yaml_file="$1"

    # Extract lines starting with '- env:' or '- envFrom:'
    grep -E '^\s+-\s+(env|envFrom):' "$yaml_file" -A 1000 | grep -E '^\s+-\s+[A-Za-z0-9_]+\s*:' | \
    sed -E 's/^\s+-\s+([A-Za-z0-9_]+)\s*:(.*)$/\1=\2/'
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

    if [ -s "$output_file.tmp" ]; then
        echo "Differences found between $production_yaml and $disaster_recovery_yaml:" >> "$output_file"
        
        # Extract variable names present only in production environment
        production_only_variables=$(comm -23 "$output_file.production" "$output_file.disaster_recovery")
        
        if [ -n "$production_only_variables" ]; then
            echo "Variables present only in $production_folder:" >> "$output_file"
            echo "$production_only_variables" >> "$output_file"
            echo "" >> "$output_file"
        fi

        # Extract variable names present only in disaster recovery environment
        disaster_recovery_only_variables=$(comm -13 "$output_file.production" "$output_file.disaster_recovery")
        
        if [ -n "$disaster_recovery_only_variables" ]; then
            echo "Variables present only in $disaster_recovery_folder:" >> "$output_file"
            echo "$disaster_recovery_only_variables" >> "$output_file"
            echo "" >> "$output_file"
        fi
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

# Loop through all YAML files in the production folder
for production_yaml_file in "$production_folder"/*/*.yaml; do
    # Extract the corresponding base file name before the hyphen
    file_name=$(basename "$production_yaml_file" | sed 's/-.*//')

    # Check if the disaster recovery file exists
    disaster_recovery_yaml_file="$disaster_recovery_folder"/*/"$file_name"*.yaml

    if compgen -G "$disaster_recovery_yaml_file" > /dev/null; then
        # Choose only the first matching file in disaster recovery folder
        dr_file=$(ls $disaster_recovery_yaml_file | head -n 1)
        echo "Comparing $production_yaml_file and $dr_file..."
        compare_yaml_files "$production_yaml_file" "$dr_file"
    else
        echo "Warning: File for $production_yaml_file not found in $disaster_recovery_folder. You may need to add the corresponding environment file."
    fi
done

echo "Comparison completed. Differences saved to $output_file."
