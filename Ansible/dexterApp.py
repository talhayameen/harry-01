import os
import subprocess


#list of vars
dpath="/home/teresol/development"

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

def get_inventory_group():
    return input("Enter the inventory group to deploy to: ")

def update_ansible_vars(folder, service, tag, dpath):
    vars_file_path = f"Ansible/vars/dev_vars.yaml"
    if not os.path.exists(os.path.dirname(vars_file_path)):
        os.makedirs(os.path.dirname(vars_file_path))

    with open(vars_file_path, 'w') as vars_file:
        vars_file.write(f"dpath: \"{dpath}\"\n")
        vars_file.write(f"file_name: \"/{service}.yaml\"\n")
        vars_file.write(f"replace_string: \"{tag}\"\n")

def deploy_with_ansible(inventory_group, dpath):
    playbook_path = "Ansible/playbooks/deployment.yaml"
    command = f"ansible-playbook -i inventory -l {inventory_group} {playbook_path} -e dpath={dpath}"
    subprocess.run(command, shell=True)

def main():
    folder = get_user_folder_choice()
    service, tag = get_user_input()
    inventory_group = get_inventory_group()
    update_ansible_vars(folder, service, tag, dpath)
    deploy_with_ansible(inventory_group, dpath)

if __name__ == "__main__":
    main()















