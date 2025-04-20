import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(App):
    def build(self):
        self.grid = GridLayout(cols=4)
        
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        for button in self.buttons:
            self.grid.add_widget(Button(text=button, on_press=self.on_button_press))
        
        return self.grid

    def on_button_press(self, instance):
        button_text = instance.text
        
        # Add functionality for button presses (you can improve it further)
        if button_text == 'C':
            # Clear the screen
            pass
        elif button_text == '=':
            # Evaluate the expression
            pass
        else:
            # Append the button text to the display
            pass

if __name__ == '__main__':
    CalculatorApp().run()
