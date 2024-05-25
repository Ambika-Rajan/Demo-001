def countvowels(s):
    vowels = 'AEIOUaeiou'
    vowelcounts = {v: 0 for v in vowels}

    totalvowels = 0
    for char in s:
        if char in vowels:
            vowelcounts[char] += 1
            totalvowels += 1

    # Combining counts of uppercase and lowercase vowels
    combined_counts = {
        'A': vowelcounts['A'] + vowelcounts['a'],
        'E': vowelcounts['E'] + vowelcounts['e'],
        'I': vowelcounts['I'] + vowelcounts['i'],
        'O': vowelcounts['O'] + vowelcounts['o'],
        'U': vowelcounts['U'] + vowelcounts['u']
    }

    return totalvowels, combined_counts


# String to analyze
input_string = "Guvi Geeks Network Private Limited"

# Get the counts
totalvowels, vowelcounts = countvowels(input_string)

# Print the results
print("Total number of vowels:", totalvowels)
print("Count of each vowel:", vowelcounts)