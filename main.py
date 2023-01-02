# importing necessary libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# function to generate cloud for the sentence
def normal(inp):
    word = WordCloud().generate(inp)
    return word


# function to carry out test without using gradio.
def image(ret_word):
    plt.figure()    # creates figure for matplotlib to display.
    plt.imshow(ret_word, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# call function to generate cloud for sentence from the user.
# re_word = create(into)
# image(re_word)
