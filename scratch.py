# import json
#
#
# def load_data_from_json(file_path):
#     """Load data from a JSON file."""
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return json.load(file)
#
#
# def merge_questions_answers(questions, answers, language):
#     """Merge questions and answers into a single list of dictionaries, tagging with language."""
#     combined_data = []
#     for key, question in questions.items():
#         combined_entry = {
#             "question_id": key,
#             "language": language,
#             "question": question,
#             "answer": answers.get(key, "")  # Use empty string if no answer is available
#         }
#         combined_data.append(combined_entry)
#     return combined_data
#
#
# def save_data_to_json(data, output_file):
#     """Save data to a JSON file with non-ASCII characters."""
#     with open(output_file, 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)  # ensure_ascii=False to display characters
#     print(f"Data successfully merged and saved to {output_file}")
#
#
# # Dictionary to hold the file paths for each language
# file_paths = {
#     "Arabic": ("test_arabic.json", "data/sequential_answers.json"),
#     "Chinese": ("test_chinese.json", "data/sequential_answers.json"),
#     "English": ("processed_sequential_questions_output.json", "data/sequential_answers.json"),
#     "Hindi": ("test_hindi.json", "data/sequential_answers.json")
# }
#
# # Initialize an empty list to collect all combined data
# all_data = []
#
# # Process each language
# for language, (questions_file, answers_file) in file_paths.items():
#     questions = load_data_from_json(questions_file)
#     answers = load_data_from_json(answers_file)
#     # Merge the questions and answers
#     merged_data = merge_questions_answers(questions, answers, language)
#     all_data.extend(merged_data)
#
# # Save the combined data of all languages to a new JSON file
# output_file = 'merged_multilingual_data.json'
# save_data_to_json(all_data, output_file)

import json


def filter_json_objects(input_file, output_file, start_index, end_index):
    """
    Reads a JSON file, keeps only the objects from start_index to end_index (inclusive),
    and writes the result to a new JSON file.

    :param input_file: str, path to the input JSON file
    :param output_file: str, path to the output JSON file
    :param start_index: int, the starting index of objects to keep (one-based)
    :param end_index: int, the ending index of objects to keep (one-based)
    """
    try:
        # Open and load the JSON data
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Convert one-based index to zero-based for slicing
        zero_based_start_index = start_index - 1
        zero_based_end_index = end_index - 1

        # Check if data is a list and can be sliced
        if isinstance(data, list) and zero_based_start_index < len(data):
            # Filter objects by the specified index range
            filtered_data = data[zero_based_start_index:zero_based_end_index + 1]
        else:
            print("The JSON structure is not a list or start_index is out of range.")
            filtered_data = []

        # Write the filtered data to a new JSON file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(filtered_data, file, ensure_ascii=False, indent=4)

        print(f"Filtered data has been written to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Usage
input_file_path = 'data/cp2_responses/GPT4_0613_normal_responses/english_responses_gpt4.json'  # Adjust this to your input file path
output_file_path = 'data/cp2_responses/GPT4_0613_normal_responses/english_responses1_gpt41.json'  # Adjust this to your desired output file path
start_idx = 102
end_idx = 202

filter_json_objects(input_file_path, output_file_path, start_idx, end_idx)


