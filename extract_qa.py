import json


# Load the JSON data from the file
def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# Save answers in a JSON format with a sequential count as keys
def save_sequential_answers_json(data, output_file):
    answers_indexed = {str(i + 1): item['gold'] for i, item in enumerate(data)}

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(answers_indexed, file, ensure_ascii=False, indent=4)


# Example usage
data = load_data('data/dataset.json')
save_sequential_answers_json(data, 'data/sequential_answers.json')
