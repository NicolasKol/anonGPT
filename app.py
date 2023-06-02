import re
import json


json_file_path = './personal_data_patterns.json'

# Loads Regex from the file


def load_regex(json_file_path):
    try:
        with open(json_file_path) as json_file:
            patterns = json.load(json_file)
        return patterns
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file '{json_file_path}'.")
    except Exception as e:
        print(
            f"Error: An unexpected error occurred while loading regex patterns. {e}")


# Call the function to load the regex patterns
patterns = load_regex(json_file_path)


def find_matching_strings(patterns, input_data):
    # Compile the regex patterns
    compiled_patterns = [re.compile(pattern) for pattern in patterns]

    matches = []

    # If input_data is a file path, read the contents of the file
    if isinstance(input_data, str) and input_data.endswith('.txt'):
        with open(input_data, 'r') as file:
            text = file.read()
        # Iterate over the compiled patterns and find matches in the text
        for pattern in compiled_patterns:
            matches.extend(pattern.findall(text))
    else:
        # If input_data is a string, directly find matches
        for pattern in compiled_patterns:
            matches.extend(pattern.findall(input_data))

    return matches


input_data = ''

expressions = load_regex(json_file_path)
# Find matching strings
matches = find_matching_strings(expressions, input_data)

# Print the matches
for match in matches:
    print(match)
