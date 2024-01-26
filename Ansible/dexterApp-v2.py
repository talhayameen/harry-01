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

#################################################################################################

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

dpath_mapping = {
    "dev": "/home/teresol/development",
    "integration": "/home/teresol.admin/integration"
    #"qa": "/path/to/qa/directory",
    #"staging": "/path/to/staging/directory",
    # Add other environments and their respective dpath values here
}






def main():
    env = get_user_environment_choice()
    folder = get_user_folder_choice()
    service, tag = get_user_input()
    
    # Define the base path where variable files will be stored
    base_path = "/home/bahl/Documents/devops-document/DevOps-Practice/Ansible/vars"
    
    for environment in environments:
        # Create a subfolder for each environment
        env_folder_path = os.path.join(base_path, environment)
        if not os.path.exists(env_folder_path):
            os.makedirs(env_folder_path)
        
        # Create the file path for the environment-specific variable file
        vars_file_path = os.path.join(env_folder_path, f"{environment}_vars.yaml")
        
        # Get the dpath value based on the environment from the dictionary
        dpath = dpath_mapping.get(environment, "/default/directory/path")
        
        # Update variables in the environment-specific file
        update_ansible_vars(vars_file_path, folder, service, tag, dpath)
        
    deploy_with_ansible(env)
