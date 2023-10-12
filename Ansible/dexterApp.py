import os
import subprocess

# List of folders
folders = [
    "aaa",
    "aaa-teller",
    "crm",
    "frontend",
    "fsm-obs",
    "reporting-crm",
    "teller",
    "aaa-crm",
    "esm",
    "fsm-crm",
    "fsm-teller",
    "reporting",
    "teresol"
]

def get_user_folder_choice():
    print("Choose a folder:")
    for index, folder in enumerate(folders, start=1):
        print(f"{index}. {folder}")

    while True:
        try:
            choice = int(input("Enter the number of the folder you want to deploy: "))
            if 1 <= choice <= len(folders):
                return folders[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_user_input():
    service = input("Enter the service name: ")
    tag = input(f"Enter the tag for the {service} service: ")
    return service, tag

def update_ansible_vars(folder, service, tag):
    vars_file_path = f"/home/bahl/Documents/devops-document/DevOps-Practice/Ansible/Ansible/vars/dev_vars.yaml"
    if not os.path.exists(os.path.dirname(vars_file_path)):
        os.makedirs(os.path.dirname(vars_file_path))

    with open(vars_file_path, 'w') as vars_file:
        vars_file.write(f"dpath: \"/home/teresol/development\"\n")
        vars_file.write(f"file_name: \"/{folder}/{service}.yaml\"\n")
        vars_file.write(f"replace_string: \"{tag}\"\n")

def deploy_with_ansible():
    playbook_path = "Ansible/playbooks/deployment.yaml"
    # inventory = "development"  # You can change this based on your environment
    command = f"ansible-playbook /home/bahl/Documents/devops-document/DevOps-Practice/Ansible/playbooks/deployment.yaml -i /home/bahl/Documents/devops-document/DevOps-Practice/Ansible/inventories/inventory"
    subprocess.run(command, shell=True)

def main():
    folder = get_user_folder_choice()
    service, tag = get_user_input()
    update_ansible_vars(folder, service, tag)
    deploy_with_ansible()

if __name__ == "__main__":
    main()

















