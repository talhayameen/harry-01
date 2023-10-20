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

# List of envoirnment
envoirnment = [
    "dev",
    "integration",
    "dev + integration",
    "qa",
    "staging",
    "qa + staging"
]

#user envoirnment numbering
def get_user_envoirnment_choice():
    print("Choose the envoirnment")
    for index, envoinment in enumerate(envoinment, start=1):
        print(f"{index}. {envoinment}")
    while True:
      try:
          choiceEnv = int(input("Enter the number of Envoirnment where you want to deploy"))
          if 1 <= choiceEnv <= len(envoinment):
              return envoinment[choiceEnv - 1]
          else:
              print("Invalid choice. Please enter a valid number.")
      except ValueError:
              print("Invalid input. Please enter a number.")


#user folder numbering
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



#user input for service name
def get_user_input():
    service = input("Enter the service name: ")
    tag = input(f"Enter the tag for the {service} service: ")
    return service, tag


#user input for envoirnment name such as dev , qa etc
def get_inventory_group():
    return input("Enter the inventory group to deploy to: ")


#updating vars 
def update_ansible_vars(folder, service, tag, dpath):
    vars_file_path = f"/home/bahl/Documents/devops-document/DevOps-Practice/Ansible/vars/dev_vars.yaml"
    if not os.path.exists(os.path.dirname(vars_file_path)):
        os.makedirs(os.path.dirname(vars_file_path))


    with open(vars_file_path, 'w') as vars_file:
        vars_file.write(f"dpath: \"{dpath}\"\n")
        vars_file.write(f"file_name: \"{folder}/{service}\"\n")
        vars_file.write(f"replace_string: \"{tag}\"\n")

def deploy_with_ansible(inventory_group, dpath):
    playbook_path = "/home/bahl/Documents/devops-document/DevOps-Practice/Ansible/playbooks/deployment.yaml"
    command = f"ansible-playbook -i inventories/inventory -l {inventory_group} {playbook_path} -e dpath={dpath}"
    subprocess.run(command, shell=True)

#MAIN 
def main():
    folder = get_user_folder_choice()
    service, tag = get_user_input()
    inventory_group = get_inventory_group()
    update_ansible_vars(folder, service, tag, dpath)
    deploy_with_ansible(inventory_group, dpath)

if __name__ == "__main__":
    main()















