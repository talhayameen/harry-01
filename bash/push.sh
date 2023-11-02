#!/bin/bash

# Navigate to your project directory
cd /home/bahl/Documents/DevOps-Practice

# Add a space to the README file
echo " " >> /home/bahl/Documents/DevOps-Practice/README.md

# Stage and commit changes
git add README.md
git commit -m "Adding py by abdullah"

# Push changes to the repository
git push origin abdullah
