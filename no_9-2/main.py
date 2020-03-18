from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty 
 
from kivy.config import Config
Config.set('graphics','width','300')
Config.set('graphics','height','200')
 
class TextWidget(Widget):
    text = StringProperty()    # プロパティの追加
 
    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''
 
    def buttonClicked1(self):   # ボタンをクリック時
        self.text = '左ボタンが押されました'
 
    def buttonClicked2(self):   # ボタンをクリック時
        self.text = '右ボタンが押されました'
 
class ButtonApp(App):
    def __init__(self, **kwargs):
        super(ButtonApp, self).__init__(**kwargs)
        self.title = 'greeting'
 
    def build(self):
        return TextWidget()
 
ButtonApp().run()