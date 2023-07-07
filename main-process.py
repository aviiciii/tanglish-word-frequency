import csv
from collections import Counter

def count_word_frequency(text):
    # Split the text into words
    words = text.split()

    # lowercase all the words
    words = [word.lower() for word in words]

    # Count the frequency of each word
    word_counts = Counter(words)

    return word_counts

def save_word_frequency_to_csv(word_counts, filename):
    # Sort the word-frequency pairs by frequency in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Write the word-frequency pairs to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])
        writer.writerows(sorted_word_counts)

# Read the text from the cleaned input file
with open('input/cleaned_input.txt', 'r') as f:
    text = f.read()

# Count the frequency of each word
word_counts = count_word_frequency(text)

# Save the word-frequency pairs to a CSV file
save_word_frequency_to_csv(word_counts, 'word_frequency.csv')
print("Done!")
