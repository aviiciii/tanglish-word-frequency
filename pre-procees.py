import re
import string

# read the raw text
with open('input/combined_input.txt', 'r') as f:
    raw_text = f.read()
words = raw_text.split(' ')
print('Total words: ', len(words))
total_words = len(words)


def remove_emojis_from_list(text_list):
    emoji_pattern = re.compile("[^\x00-\x7F]+")
    text_list_without_emojis = []

    for text in text_list:
        text_without_emojis = emoji_pattern.sub('', text)
        text_list_without_emojis.append(text_without_emojis)

    return text_list_without_emojis



def remove_punctuations_from_list(text_list):
    text_list_without_punctuations = []

    for text in text_list:
        # Remove punctuations using the string.punctuation constant
        text_without_punctuations = text.translate(str.maketrans("", "", string.punctuation))
        text_list_without_punctuations.append(text_without_punctuations)

    return text_list_without_punctuations

def remove_numbers_from_list(text_list):
    text_list_without_numbers = []

    for text in text_list:
        # Remove numbers using regular expressions
        text_without_numbers = re.sub(r'\d+', '', text)
        text_list_without_numbers.append(text_without_numbers)

    return text_list_without_numbers


# remove the empty string
words = [word for word in words if word != '']
after_remove_empty = len(words)
print('Removed empty: ', total_words - after_remove_empty)

# remove emojis
words = remove_emojis_from_list(words)
after_remove_emojis = len(words)
print('Removed emojis: ', after_remove_empty - after_remove_emojis)

# remove punctuations
words = remove_punctuations_from_list(words)
after_remove_punctuations = len(words)
print('Removed punctuations: ', after_remove_emojis - after_remove_punctuations)


# remove numbers
words = remove_numbers_from_list(words)
after_remove_numbers = len(words)
print('Removed numbers: ', after_remove_punctuations - after_remove_numbers)


# remove single characters
words = [word for word in words if len(word) > 1]
after_remove_single_characters = len(words)


