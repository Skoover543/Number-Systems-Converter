import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button as DropDownButton

kivy.require('2.0.0')


class ConverterApp(App):
    def build(self):
        self.title = "Number Base Converter"

        # Layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input field
        self.textInput = TextInput(hint_text='Enter number', multiline=False, size_hint=(1, 0.1))
        layout.add_widget(self.textInput)

        # Horizontal layout for dropdowns
        dropdown_layout = BoxLayout(size_hint=(1, 0.1))

        # Dropdown for conversion options
        self.convert_from_dropdown = DropDown()
        self.convert_to_dropdown = DropDown()

        # Conversion types
        conversion_types = ['Decimal', 'Binary', 'Octal', 'Hexadecimal']

        # Creating dropdown buttons
        self.from_button = DropDownButton(text='Convert From', size_hint=(1, 1))
        self.to_button = DropDownButton(text='Convert To', size_hint=(1, 1))

        for option in conversion_types:
            button_from = Button(text=option, size_hint_y=None, height=30)
            button_from.bind(on_release=lambda buttonOne: self.select_from(buttonOne.text))
            self.convert_from_dropdown.add_widget(button_from)

            button_to = Button(text=option, size_hint_y=None, height=30)
            button_to.bind(on_release=lambda btn: self.select_to(btn.text))
            self.convert_to_dropdown.add_widget(button_to)

        self.from_button.bind(on_release=self.convert_from_dropdown.open)
        self.to_button.bind(on_release=self.convert_to_dropdown.open)

        dropdown_layout.add_widget(self.from_button)
        dropdown_layout.add_widget(self.to_button)

        layout.add_widget(dropdown_layout)

        # Convert button
        convert_button = Button(text='Convert', size_hint=(1, 0.1))
        convert_button.bind(on_press=self.convert)
        layout.add_widget(convert_button)

        # Result label
        self.results = Label(text='Result:', size_hint=(1, 0.1))
        layout.add_widget(self.results)

        return layout

    def select_from(self, selection):
        self.from_button.text = selection
        self.convert_from_dropdown.dismiss()  # Close the dropdown after selection

    def select_to(self, selection):
        self.to_button.text = selection
        self.convert_to_dropdown.dismiss()  # Close the dropdown after selection

    def convert(self, instance):
        from_base = self.from_button.text
        to_base = self.to_button.text
        number = self.textInput.text.strip()

        try:
            if from_base == 'Decimal':
                base10_num = float(number)
            elif from_base == 'Binary':
                base10_num = float(int(number, 2))
            elif from_base == 'Octal':
                base10_num = float(int(number, 8))
            elif from_base == 'Hexadecimal':
                base10_num = float(int(number, 16))

            if to_base == 'Decimal':
                result = str(base10_num)
            elif to_base == 'Binary':
                result = self.float_to_binary(base10_num)
            elif to_base == 'Octal':
                result = self.float_to_octal(base10_num)
            elif to_base == 'Hexadecimal':
                result = self.float_to_hexadecimal(base10_num)

            self.results.text = f"Result: {result}"
        except ValueError:
            self.results.text = "Invalid input!"

    def float_to_binary(self, num):
        if num < 0:
            return '-' + self.float_to_binary(-num)
        whole, fraction = str(num).split(".")
        whole = int(whole)
        fraction = float("0." + fraction)
        wholeBinaryNumber = bin(whole).replace("0b", "")
        Binary_fraction = []

        while fraction:
            fraction *= 2
            bit = int(fraction)
            Binary_fraction.append(str(bit))
            fraction -= bit
            if len(Binary_fraction) > 10:  # Limit to 10 digits after the decimal
                break

        return f"{wholeBinaryNumber}." + ''.join(Binary_fraction)

    def float_to_octal(self, num):
        if num < 0:
            return '-' + self.float_to_octal(-num)
        whole, frac = str(num).split(".")
        whole = int(whole)
        frac = float("0." + frac)
        octal_whole = oct(whole).replace("0o", "")
        octal_frac = []

        while frac:
            frac *= 8
            bit = int(frac)
            octal_frac.append(str(bit))
            frac -= bit
            if len(octal_frac) > 10:  # Limit to 10 digits after the decimal
                break

        return f"{octal_whole}." + ''.join(octal_frac)

    def float_to_hexadecimal(self, num):
        if num < 0:
            return '-' + self.float_to_hexadecimal(-num)
        whole, frac = str(num).split(".")
        whole = int(whole)
        frac = float("0." + frac)
        hex_whole = hex(whole).replace("0x", "")
        hexadecimal = []

        while frac:
            frac *= 16
            bit = int(frac)
            hexadecimal.append(str(hex(bit)[2:]))
            frac -= bit
            if len(hexadecimal) > 10:  # Limit to 10 digits after the decimal
                break

        return f"{hex_whole}." + ''.join(hexadecimal)


if __name__ == "__main__":
    ConverterApp().run()
