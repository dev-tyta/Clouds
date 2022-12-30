# importing necessary libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# receives input from user
into = input("Put in a sentence: ")


# function to generate cloud for the sentence
def create(inp):
    word = WordCloud().generate(inp)
    return word


def image(ret_word):
    plt.figure()    # creates figure for matplotlib to display.
    plt.imshow(ret_word, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# # call function to generate cloud for sentence from the user.
# re_word = create(into)
# image(re_word)
