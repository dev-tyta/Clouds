# importing necessary libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

into = input("Put in a sentence: ")


def create(inp):
    word = WordCloud().generate(inp)
    return word


