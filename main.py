#!/usr/bin/env python3

import collections
import nltk

nltk.download("punkt")
nltk.download("stopwords")



# Only display words and n-grams occurring 2 or more times
min_frequency = 2
# Calculate n-grams up to 3 words
ngram_words = 3
# Display the top 15 n-grams
display_top_ngrams = 15


# Load resume text
with open("resume.txt", "r") as f:
	resume_text = f.read()

# Tokenize the text into words
words = nltk.tokenize.word_tokenize(resume_text)
# Remove stopwords and punctuation
stop_words = set(nltk.corpus.stopwords.words("english"))
words_filtered = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

# Calculate word frequencies
word_freq = collections.Counter(words_filtered)
most_common_words = word_freq.most_common()
print(f"Word frequencies:")
for word, freq in most_common_words:
	if freq >= min_frequency:
		print(f"{word} : {freq}")

# Calculate n-grams
for i in range(2, ngram_words + 1):
	ngram_freq = collections.Counter(nltk.ngrams(words_filtered, i))
	most_common_ngrams = ngram_freq.most_common(display_top_ngrams)
	print(f"\nTop {display_top_ngrams} {i}-grams:")
	for ngram, freq in most_common_ngrams:
		if freq >= min_frequency:
			print(" ".join(ngram), ":", freq)
