import openai
import json


def fetch_answers_from_gpt(questions_file, output_file, api_key):
    # Load questions from the JSON file
    with open(questions_file, 'r', encoding='utf-8') as file:
        questions = json.load(file)

    # Initialize OpenAI client with your API key
    openai.api_key = api_key

    # Open the output file for writing and start a JSON array
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('[')  # Start of JSON array
        first_entry = True

        # Loop through questions and send them to GPT-3.5
        for key, question in questions.items():
            try:
                full_prompt = f"Can you translate this to French. Please keep the latex intact: {question}"
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system",
                               "content": "Translate the following English text to French, keeping LaTeX code intact."},
                              {"role": "user", "content": question}],
                    max_tokens=1000
                )
                response_text = response['choices'][0]['message']['content'].strip()

                # Serialize response to JSON and write to the file
                response_entry = json.dumps({key: response_text}, ensure_ascii=False)
                if not first_entry:
                    outfile.write(',')  # Add comma before entry if it's not the first one
                outfile.write(response_entry)
                first_entry = False

                print(f"Question {key} done!")
            except Exception as e:
                print(f"Error processing question {key}: {str(e)}")
                error_response = json.dumps(
                    {key: "Error: Unable to process question due to invalid input or server error."})
                if not first_entry:
                    outfile.write(',')
                outfile.write(error_response)
                first_entry = False

        outfile.write(']')  # End of JSON array


def main():
    questions_file = 'data/sequential_questions_output.json'
    output_file = 'translated_french.json'
    # api_key = 'your-openai-api-key'  # Make sure to use your actual OpenAI API key

    fetch_answers_from_gpt(questions_file, output_file, api_key)


if __name__ == "__main__":
    main()
