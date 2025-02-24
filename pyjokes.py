'''
This is a snippet to generate Jokes that only a programmer can understand

Email; peterwahomemaina003@gmail.com
'''

#Install pyjokes
!pip install pyjokes

import pyjokes
import ipywidgets as widgets
from IPython.display import display, clear_output


def get_and_display_joke():
    """Gets a joke and displays it."""
    joke = pyjokes.get_joke()
    print(f"Here's a programming joke for you: \n {joke}")


button = widgets.Button(description="Tell Me Another Joke")


def on_button_click(b):
    with out:
        clear_output(wait=True)
        get_and_display_joke()  
        display(button)  


out = widgets.Output()
display(out)  


with out:
    get_and_display_joke()
    display(button)


button.on_click(on_button_click)