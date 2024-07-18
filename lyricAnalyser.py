import string 
translator = str.maketrans("", "", string.punctuation)



with open("lyrics.txt", "r") as file:
    lyrics = file.readlines()

wordFreq={}
for line in lyrics:
    for word in line.split():
        word = word.lower()
        if "[" in word:
            pass

        else:
            word = word.translate(translator)
            if word not in wordFreq.keys():
                wordFreq[word] = 1
            else:
                wordFreq[word] += 1
            
import matplotlib.pyplot as plt 
import seaborn as sns

# xVal = wordFreq.keys()
# yVal = wordFreq.values()


xVal = list(wordFreq.keys())
xVal.sort()
yVal = [wordFreq[i] for i in xVal]

sns.barplot(x=xVal, y=yVal, hue=yVal)

# y_pos=range(len(x))

# plt.bar(y_pos,y)
plt.xticks(range(len(xVal)), xVal, rotation=90)
plt.show()