#!/bin/bash

# Define variables
file_name="$1"  # Pass the file name as the first argument when running the script
search_string="$2"  # Pass the string to search for as the second argument
replace_string="$3"  # Pass the replacement string as the third argument

# Check if all required arguments are provided
if [ -z "$file_name" ] || [ -z "$search_string" ] || [ -z "$replace_string" ]; then
  echo "Usage: $0 <file_name> <search_string> <replace_string>"
  exit 1
fi
# Use sed to replace the string in the file
sed -i "s/$search_string/$replace_string/g" "$file_name"
