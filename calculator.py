import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        """
           Entry
        7 8 9 ÷ DEL
        4 5 6 x CE
        1 2 3 - CE
        , 0   + =
        """

        cols = 5
        rows = 5
        standart_widget_width = 1 / cols
        standart_widget_height = 1 / rows

        main_layout = FloatLayout()
        entry_label = Label(pos_hint={'x': 0., 'y': 1.}, size_hint=(1., standart_widget_height))
        buttons = {'7': Button(text='7'), '8': Button(text='8'), '9': Button(text='9'), '÷': Button(text='÷'), 'del': Button(text='DEL'),
                   '4': Button(text='4'), '5': Button(text='5'), '6': Button(text='6'), 'x': Button(text='x'), 'clear': Button(text='CE'),
                   '1': Button(text='1'), '2': Button(text='2'), '3': Button(text='3'), '-': Button(text='-'),
                   ',': Button(text=','), '0': Button(text='0'),                        '+': Button(text='+'), '=': Button(text='=')}

        main_layout.add_widget(entry_label)
        for button in buttons.values():
            main_layout.add_widget(button)

        return main_layout