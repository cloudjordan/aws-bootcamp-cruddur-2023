# This script installs PostgreSQL and its related packages, and installs the Python packages required by the Flask backend
# Only use this after resuming a workspace that has timed out.
# To use it, paste this into shell: ./setup-environment.sh

#! /usr/bin/bash

# Get the full path of the backend-flask directory
psql_path=$(realpath .)/backend-flask

curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
sudo apt update
sudo apt install -y postgresql-client-13 libpq-dev

# Change to the backend-flask directory and install requirements
cd $psql_path && pip install -r requirements.txt


