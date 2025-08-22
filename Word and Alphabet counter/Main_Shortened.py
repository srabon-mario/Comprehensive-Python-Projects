def WordAndAlphabet(s):
    return len(s.split()),sum(c.isalpha() for c in s)    #Wrote this as a shorter version of previous main code.

text = input("Hey Please enter an Senterce ---")
words,alpha = WordAndAlphabet(text)
print(f"So the sentence is \"{text}\"")
print(f"Number of the words in the sentence are--{words}")
print(f"Number of the alphabets in the sentence are--{alpha}")
