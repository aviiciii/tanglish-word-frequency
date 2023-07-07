import csv
from collections import Counter

def count_word_frequency(text):
    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    return word_counts

def save_word_frequency_to_csv(word_counts, filename):
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])
        writer.writerows(sorted_word_counts)

# Example usage
with open('input/cleaned_input.txt', 'r') as f:
    text = f.read()

word_counts = count_word_frequency(text)


save_word_frequency_to_csv(word_counts, 'word_frequency.csv')
print("Word frequency CSV file has been created.")
