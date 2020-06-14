#!/bin/bash
rsync -avzP --exclude='.vscode' --exclude='.git' --exclude='.idea' --exclude='venv' --exclude='.gitignore' \
          --exclude='__pycache__' --exclude='sync.sh' --exclude='media' --exclude='static' \
          -e ssh /home/vladimir/projects/machinetools root@109.234.36.63:/home/projects