# import json
# import subprocess
#
#
# def convert_latex_with_pandoc(latex_str):
#     """Convert LaTeX string to plain text using Pandoc."""
#     try:
#         process = subprocess.run(
#             ['pandoc', '--from=latex', '--to=plain'],
#             input=latex_str.encode('utf-8'),
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )
#         return process.stdout.decode('utf-8').strip()
#     except subprocess.SubprocessError as e:
#         print(f"Error during Pandoc conversion: {e}")
#         return latex_str  # Return original if error
#
#
# def remove_latex_from_questions(data):
#     """Process each question to remove LaTeX."""
#     processed_data = {}
#     for key, question in data.items():
#         processed_data[key] = convert_latex_with_pandoc(question)
#     return processed_data
#
#
# # Load JSON data
# def load_and_process_json(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#
#     # Process questions to remove LaTeX
#     processed_data = remove_latex_from_questions(data)
#
#     # Save the modified JSON
#     processed_filename = 'processed_' + filename
#     with open(processed_filename, 'w', encoding='utf-8') as file:
#         json.dump(processed_data, file, ensure_ascii=False, indent=4)
#
#     print("Processed data saved to:", processed_filename)
#
#
# # Example usage with the file you uploaded
# load_and_process_json(
#     'sequential_questions_output.json')  # Update 'path_to_your_file.json' to your actual file path

import subprocess


def convert_latex_to_text(latex_str):
    """Converts LaTeX embedded text to plain text using Pandoc."""
    try:
        # Setup the Pandoc command to convert LaTeX to plain text
        process = subprocess.run(
            ['pandoc', '--from=latex', '--to=plain'],
            input=latex_str.encode('utf-8'),  # Encode the input string to bytes
            stdout=subprocess.PIPE,  # Capture the output
            stderr=subprocess.PIPE  # Capture any errors
        )
        # Decode the output from bytes to string
        return process.stdout.decode('utf-8')
    except subprocess.SubprocessError as e:
        print(f"Error during Pandoc conversion: {e}")
        return latex_str  # Return original string in case of an error


# The LaTeX string, you would replace the content of `latex_content` with your actual LaTeX text
latex_content = """
        "question": "عصا خشبية موحدة ذات كتلة $1.6 \\mathrm{~kg}$ وطول $l$ تستريح بزاوية مائلة على جدار عمودي ناعم بارتفاع $h(<l)$ بحيث تمتد جزءٌ صغير من العصا إلى خارج الجدار. قوة رد الفعل من الجدار على العصا هي عمودية على العصا. تكون العصا بزاوية $30^{\\circ}$ مع الجدار وسفل العصا على أرضية خشنة. إن قوة رد الفعل من الجدار على العصا تكون متساوية في القيمة لقوة رد الفعل من الأرض على العصا. النسبة $h/l$ وقوة الاحتكاك $f$ عند أسفل العصا هي\n\n$\\left(g=10 \\mathrm{~ms} \\mathrm{~s}^{2}\\right)$\n\n(A) $\\frac{h}{l}=\\frac{\\sqrt{3}}{16}, f=\\frac{16 \\sqrt{3}}{3} \\mathrm{~N}$\n\n(B) $\\frac{h}{l}=\\frac{3}{16}, f=\\frac{16 \\sqrt{3}}{3} \\mathrm{~N}$\n\n(C) $\\frac{h}{l}=\\frac{3 \\sqrt{3}}{16}, f=\\frac{8 \\sqrt{3}}{3} \\mathrm{~N}$\n\n(D) $\\frac{h}{l}=\\frac{3 \\sqrt{3}}{16}, f=\\frac{16 \\sqrt{3}}{3} \\mathrm{~N}$",

"""

# Call the function and print the result
plain_text = convert_latex_to_text(latex_content)
print(plain_text)
