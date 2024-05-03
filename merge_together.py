import json

# Load the JSON file
with open('data/dataset.json', 'r') as file:
    data = json.load(file)

# Load the JSON file
with open('modified_test_chinese.json', 'r', encoding='utf-8') as file:
    hindi_data = json.load(file)

# Update the 'question' field in the original data with Hindi questions
for key, value in hindi_data.items():
    index = int(key) - 1  # Adjust index for zero-based indexing
    data[index]['question'] = value

# Extract the part of the data from index 101 to 201
# data_slice = data[101:201]  # Python slicing includes start index but excludes end index

# Write the extracted data to a new JSON file
with open('data/updated_chinese_dataset.json', 'w', encoding='utf-8') as file:
    json.dump(data_slice, file, ensure_ascii=False, indent=4)
