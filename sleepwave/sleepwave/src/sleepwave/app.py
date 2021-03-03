"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.colors import WHITE, rgb
import pygame


class HelloWorld(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, background_color= rgb(204, 204, 255) ))
        
        time_label = toga.Label(
        'Enter the latest possible time you want to wake up at & choose the size of the interval to be woken up within: ',
        style=Pack(padding=(0, 5))
        )
        self.time_inputMax = toga.TextInput(style=Pack(flex=1), placeholder = 'latest')
        self.time_inputInterval = toga.Selection(style=Pack(flex=1), items=['30', '40', '50', '60'])
        
        time_box = toga.Box(style=Pack(direction=ROW, padding=5))
        time_box.add(time_label)
        time_box.add(self.time_inputMax)
        time_box.add(self.time_inputInterval)
        
        buttonEnter = toga.Button(
            'enter',
            on_press=self.say_time,
            style=Pack(padding=5)
        )
        buttonSound = toga.Button(
            'sound output test',
            on_press=self.play_sound,
            style=Pack(padding=5)
        )
        
        buttonStopAlarm = toga.Button(
            'Alarm Off',
            on_press=self.stop_alarm,
            style=Pack(padding=5)
        )
        
        main_box.add(time_box)
        main_box.add(buttonEnter)
        main_box.add(buttonSound)
        main_box.add(buttonStopAlarm)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_time(self, widget):
        print("Latest wakeup time", self.time_inputMax.value, "time interval", self.time_inputInterval.value)
        
    def play_sound(self, widget):
        pygame.init()
        pygame.mixer.init()
        soundA= pygame.mixer.Sound("alarm-normal-sound.wav")
        soundA.play(loops=-1)
          
        
        
    def stop_alarm(self, widget):
        pygame.mixer.stop()

        
def main():
    return HelloWorld()
