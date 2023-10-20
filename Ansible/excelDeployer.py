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
