# Script used to remove only the questions from dataset.json

import json

# Load the JSON data from the file
with open('data/dataset.json', 'r') as file:
    data = json.load(file)

# Create a dictionary to store questions with a sequential key
questions_dict = {}
counter = 1  # Start the counter at 1

# Loop through each item in the JSON data
for item in data:
    # Assign the question to a key based on the current counter value
    questions_dict[str(counter)] = item['question']
    counter += 1  # Increment the counter for the next question

# Write the dictionary to a new JSON file
with open('data/sequential_questions_output.json', 'w', encoding='utf-8') as outfile:
    json.dump(questions_dict, outfile, indent=4)

print("Questions have been successfully extracted and written to sequential_questions_output.json.")
