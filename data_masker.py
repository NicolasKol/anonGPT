class DataMasker:
    def __init__(self, regex_matcher):
        self.regex_matcher = regex_matcher

    def create_dummies(self, matches):
        dummies = [(category + str(i+1), match)
                   for category, category_matches in matches.items()
                   for i, match in enumerate(category_matches)]
        return dummies

    def substitute(self, input_data):
        matches = self.regex_matcher.find_matching_strings(input_data)

        if isinstance(input_data, str) and input_data.endswith('.txt'):
            try:
                with open(input_data, 'r') as file:
                    text = file.read()
            except FileNotFoundError:
                print(
                    f"No file found at {input_data}. Please input valid file path or string.")
                return
        else:
            text = input_data

        dummies = self.create_dummies(matches)

        dummies.sort(key=lambda x: x[1][1], reverse=True)
        
        for dummy, original in dummies:
            start = original[1]
            length = len(original[0])
            text = text[:start] + dummy + text[start + length:]

        return text, dummies

    def unsubstitute(self, text, dummies):
        for dummy, original in dummies:
            text = text.replace(dummy, original[0])
        return text
