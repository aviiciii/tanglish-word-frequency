import re
import string

# read the raw text
with open('input/combined_input.txt', 'r') as f:
    raw_text = f.read()
words = raw_text.split(' ')
print('Total words:', len(words))

def remove_noise_from_list(text_list):
    noise_set = set(['', ' ', '\n'])  # Set of noise elements to remove
    emoji_pattern = re.compile("[^\x00-\x7F]+")
    punctuation_table = str.maketrans("", "", string.punctuation)

    text_list_size = len(text_list)
    i = 0
    while i < text_list_size:
        # Remove emojis
        text_list[i] = emoji_pattern.sub('', text_list[i])
        # Remove punctuation
        text_list[i] = text_list[i].translate(punctuation_table)
        # Remove numbers
        text_list[i] = re.sub(r'\d+', '', text_list[i])

        if text_list[i] in noise_set or len(text_list[i]) <= 1:
            # Remove empty strings and single characters
            text_list.pop(i)
            text_list_size -= 1
        else:
            i += 1

    return text_list

# Remove noise from the list of words
words = remove_noise_from_list(words)
after_noise_removal = len(words)

print('Words after noise removal:', after_noise_removal)
