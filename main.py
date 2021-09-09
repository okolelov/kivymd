from kivy.lang import Builder

from kivymd.app import MDApp


KV = '''
MDScreen:

    MDTextField:
        hint_text: "Введите номер"
        mode: "fill"
        fill_color: 0, 0, 24, .4
        pos_hint: {"top":1}
        

    MDRaisedButton:
        text: "Тест"
        size_hint: None, None
        size: 500, 100
        pos_hint: {"center_x": 0.93, "center_y": 0.05}

'''


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_color
        return Builder.load_string(KV)


MainApp().run()