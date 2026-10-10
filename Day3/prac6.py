# Character Replacement Medium
# Ask the user to enter a sentence. Replace every occurrence of "bad" with "good" and print the updated sentence.
# Then count how many times the word "good" appears in the updated sentence.
sentence = input("Enter a sentence: ")
updated_sentence = sentence.replace("bad", "good")
print("Updated sentence:", updated_sentence)
count = updated_sentence.count("good")
print("Number of times 'good' appears:", count)