import json

# Load the JSON data
with open('responses.json', 'r') as file:
    data = json.load(file)

# Iterate through the responses
for index, response in enumerate(data):
    try:
        # Check if 'extract' key exists and is properly formatted
        if 'extract' not in response:
            raise ValueError(f"Missing 'extract' in response at index {index}")
        if not isinstance(response['extract'], str):
            raise TypeError(f"'extract' is not a string in response at index {index}")
        # You might want to add more checks depending on what constitutes a 'proper' extract

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        print(json.dumps(response, indent=4))  # Print the problematic object
        break  # Stop execution on the first error

print("Check complete. If no errors were printed, all extracts are present and correct.")
