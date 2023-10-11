#!/bin/bash

# Define variables
file_path="$1"  # Pass the file path as the first argument when running the script
new_tag="$2"    # Pass the new tag as the second argument

# Check if all required arguments are provided
if [ -z "$file_path" ] || [ -z "$new_tag" ]; then
  echo "Usage: $0 <file_path> <new_tag>"
  exit 1
fi

# Ensure the file exists
if [ ! -f "$file_path" ]; then
  echo "File not found: $file_path"
  exit 1
fi

# Use sed with regex to replace the tag in the file
sed -i -E 's@(harbor\.teresol\.com/[^:]+:)[^[:space:]]*@\1'"${new_tag}"'@g' "$file_path"

# Optional: Print a message to confirm the replacement
echo "Replaced tag matching pattern with '${new_tag}' in '${file_path}'"
