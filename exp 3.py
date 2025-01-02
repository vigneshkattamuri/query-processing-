import pandas as pd

def replace_missing_spaces(input_string):
    char_freq = pd.Series(list(input_string)).value_counts()
    
    
    least_frequent_char = char_freq[char_freq.index != ' '].idxmin()

    modified_string = input_string.replace(' ', least_frequent_char)
    
    return modified_string


input_string = "HelloWorldThisIsTest"
modified_string = replace_missing_spaces(input_string)
print("Modified String:", modified_string)
