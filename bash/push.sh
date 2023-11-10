#!/bin/bash

# Navigate to your project directory
cd /home/bahl/Documents/devops-document/DevOps-Practice

# Add a space to the README file
echo " " >> /home/bahl/Documents/devops-document/DevOps-Practice/README.md
echo "Hello from dexter" >> /home/bahl/Documents/devops-document/DevOps-Practice/README.md

# Stage and commit changes
git add README.md
git commit -m "Adding py"

# Push changes to the repository
git push origin main

#crontab -e
#0 8,14,20 * * * /path/to/your/project/git_push_script.sh