#!/bin/bash
rsync -avzP --exclude='.vscode' --exclude='.git' --exclude='.idea' --exclude='venv' --exclude='.gitignore' \
          --exclude='__pycache__' --exclude='sync.sh' \
          -e ssh /home/vladimir/projects/diplom root@212.109.195.15:/home/projects