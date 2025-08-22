def WordAndAlphabet(sentence):
    words = sentence.split()
    word_count = len(words)
    alphabet_count = sum(char.isalpha() for char in sentence)
    return word_count,alphabet_count

text = input("Hey Please enter an Senterce ---")
words,alpha = WordAndAlphabet(text)
print(f"So the sentence is \"{text}\"")
print(f"Number of the words in the sentence are--{words}")
print(f"Number of the alphabets in the sentence are--{alpha}")
