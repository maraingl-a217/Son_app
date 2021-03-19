from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config

#Window.size = (720, 1280)
Window.size = (850, 850)

Config.set('kivy', 'keyboard_mode', 'systemanddoc')

def get_schet(h, g):
    min = str(h*60)
    hours = str(min*365)
    days = float(h*g*60*365) #begin
    year_ch = float(h*g*60*365/ 60)
    year_day = float(h*g*60*365/ 60 / 24)
    year_year = float(h*g*60*365/ 60 / 24 / 365)
    year_days_str = str(days) #str
    year_ch_str = str(year_ch)
    year_day_str = str(year_day)
    year_year_str = str(year_year)


    return {'min': year_days_str, 'ch': year_ch_str, 'day': year_day_str, 'year': year_year_str}



class Container(GridLayout):

    def calculate(self):
        try:
            mass = int(self.text_input.text)
            let = int(self.text_input_let.text)
        except:
            mass = 0
            let = 60

        dan = get_schet(mass, let)

        self.min.text = dan.get('min')
        self.ch.text = dan.get('ch')
        self.day.text = dan.get('day')
        self.year.text = dan.get('year')





class MyApp(App):
    def build(self):

        return Container()



if __name__ == '__main__':
    MyApp().run()