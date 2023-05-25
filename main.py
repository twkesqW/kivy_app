from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView


class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

#створити вікно

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        hl = BoxLayout()
        txt = Label(text='Вибери екран')
        vl.add_widget(ScrButton(self, direction='down', goal='first', text="1"))
        vl.add_widget(ScrButton(self, direction='left', goal='second', text="2"))
        vl.add_widget(ScrButton(self, direction='left', goal='third', text="3"))
        #добавити кнопку
        hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)


class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn = Button(text='Вибір: 1', size_hint=(.5, 1), pos_hint={'left': 0})
        btn_back = ScrButton(self, direction='up', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)




class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.countClick = 0
        vl = BoxLayout(orientation='vertical')
        self.txt = Label(text='Вибір: 2')
        vl.add_widget(self.txt)

        hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl1 = Label(text='Введіть пароль:', halign='right')
        self.input = TextInput()

        hl_0.add_widget(lbl1)
        hl_0.add_widget(self.input)
        vl.add_widget(hl_0)

        hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        btn_false = Button(text="OK!")
        btn_back = ScrButton(self, direction='right', goal='main', text="Назад")

        hl.add_widget(btn_false)
        hl.add_widget(btn_back)
        vl.add_widget(hl)
        self.add_widget(vl)
        btn_false.on_press = self.change_text

    def change_text(self):
        self.txt.text = self.input.text + '? Не спрацювало ...'


class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
        vl = BoxLayout(orientation='vertical')

        self.txt3 = Label(text = str(self.count))
        btnclk = Button(text = "Click",size_hint=(.5, 1), pos_hint={'left': 0})
        hl = BoxLayout(orientation = 'horizontal')

        hl.add_widget(self.txt3)
        hl.add_widget(btnclk)
        btnclk.on_press = self.clk_func

        vl.add_widget(hl)
        self.add_widget(vl)

    def clk_func(self):
        self.count += 1
        self.txt3.text = str(self.count)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name = 'third'))
        #добавляєте в менеджер
        return sm


app = MyApp()
app.run()