import gradio as gr


def greet(name):
    return f"Hello {name}! Welcome to our test page!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()
