import gradio as gr
from main import normal
import matplotlib.pyplot as plt


def greet(name):
    return f"Hello {name}! Welcome to our test page!"


def inpt(text):
    created_cloud = normal(text)
    fig, ax = plt.subplots()
    ax = plt.imshow(created_cloud)
    gr.pyplot(fig)


demo = gr.Interface(fn=inpt, inputs="text", outputs="image")

if __name__ == "__main__":
    demo.launch(debug=True)
