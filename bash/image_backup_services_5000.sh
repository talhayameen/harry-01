#!/bin/bash

# Directory to save the Docker service images
backup_dir="/home/bahl/Documents/devops-document/DevOps-Practice/bash/backup"

# Get the list of image names from Docker services and create backup
docker service ls --format "{{.Image}}" | while read -r image; do
    # Extract image name after '5000/' (assuming all your images follow this pattern)
    image_name=$(echo "$image" | awk -F '5000/' '{print $2}')
    
    # Skip if the image name is empty or contains '/'
    if [[ -n "$image_name" && ! "$image_name" =~ "/" ]]; then
        # Replace '/' in the image name with '-'
        image_name=$(echo "$image_name" | tr '/' '-')
        
        # Backup the image as a tarball
        docker save -o "$backup_dir/$image_name.tar" "$image"
        
        echo "Backup created for image: $image_name"
    else
        echo "Skipping invalid image: $image"
    fi
done

echo "Backup process completed."
