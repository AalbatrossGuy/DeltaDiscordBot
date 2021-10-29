#! /bin/bash

git pull

echo "Installing Dependencies..."

pip install -r requirements.txt

pip install libzbar-cffi==0.2.1

pip install --upgrade discord-components

echo "Dependencies Installation done..."

sleep "3s"

echo "Starting Delta..."

# touch .env

# ENV=".env"

# echo "TOKEN=$TOKEN" >> $ENV 

source ./start.sh
