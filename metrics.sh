#!/bin/bash

folder1="psud26/chunked"
folder2="pud26/chunked"

# Read files in folder 1
echo "Files in folder $folder1:"
for file in "$folder1"/*; do
    if [ -f "$file" ]; then
        echo "$file"
        python3 lab.py $file ${file}_metrics
    fi
done

# Read files in folder 2
echo "Files in folder $folder2:"
for file in "$folder2"/*; do
    if [ -f "$file" ]; then
        echo "$file"
         python3 lab.py $file ${file}_metrics
    fi
done
