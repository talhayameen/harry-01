pipeline:
  agent:
    any
    
  environment:
    BASE_PATH: '/home/devops/staging'

  stages:
    - stage: Update YAML Files
      steps:
        - script:
            name: 'Update YAML Files'
            script: |
              FOLDERS=$(ls $BASE_PATH)
              echo "Available folders:"
              echo $FOLDERS

              read -p "Enter the number of the folder you want to update: " CHOICE
              SELECTED_FOLDER=$(echo $FOLDERS | cut -d' ' -f$CHOICE)
              FOLDER_PATH="$BASE_PATH/$SELECTED_FOLDER"
              
              read -p "Enter the path to the diff file: " DIFF_FILE

              python3 <<EOF
import os
import yaml

folder_path = os.environ['FOLDER_PATH']
diff_file = os.environ['DIFF_FILE']
errors = []

with open(diff_file, 'r') as file:
    lines = file.readlines()

    for line in lines:
        service, tag = line.strip().split(':')
        print(f"Processing line: {service}, {tag}")

        filenames = [filename for filename in os.listdir(folder_path) if filename.startswith(service)]

        if filenames:
            latest_filename = sorted(filenames, reverse=True)[0]
            file_path = os.path.join(folder_path, latest_filename)

            with open(file_path, 'r') as yaml_file:
                content = yaml_file.read()

            # Update the image tag in the YAML content
            updated_content = content.replace(f'{service}:{tag}', f'{service}:{tag}')

            with open(file_path, 'w') as yaml_file:
                yaml_file.write(updated_content)

            print(f"Updated file: {file_path}")
        else:
            errors.append(service)

if errors:
    with open(os.path.join(folder_path, 'errors.txt'), 'w') as error_file:
        error_file.write('\n'.join(errors))

print("Processing completed.")
EOF
