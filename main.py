import re 

#Set Up File Paths
dictionary_file = "dictionary_words.txt"
sequence_file = "sequence.txt"
words_file = "words.txt"

#Define regular expression for valid word characters
word_regex = re.compile(r"^[a-zA-Z]+$")

#Function to extract unique sequences from a word
def get_sequences(word):
    sequences = set()
    for i in range (len(word) - 3):
        sequence = word[i:i+4].lower()
        if sequence.isalpha():
            sequences.add(sequence)
    return sequences

#initialize data
word_sequences = {}
unique_sequences = set()
nonunique_sequences = set()

#Open dictionary file and adjust the logic to each list that should receive values
with open(dictionary_file) as f:
    for line in f:
        word = line.strip() 
        
        if word_regex.match(word):
            sequences = get_sequences(word) 

            for sequence in sequences:
                if sequence in nonunique_sequences:
                    continue
                elif sequence in unique_sequences:
                    word_sequences.pop(sequence, None)
                    unique_sequences.remove(sequence)
                    nonunique_sequences.add(sequence)
                else:
                    word_sequences[sequence] = word
                    unique_sequences.add(sequence)


#Add the values of each list to the realted files
with open(sequence_file, "w") as f:
    # f.truncate()
    for sequence in sorted(unique_sequences):
        f.write(sequence + "\n")

with open(words_file, "w") as f:
    # f.truncate()
    for word in sorted(unique_sequences):
        f.write(word_sequences[word] + "\n")       
