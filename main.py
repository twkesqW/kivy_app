from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Shop(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.shopItems.add_widget(Button(text="1"))
        self.ids.shopItems.add_widget(Button(text="2"))
        self.ids.shopItems.add_widget(Button(text="3"))
        self.ids.shopItems.add_widget(Button(text="4"))
        self.ids.shopItems.add_widget(Button(text="5"))
        self.ids.shopItems.add_widget(Button(text="6"))
        self.ids.shopItems.add_widget(Button(text="7"))
        self.ids.shopItems.add_widget(Button(text="8"))

    def onMainWindow(self):
        #self.manager.transition.direction = self.direction
        self.manager.current = 'main'

class Box(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.countClick = 0

    def onClickBall(self):
        self.countClick += 1
        self.ids.countClick.text =  str(self.countClick)
        self.ids.ballImg.size_hint = (0.5, 0.5)

class ExampleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(Shop(name='shop'))
        sm.add_widget(Box(name='main'))

        return sm

if __name__ == '__main__':
    app = ExampleApp()
    app.run()