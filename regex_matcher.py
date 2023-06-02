import re

class RegexMatcher:
    def __init__(self, regex_file_path):
        self.regex_file_path = regex_file_path
        self.expressions = self.load_regex()

    def load_regex(self):
        with open(self.regex_file_path, 'r', encoding='utf-8') as regex_file:
            patterns = [line.rstrip('\n') for line in regex_file if not line.startswith("--")]
        return [re.compile(pattern) for pattern in patterns]

    def find_matching_strings(self, input_data):
        matches = []

        if isinstance(input_data, str) and input_data.endswith('.txt'):
            try:
                with open(input_data, 'r') as file:
                    text = file.read()
            except FileNotFoundError:
                print(f"No file found at {input_data}. Please input valid file path or string.")
                return
        else:
            text = input_data

        for pattern in self.expressions:
            for match in pattern.finditer(text):
                if match.group():  
                    matches.append((match.group(), match.start()))

        matches = list(dict.fromkeys(matches))
        return matches

