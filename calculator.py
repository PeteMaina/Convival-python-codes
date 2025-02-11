'''This code utilizes multiple languages inclusive of
HTML, CSS and python to form a calculator

code by Peter Maina

Email me peterwahomemaina003@gmail.com'''

!pip install ipywidgets

import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
import math

# Create widgets
input_widget = widgets.Text(placeholder="Enter expression", disabled=True)  # Input display, read-only
output_widget = widgets.Output()  # Result display
buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '√',
    '1', '2', '3', '-', '^',
    '0', '.', '=', '+'
]
button_widgets = [widgets.Button(description=b) for b in buttons]

# Layout
grid = widgets.GridBox(
    button_widgets,
    layout=widgets.Layout(grid_template_columns="repeat(5, 1fr)")
)

# CSS styling for the calculator
style = """
<style>
.calculator-container {
    width: 100px; 
    height: 300px; 
    border: 1px solid #ccc;
    padding: 10px;
    display: flex;
    flex-direction: column; 
    overflow: none;
}

.calculator-input {
    flex: 1; 
    margin-bottom: 10px;
}

.calculator-buttons {
    display: grid;
    grid-template-columns: repeat(5, 1fr); 
    grid-gap: 5px;
}

.calculator-button {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
    cursor: pointer;
}
</style>
"""

# Create a container for the calculator
calculator_container = widgets.VBox([
    widgets.HTML(style),
    widgets.HBox([input_widget], layout=widgets.Layout(justify_content='center')),
    widgets.HBox([output_widget], layout=widgets.Layout(justify_content='center')),
    grid
], layout=widgets.Layout(width='auto', height='auto', align_items='center'))

# Display the container
display(calculator_container)

# Initialize display value
display_value = ''

# Function to handle button clicks
def on_button_click(b):
    global display_value
    button_value = b.description

    if button_value == '=':
        try:
            result = eval(display_value)
            with output_widget:
                clear_output(wait=True)
                print(f"Result: {result}")
        except Exception as e:
            with output_widget:
                clear_output(wait=True)
                print(f"Error: {e}")
    elif button_value == 'C':
        display_value = ''
        input_widget.value = ''
        with output_widget:
            clear_output(wait=True)
    elif button_value == '√':
        try:
            display_value += f"math.sqrt("
            input_widget.value = display_value
        except Exception as e:
            with output_widget:
                clear_output(wait=True)
                print(f"Error: {e}")
    elif button_value == '^':
        display_value += '**'
        input_widget.value = display_value
    else:
        display_value += button_value
        input_widget.value = display_value

# Attach click handlers to buttons
for button in button_widgets:
    button.on_click(on_button_click)