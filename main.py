from gradio import Interface, Textbox, Blocks, Row, Button, Dropdown, Column, Image



def greet(name):
    return f"Hello {name.title()}"


with Blocks() as ifc:
    with Row():
        text1 = Textbox(label="t1")
        slider2 = Textbox(label="s2")
        drop3 = Dropdown(["a", "b", "c"], label="d3")
    with Row():
        with Column(scale=1, min_width=600):
            text1 = Textbox(label="prompt 1")
            text2 = Textbox(label="prompt 2")
            inbtw = Button("Between")
            text4 = Textbox(label="prompt 1")
            text5 = Textbox(label="prompt 2")
        with Column(scale=2, min_width=600):
            img1 = Image("assets/img.jpg")
            btn = Button("Go").style(full_width=True)

# ifc = Interface(fn=greet, inputs=Textbox(lines=2, placeholder="Name here.."), outputs="text")

ifc.launch()
