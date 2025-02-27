#!/bin/bash

# Check if the user provided two arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <problem_type> <problem_name>"
    exit 1
fi

# Capture inputs and remove any trailing slash from problem_type
problem_type=${1%/}
problem_name=$2

# Define the base directory for the problem
base_dir="./$problem_type/$problem_name"

# Create the directory structure
mkdir -p "$base_dir"

# Create the necessary files
touch "$base_dir/README.md"
touch "$base_dir/solution.py"

# Add a basic structure to solution.py
echo "class Solution:" > "$base_dir/solution.py"
echo "    def your_method(self):" >> "$base_dir/solution.py"
echo "        pass" >> "$base_dir/solution.py"

# Feedback to user
echo "Directory and files created successfully at $base_dir."
