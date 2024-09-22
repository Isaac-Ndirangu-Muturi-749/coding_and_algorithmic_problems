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
touch "$base_dir/problem.md"
touch "$base_dir/queries.sql"
touch "$base_dir/test_cases.sql"

# Add a basic structure to problem.md
echo "# Problem Statement: $problem_name" > "$base_dir/problem.md"
echo '```sql' >> "$base_dir/problem.md"
echo "" >> "$base_dir/problem.md"
echo "" >> "$base_dir/problem.md"
echo '```' >> "$base_dir/problem.md"

# Add a basic structure to queries.sql
echo "-- Write your MySQL query statement below" > "$base_dir/queries.sql"

# Add a basic structure to test_cases.sql
echo "-- Write your test queries here" > "$base_dir/test_cases.sql"

# Feedback to user
echo "Directory and files created successfully at $base_dir."
