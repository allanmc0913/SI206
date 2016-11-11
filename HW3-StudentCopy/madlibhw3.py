# Allan Chen, SI206 Homework 3

# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3

import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random

# import nltk
nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize
#import text2 (Sense and Sensibility) file to use for madlib generation
from nltk.book import text2

tokens = text2[0:150]

print("TOKENS")
print("\n\nSTART*******")

def spaced(word):
	if word in [",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word

start_text = list()
#for each item in tokens list
for item in tokens:
	#invoke spaced function on each item, then append into new list
	start_text.append(spaced(item))
#print out elements of the list using join method	
print ("".join(start_text))

tagged_tokens = nltk.pos_tag(tokens)

#changed the percentages and added one more part of speech
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "PRON":"a pronoun"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "PRON":.1}

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print("\n\nEND*******")
print ("".join(final_words))
