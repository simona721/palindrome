#Check if a word is a palindrome
#word = input("Enter a word: ")
#
#if word == "".join(reversed(word)):
#    print(f"The word {word} is a palindrome.")
#else:
#    print(f"The word {word} is not a palindrome.")


#Check which words in a sentence are a palindrome


def palindrome(word):
    return word == word[::-1]

# split sentence into words and filter out the non palindromes
sentence = [w for w in input("Enter a sentence: ").split() if palindrome(w)]

print(f" There are {(len(sentence))} palindromes in your sentence.\n")
# print each palindrome from our list
for pal in sentence:
    print(f"{pal} is a palindrome")