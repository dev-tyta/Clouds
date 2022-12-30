import gradio as gr
from main import create, image


def greet(name):
    return f"Hello {name}! Welcome to our test page!"


def inpt(text):
    created_cloud = create(text)
    image()


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()
