import gradio as gr
from main import create, image


def greet(name):
    return f"Hello {name}! Welcome to our test page!"


def inpt(text):
    created_cloud = create(text)
    gr.ImageMask(image_mode= created_cloud)
    # image(created_cloud)


demo = gr.Interface(fn=inpt, inputs="text", outputs="image")

demo.launch(share=True)
