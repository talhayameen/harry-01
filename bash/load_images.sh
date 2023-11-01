#!/bin/bash

# Directory where the Docker service images are saved
backup_dir="/home/bahl/Documents/devops-document/DevOps-Practice/bash/backup"

# Registry address and host
host_ip=0.0.0.0
registry="{host_ip:5000}"

# List all tar files in the backup directory
for tar_file in "$backup_dir"/*.tar; do
    # Extract image name from the tar file name
    image_name=$(basename "$tar_file" | sed 's/\.tar//')

    # Load the Docker image from the tar file
    docker load -i "$tar_file"

    # Tag the loaded image with registry address and namespace
    docker tag "$image_name" "$registry/$image_name"

    # Push the tagged image to the registry
    docker push "$registry/$image_name"

    echo "Image '$image_name' loaded, tagged, and pushed to '$registry'."

    # Clean up: remove the loaded image to avoid conflicts with existing local images
    # docker image rm "$image_name"

done

echo "Image loading, tagging, and pushing process completed."
