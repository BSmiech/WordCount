import string
text = open("Twinkle.txt", "r") #opening the txt file
d = dict() #building a dictionary
#making a loop for each verse in the text
for verse in text:
    verse = verse.lower() #putting all words in lower cases
    verse = verse.strip() #removing leading spaces
    verse = verse.translate(verse.maketrans("", "", string.punctuation)) #removing punctuation and special characters
    words = verse.split(" ") #splitting the verse into separate words
    #making a loop for each word in the verse
    for word in words:
        if word in d: #checking if the word is in the dictionary
            d[word] = d[word] + 1 #if yes then add one to the count
        else:
            d[word] = 1 #if not then count=1
#printing the output
for key in list(d.keys()):
    print(key, ":", d[key])
