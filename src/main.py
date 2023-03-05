from kivy.app import App
from kivy.uix.label import Label
import scipy


class TestApp(App):
    def build(self):
        return Label(text=f"scipy: {scipy.__version__}")


TestApp().run()
