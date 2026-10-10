# Word Search Easy

# Ask the user to enter a sentence and a word to search for. Print the index where the word first appears. If it doesn't appear, print "Word not found".

sentence = input("Enter a sentence: ")
word = input("Enter a word to search for: ")

index = sentence.find(word)
if index != -1:
    print(index)
else:
    print("Word not found")