#!/bin/bash
rsync -av --exclude='.vscode' --exclude='.git' --exclude='.idea' --exclude='venv' --exclude='.gitignore' \
          --exclude='node_modules' --exclude='package-lock.json' --exclude='package.json' \
          --exclude='.pytest_cache' --exclude='requirements-dev.txt' --exclude='db.sqlite3' \
          --exclude='__pycache__' --exclude='sync.sh' --exclude='gulpfile.js' \
          /home/vladimir/projects/impuls root@109.234.38.203:/home/projects