# importing necessary libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# receives input from user
into = input("Put in a sentence: ")


# function to generate cloud for the sentence
def create(inp):
    word = WordCloud().generate(inp)
    return word


# call function to generate cloud for sentence from the user.
ret_word = create(into)
plt.figure()    # creates figure for matplotlib to display.
plt.imshow(ret_word, interpolation="bilinear")
plt.axis("off")
plt.show()
