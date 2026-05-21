#!/bin/bash

echo "Installing Aur todo pkg"
yay -S todo --noconfirm

echo "Making python file execulatble"
chmod +x todo.py

echo "Clearing zshrc cache"
hash -r

echo "Copying Python Script"
echo "alias todo='python3 ~/todo/todo.py'" >> ~/.zshrc

source ~/.zshrc
echo "Done"
