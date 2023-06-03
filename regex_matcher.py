import re


class RegexMatcher:
    def __init__(self, regex_file_path):
        self.regex_file_path = regex_file_path
        self.expressions = self.load_regex()

    def load_regex(self):
        with open(self.regex_file_path, 'r', encoding='utf-8') as regex_file:
            patterns = {}
            current_category = None
            for line in regex_file:
                if line.startswith("--"):
                    current_category = line.rstrip('\n')[2:]
                elif current_category is not None:
                    patterns[current_category] = re.compile(line.rstrip('\n'))
        return patterns

    def find_matching_strings(self, input_data):
        matches = {}

        if isinstance(input_data, str) and input_data.endswith('.txt'):
            try:
                with open(input_data, 'r') as file:
                    text = file.read()
            except FileNotFoundError:
                print(f"No file found at {input_data}. Please input valid file path or string.")
                return
        else:
            text = input_data

        for category, pattern in self.expressions.items():
            category_matches = []
            for match in pattern.finditer(text):
                if match.group():  
                    category_matches.append((match.group(), match.start(), match.end()))
            matches[category] = category_matches
            
        # Removing overlaps
        sorted_matches = sorted([(cat, match) for cat, match_list in matches.items() for match in match_list], key=lambda x: (x[1][1], -x[1][2]))
        non_overlapping_matches = {}

        current_category, (current_match, current_start, current_end) = sorted_matches[0]
        non_overlapping_matches[current_category] = [(current_match, current_start, current_end)]

        #dates still matching as phone numbers. Need to prioritize size of match somehow
        for cat, (match, start, end) in sorted_matches[1:]:
            if start >= current_end:
                current_category, current_match, current_start, current_end = cat, match, start, end
                if current_category not in non_overlapping_matches:
                    non_overlapping_matches[current_category] = []
                non_overlapping_matches[current_category].append((current_match, current_start, current_end))
            elif end > current_end:  # New condition: If the match ends after the current one, update the current match.
                current_category, current_match, current_end = cat, match, end
                non_overlapping_matches[current_category][-1] = (current_match, current_start, current_end)  # Replace the last added match with the new larger one

        return non_overlapping_matches


        # # Removing overlaps
        # sorted_matches = sorted([(cat, match) for cat, match_list in matches.items() for match in match_list], key=lambda x: (x[1][1], -x[1][2]))
        # non_overlapping_matches = {}

        # current_category, (current_match, current_start, current_end) = sorted_matches[0]
        # non_overlapping_matches[current_category] = [(current_match, current_start, current_end)]

        # for cat, (match, start, end) in sorted_matches[1:]:
        #     if start >= current_end:
        #         current_category, current_match, current_start, current_end = cat, match, start, end
        #         if current_category not in non_overlapping_matches:
        #             non_overlapping_matches[current_category] = []
        #         non_overlapping_matches[current_category].append((current_match, current_start, current_end))

        # return non_overlapping_matches
