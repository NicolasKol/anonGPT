from regex_matcher import RegexMatcher
matcher = RegexMatcher('./regex.txt')
input_data = input("Please enter the text or path to a text file: ")
matches = matcher.find_matching_strings(input_data)

for match in matches:
    print(match)
