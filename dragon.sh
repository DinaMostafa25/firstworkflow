#!/bin/bash

echo "Installing cowsay..."
sudo apt-get update -y
sudo apt-get install cowsay -y

echo "Creating dragon.txt..."
cowsay -f dragon "Run for cover, I am a dragon... RAWR" > dragon.txt

echo "Checking file..."
grep -i "dragon" dragon.txt

echo "Displaying file..."
cat dragon.txt
