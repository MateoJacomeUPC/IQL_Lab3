#!/bin/bash

folder1="psud26"
folder2="pud26"

# Read files in folder 1
echo "Files in folder $folder1:"
for file in "$folder1"/*; do
    if [ -f "$file" ]; then
        echo "$file"
        python3 /home/jose/Documentos/MIRI/IQL/treebank-parser/cli/main.py -i $file -o ${file}_AC  Head-Vector --ChunkSyntacticDependencyTree Anderson
    fi
done

# Read files in folder 2
echo "Files in folder $folder2:"
for file in "$folder2"/*; do
    if [ -f "$file" ]; then
        echo "$file"
         python3 /home/jose/Documentos/MIRI/IQL/treebank-parser/cli/main.py -i $file -o ${file}_AC --lal Head-Vector --ChunkSyntacticDependencyTree Anderson
    fi
done
