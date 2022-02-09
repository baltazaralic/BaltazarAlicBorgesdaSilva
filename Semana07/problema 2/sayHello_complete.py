from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):


        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # label widget
        self.brand = Label(
                        text="Social Lion",
                        font_name='Comic',
                        font_size=25,
                        color='#FFFFFF'
                        )
        self.window.add_widget(self.brand)

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.greeting = Label(
                        text="Sign In:\n Write your name",
                        font_size=18,
                        color='#00FF99'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline=False,
                    padding_y=(20, 20),
                    size_hint=(1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text="Subscribe",
                      size_hint=(1, 0.5),
                      bold=True,
                      background_color='#00FF99',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.greeting.text = "Bem Vindo " + self.user.text + "!"

# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()
