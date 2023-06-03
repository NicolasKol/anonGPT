from regex_matcher import RegexMatcher
from data_masker import DataMasker

matcher = RegexMatcher('./regex.txt')
input_data = "./test.txt"
#input("Please enter the text or path to a text file: ")
matches = matcher.find_matching_strings(input_data)


# for category, category_matches in matches.items():
#     print(f"Category: {category}")
#     for match in category_matches:
#         print(f"Match: {match}")

data_masker = DataMasker(matcher)
text, dummies = data_masker.substitute(input_data)
newtext = data_masker.unsubstitute(text, dummies)
print(text)
print(newtext)