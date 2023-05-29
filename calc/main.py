from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window


Window.size = (320, 510)
Window.clearcolor = (24/255, 32/255, 42/255, 1)
Window.always_on_top = True
Window.minimum_width=250
Window.minimum_height=350
Window.set_title('a')

class MainGrid(Widget):
    screen = ObjectProperty(None)

    def clearScreen(self):
        self.ids.screen.text=''

    def removeOne(self):
        self.ids.screen.text=self.ids.screen.text.replace('Error', '')[:-1]

    def enterSymbol(self, symbol):
        self.ids.screen.text = self.ids.screen.text.replace('Error', '') + symbol

    def changeSign(self):
        self.ids.screen.text = f'-({self.ids.screen.text})'
    def takeResult(self):
        try:
            print(Window.size)
            if self.ids.screen.text!='':
                self.ids.screen.text=str(eval(self.ids.\
                    screen.text.replace('÷', '/').replace('×', '*')))
        except Exception as ex:
            self.ids.screen.text='Error'

class calcApp(App):
    def build(self):
        return MainGrid()
    
    
if __name__=='__main__':
    calcApp().run()

    