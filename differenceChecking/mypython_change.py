import os
import subprocess

# Define the folders
production_folder = "production"
disaster_recovery_folder = "disaster_recovery"

# Define the output file
output_file = "environment_variable_diff.txt"

# Function to extract environment variables from YAML file
def extract_env_variables(yaml_file):
    result = subprocess.run(
        ["grep", "-E", '^\s+-\s+(env|envFrom):', yaml_file, "-A", "1000"],
        capture_output=True,
        text=True,
    )
    env_lines = result.stdout.splitlines()
    return [
        line.split(":")[0].strip() for line in env_lines if line.strip().startswith("-")
    ]

# Function to compare environment variables between two YAML files
def compare_yaml_files(production_yaml, disaster_recovery_yaml):
    production_vars = extract_env_variables(production_yaml)
    disaster_recovery_vars = extract_env_variables(disaster_recovery_yaml)

    # Variables present only in production
    production_only = list(set(production_vars) - set(disaster_recovery_vars))

    # Variables present only in disaster recovery
    disaster_recovery_only = list(set(disaster_recovery_vars) - set(production_vars))

    # Write differences to the output file
    with open(output_file, "a") as f:
        f.write(f"Differences found between {production_yaml} and {disaster_recovery_yaml}:\n")
        f.write(f"Variables present only in {production_folder}:\n")
        f.write("\n".join(sorted(production_only)) + "\n\n")
        f.write(f"Variables present only in {disaster_recovery_folder}:\n")
        f.write("\n".join(sorted(disaster_recovery_only)) + "\n\n")

# Main script

# Check if the folders exist
if not os.path.exists(production_folder) or not os.path.exists(disaster_recovery_folder):
    print("Error: Production or Disaster Recovery folder does not exist.")
    exit(1)

# Loop through all subdirectories in the production folder
for subdirectory in os.listdir(production_folder):
    subdirectory_path = os.path.join(production_folder, subdirectory)

    # Check if it is a directory
    if os.path.isdir(subdirectory_path):
        disaster_recovery_subdirectory = os.path.join(
            disaster_recovery_folder, subdirectory
        )

        # Check if the disaster recovery subdirectory exists
        if os.path.exists(disaster_recovery_subdirectory):
            # Loop through all YAML files in the subdirectory
            for production_yaml_file in os.listdir(subdirectory_path):
                production_yaml_path = os.path.join(
                    subdirectory_path, production_yaml_file
                )

                disaster_recovery_yaml_file = os.path.join(
                    disaster_recovery_subdirectory, production_yaml_file
                )

                # Check if the disaster recovery file exists
                if os.path.exists(disaster_recovery_yaml_file):
                    print(
                        f"Comparing {production_yaml_path} and {disaster_recovery_yaml_file}..."
                    )
                    compare_yaml_files(production_yaml_path, disaster_recovery_yaml_file)
                else:
                    print(f"Warning: File {disaster_recovery_yaml_file} not found.")
        else:
            print(f"Warning: Subdirectory {disaster_recovery_subdirectory} not found.")

print(f"Comparison completed. Differences saved to {output_file}.")
