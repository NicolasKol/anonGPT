from regex_matcher import RegexMatcher
matcher = RegexMatcher('./regex.txt')
input_data = "bla absda dako@hotmail.de dortmund bla bla 5555555555554444 hallo mein name Jens +49176645789" #input("Please enter the text or path to a text file: ")
matches = matcher.find_matching_strings(input_data)

for match in matches:
    print(match)
