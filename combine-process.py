# clean the input
import pandas as pd

# read tsv
df = pd.read_csv('input/tamil_train.tsv', sep='\t', header=None)

# remove the first column and the last column
df = df.drop([1], axis=1)
# remove the first row
df = df.drop([0], axis=0)
# rename the column
df.columns = ['text']

# list of sentences
sentences = df['text'].values

# write to file
with open('input/raw.txt', 'a') as f:
    for s in sentences:
        f.write(s + ' ')

print('Done!')

