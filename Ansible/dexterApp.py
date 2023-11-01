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

# List of envoirnment
envoirnments = [
    "dev",
    "integration",
    "dev + integration",
    "qa",
    "staging",
    "qa + staging"
]

#################################################################################################



###################################user folder numbering##################################
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



###################################user input for service name##################################
def get_user_input():
    service = input("Enter the service name: ")
    tag = input(f"Enter the tag for the {service} service: ")
    return service, tag


########################################updating dev vars#######################################

def update_ansible_dev_vars(folder, service, tag):
    vars_file_path = f"/home/bahl/Documents/devops-document/DevOps-Practice/Ansible/vars/dev_vars.yaml"
    if not os.path.exists(os.path.dirname(vars_file_path)):
        os.makedirs(os.path.dirname(vars_file_path))


    with open(vars_file_path, 'w') as vars_file:
        dpath="/home/teresol/development"
        vars_file.write(f"dpath: \"{dpath}\"\n")
        vars_file.write(f"file_name: \"{folder}/{service}\"\n")
        vars_file.write(f"replace_string: \"{tag}\"\n")

#################################################################################################




######################################user envoirnment numbering#################################


def get_user_envoirnment_choice():
    print("Choose the envoirnment")
    for index, envoirnment in enumerate(envoirnments, start=1):
        print(f"{index}. {envoirnment}")
    while True:
      try:

          choiceEnv = int(input("Enter the number of Envoirnment where you want to deploy: "))

          if 1 <= choiceEnv <= len(envoirnments):
              
            if choiceEnv == 1:
              ##########calling folder func#########
              folder = get_user_folder_choice()
              ##########asking service name and tag#########
              service, tag = get_user_input()
            #   dpath="/home/teresol/development"
              update_ansible_dev_vars(folder, service, tag)
              
              return envoirnments[choiceEnv - 1]
          
          else:
              
              print("Invalid choice. Please enter a valid number.")



      except ValueError:
              print("Invalid input. Please enter a number.")


################################################################################################


def deploy_with_ansible(env):

    playbook_path = "/home/bahl/Documents/devops-document/DevOps-Practice/Ansible/playbooks/deployment.yaml"
    command = f"ansible-playbook -i inventories/inventory -l {env} {playbook_path}"
    subprocess.run(command, shell=True)

#MAIN 
def main():
    
    
    env=get_user_envoirnment_choice()
    deploy_with_ansible(env)

if __name__ == "__main__":
    main()















