import gradio as gr
from main import create, image


def greet(name):
    return f"Hello {name}! Welcome to our test page!"


def inpt(text):
    created_cloud = create(text)
    gr.ImageMask(image_mode=created_cloud)
    # image(created_cloud)


btn = gr.Button("Generate image").style(full_width=False)

gallery = gr.Gallery(label="Generated images", show_label=False, elem_id="gallery"
        ).style(grid=[2], height="auto")

btn.click(inpt, None, gallery)

demo = gr.Interface(fn=inpt, inputs="text", outputs="image")

demo.launch()
