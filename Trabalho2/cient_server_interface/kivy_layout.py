from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import *
from get_html import *
from client import *




class app_casa(App):
    def build(self):

        global sala, cozinha, quarto, banheiro

        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 2
        self.window.size_hint = (1, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.light_sala = Image(source="images/sala_off.png")
        self.window.add_widget(self.light_sala)

        self.light_cozinha = Image(source="images/cozinha_off.png")
        self.window.add_widget(self.light_cozinha)

        """

        # label widget
        self.sala = Label(
                        text="Sala",
                        font_name='Comic',
                        font_size=25,
                        color='#FFFFFF'
                        )
        self.window.add_widget(self.sala)"""

        self.button_sala = Button(
            text="sala",
            size_hint=(0.5, 0.2),
            bold=True,
            background_color='#000000'
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button_sala.bind(on_press=self.sala_set_light)
        self.window.add_widget(self.button_sala)


        """

        # label widget
        self.cozinha = Label(
            text="Cozinha",
            font_name='Comic',
            font_size=25,
            color='#FFFFFF'
        )
        self.window.add_widget(self.cozinha)"""

        self.button_cozinha = Button(
            text="cozinha",
            # size_hint=(1, 0.5),
            size_hint=(0.5, 0.2),
            bold=True,
            background_color='#000000',
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button_cozinha.bind(on_press=self.cozinha_set_light)
        self.window.add_widget(self.button_cozinha)

        self.light_quarto = Image(source="images/quarto_off.png")
        self.window.add_widget(self.light_quarto)

        self.light_banheiro = Image(source="images/banheiro_off.png")
        self.window.add_widget(self.light_banheiro)

        """

        # label widget
        self.quarto = Label(
            text="Quarto",
            font_name='Comic',
            font_size=25,
            color='#FFFFFF'
        )
        self.window.add_widget(self.quarto)"""

        self.button_quarto = Button(
            text="quarto",
            # size_hint=(1, 0.5),
            size_hint=(0.5, 0.2),
            bold=True,
            background_color='#000000'
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button_quarto.bind(on_press=self.quarto_set_light)
        self.window.add_widget(self.button_quarto)

        """

        # label widget
        self.banheiro = Label(
            text="Banheiro",
            font_name='Comic',
            font_size=25,
            color='#FFFFFF'
        )
        self.window.add_widget(self.banheiro)"""

        self.button_banheiro = Button(
            text="banheiro",
            #size_hint=(1, 0.5),
            size_hint=(0.5, 0.2),
            bold=True,
            background_color='#000000'
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button_banheiro.bind(on_press=self.banheiro_set_light)
        self.window.add_widget(self.button_banheiro)

        Clock.schedule_interval(self.mainloop, 0.05)

        return self.window

    def light_on(self, nome):
        if nome == "sala":
            self.light_sala.set_texture_from_resource("images/sala_on.png")
        if nome == "cozinha":
            self.light_cozinha.set_texture_from_resource("images/cozinha_on.png")
        if nome == "quarto":
            self.light_quarto.set_texture_from_resource("images/quarto_on.png")
        if nome == "banheiro":
            self.light_banheiro.set_texture_from_resource("images/banheiro_on.png")

    def light_off(self, nome):
        if nome == "sala":
            self.light_sala.set_texture_from_resource("images/sala_off.png")
        if nome == "cozinha":
            self.light_cozinha.set_texture_from_resource("images/cozinha_off.png")
        if nome == "quarto":
            self.light_quarto.set_texture_from_resource("images/quarto_off.png")
        if nome == "banheiro":
            self.light_banheiro.set_texture_from_resource("images/banheiro_off.png")

    def sala_set_light(self, instance):
        set_html_f("sala")

    def cozinha_set_light(self, instance):
        set_html_f("cozinha")

    def quarto_set_light(self, instance):
        set_html_f("quarto")

    def banheiro_set_light(self, instance):
        set_html_f("banheiro")

    def mainloop(self, instance):
        if sala.state:
            self.light_on("sala")
        elif not sala.state:
            self.light_off("sala")
        if cozinha.state:
            self.light_on("cozinha")
        elif not cozinha.state:
            self.light_off("cozinha")
        if quarto.state:
            self.light_on("quarto")
        elif not quarto.state:
            self.light_off("quarto")
        if banheiro.state:
            self.light_on("banheiro")
        elif not banheiro.state:
            self.light_off("banheiro")


    """
    # image widget
        
        return self.window
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

        

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.quarto.text = "Bem Vindo " 
    """

app = app_casa()
app.run()

