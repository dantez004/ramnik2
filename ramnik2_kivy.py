from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.core.window import Window

class Ramnik2(App):
    def build(self):
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        mainLayout = FloatLayout()

        #top text
        topLabel = Label(text='подскажу длину bmx рамы для твоего роста', halign='center', font_size=18)
        topLabel.pos_hint = {'center_x': 0.5, 'center_y': 0.9}
        mainLayout.add_widget(topLabel)

        #TextInput and Button
        self.entry = TextInput(multiline=False, size_hint=(0.5, 0.08), font_size=20)
        self.entry.bind(text=self.OnTextChange)
        self.entry.pos_hint = {'center_x':0.5, 'center_y': 0.7}
        mainLayout.add_widget(self.entry)

        #Bottom text
        self.upinfosize = Label(text='наиболее подходящее всем')
        self.rich = Label(text='20.5"  <ростовка>  20.75"')
        self.back = Label(text='12.75"   <перья>   12.8"')
        self.addinfo = Label(text='')

        self.upinfosize.pos_hint = {'center_x':0.5, 'center_y':0.5}
        self.rich.pos_hint = {'center_x':0.5, 'center_y':0.4}
        self.back.pos_hint = {'center_x':0.5, 'center_y':0.3}
        self.addinfo.pos_hint = {'center_x':0.5, 'center_y':0.2}
        mainLayout.add_widget(self.upinfosize)
        mainLayout.add_widget(self.rich)
        mainLayout.add_widget(self.back)
        mainLayout.add_widget(self.addinfo)

        return mainLayout

    def OnTextChange(self, instance, value):
        height = instance.text.strip()
        if 0 < len(height) < 4 and height.startswith('1'):
            try:
                height = int(height)
                self.upinfosize.text = 'управляемость     <параметр>   стабильность'
                if height in range(155, 160):  # логика относительно составленной таблицы рост-длина
                    self.rich.text = '20.25"    <ростовка>    20.4"'
                    self.back.text = '12.4"    < перья >     12.6"'
                elif height in range(160, 165):
                    self.rich.text = '20.3-20.4"<ростовка>    20.5"'
                    self.back.text = '12.44"    < перья >     12.7"'
                elif height in range(165, 170):
                    self.rich.text = '20.4"    <ростовка>    20.6"'
                    self.back.text = '12.5"    < перья >     12.75"'
                elif height in range(170, 175):
                    self.rich.text = '20.5"    <ростовка>    20.7"'
                    self.back.text = '12.7"    < перья >     12.75"'
                elif height in range(175, 180):
                    self.rich.text = '20.7"    <ростовка>20.8-21"'
                    self.back.text = '12.75"    < перья >     13.2"'
                elif height in range(180, 185):
                    self.rich.text = '20.7-20.8"<ростовка>      21"'
                    self.back.text = '12.8"    < перья >     13.2"'
                elif height in range(185, 190):
                    self.rich.text = '20.75"   <ростовка>    21.1"'
                    self.back.text = '13.2"    < перья >     13.7"'
                    self.addinfo.text = 'если Вы Ирек Ризаев, то вам перья 12.8'
                elif height in range(190, 192):
                    self.rich.text = '21.1"+   <ростовка>   21.2"+'
                    self.back.text = '13.6"    < перья >     13.75"'
                else:
                    self.addinfo.text = 'необходимо ввести целое число от 155 до 191'
            except ValueError:
                self.entry.text = ''
                self.addinfo.text = 'необходимо ввести целое число от 155 до 191'
        else:
            self.entry.text = ''
            self.upinfosize.text ='наиболее подходящее всем'
            self.rich.text ='20.5"  <ростовка>  20.75"'
            self.back.text ='12.75"   <перья>   12.8"'
            self.addinfo.text =''
if __name__ == '__main__':
    Ramnik2().run()