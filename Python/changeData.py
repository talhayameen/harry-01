import json

# Load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Modify JSON data
def modify_json(data):
    data['age'] = 35
    data['city'] = 'San Francisco'

# Save JSON data to a file
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Main function
def main():
    file_path = 'data.json'

    # Load JSON data from the file
    json_data = load_json(file_path)

    # Modify JSON data
    modify_json(json_data)

    # Save modified JSON data back to the file
    save_json(json_data, file_path)

if __name__ == "__main__":
    main()
