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
 
    def buttonClicked(self):   # ボタンをクリック時
        self.text = 'ボタンが押されました'
 
class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'
 
    def build(self):
        return TextWidget()
 
TestApp().run()