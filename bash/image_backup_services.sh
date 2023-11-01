#!/bin/bash

# Directory to save the Docker service images
backup_dir="/home/bahl/Documents/devops-document/DevOps-Practice/bash/backup"

# Get the list of image names from Docker services and create backup
docker service ls --format "{{.Image}}" | while read -r image; do
    # Extract image name after the last '/'
    image_name=$(echo "$image" | awk -F '/' '{print $NF}')
    
    # Skip if the image name is empty
    if [[ -n "$image_name" ]]; then
        # Replace ':' in the image name with '-'
        image_name=$(echo "$image_name" | tr ':' '-')
        
        # Backup the image as a tarball
        docker save -o "$backup_dir/$image_name.tar" "$image"
        
        echo "Backup created for image: $image_name"
    else
        echo "Skipping invalid image: $image"
    fi
done

echo "Backup process completed."
