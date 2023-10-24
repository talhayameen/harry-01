import os
import pandas as pd

# Excel sheet se data read karna
df = pd.read_excel('path/to/excel/sheet.xlsx')


namespace_folders = ["aaa", "aaa-teller", "crm", ...]

for namespace in namespace_folders:
    folder_path = f'/path/to/kubernetes/cluster/{namespace}'
    yaml_files = [file for file in os.listdir(folder_path) if file.endswith('.yaml')]

    for yaml_file in yaml_files:
        with open(os.path.join(folder_path, yaml_file), 'r') as file:
            yaml_content = yaml.load(file, Loader=yaml.FullLoader)
            # Ab aap yaml_content mein changes kar sakte hain

for index, row in df.iterrows():
    service_name = row['services']
    new_tag = row['tags']

    # Namespace folders aur YAML files ko loop mein iterate karein
    # Agar service_name match hota hai to uss service ke image tag ko update karein
with open(os.path.join(folder_path, yaml_file), 'w') as file:
    yaml.dump(yaml_content, file)


