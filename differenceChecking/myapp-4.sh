#!/bin/bash

# Define the directory structure
BASE_DIR="/home/bahl/Documents/devops-document/DevOps-Practice/differenceChecking"
ENVIRONMENTS=("pilot" "pre-prod")

# Function to extract base name from a filename
get_base_name() {
    echo "$1" | awk -F '[-.]' '{print $1}'
}

# Function to compare environment variable differences
compare_environments() {
    env1_files=("$1"/*)
    env2_files=("$2"/*)

    for file1 in "${env1_files[@]}"; do
        base_name1=$(get_base_name "$(basename "$file1")")

        for file2 in "${env2_files[@]}"; do
            base_name2=$(get_base_name "$(basename "$file2")")

            if [ "$base_name1" == "$base_name2" ]; then
                # Compare YAML files and extract environment variable differences
                diff_result=$(diff -u <(grep -E '^\s*[-]?\s*\w*:\s*\w*' "$file1" | sort) <(grep -E '^\s*[-]?\s*\w*:\s*\w*' "$file2" | sort))

                if [ -n "$diff_result" ]; then
                    echo "Differences in environment variables for $base_name1:"
                    echo "$diff_result"
                    echo "-----------------------------------"
                fi
            fi
        done
    done
}

# Main loop to iterate through environments
for ((i = 0; i < ${#ENVIRONMENTS[@]}; i++)); do
    for ((j = i + 1; j < ${#ENVIRONMENTS[@]}; j++)); do
        echo "Comparing ${ENVIRONMENTS[i]} with ${ENVIRONMENTS[j]}"
        compare_environments "$BASE_DIR/${ENVIRONMENTS[i]}" "$BASE_DIR/${ENVIRONMENTS[j]}"
    done
done
