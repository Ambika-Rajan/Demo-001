# Import SequenceMatcher from difflib
from difflib import SequenceMatcher


# Function to find longest common substring
def longest_Substring(s1, s2):
    # Create sequence matcher object
    seq_match = SequenceMatcher(None, s1, s2)

    # Find longest matching substring
    match = seq_match.find_longest_match(0, len(s1), 0, len(s2))


    # If match found, return substring
    if (match.size != 0):
        return (s1[match.a: match.a + match.size])

    # Else no match found
    else:
        return ('Longest common sub-string not present')


# Test strings
s1 = 'abcdefgh'
s2 = 'xswerabcdwd'

# Print original strings
print("Original Substrings:\n", s1 + "\n", s2)

# Print message
print("\nCommon longest sub_string:")

# Print longest common substring
print(longest_Substring(s1, s2))
