#!/bin/bash

echo "Setting up my-inventory project..."
chmod +x my-inventory
sudo ln -s "$(pwd)/my-inventory" /usr/local/bin
echo "my-inventory command now runs project!"
