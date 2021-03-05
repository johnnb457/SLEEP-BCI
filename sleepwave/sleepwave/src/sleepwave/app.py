"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.colors import WHITE, rgb
import pygame
import datetime

class HelloWorld(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, background_color= rgb(204, 204, 255) )) # set the background color to purple
        
        time_label = toga.Label(
        'Enter the latest possible time you want to wake up at & choose the size of the interval to be woken up within: ',
        style=Pack(padding=(0, 5))
        )
        
        self.time_inputHour = toga.NumberInput(min_value=1, max_value=12, style=Pack(flex=1)) # number input for the hour of latest desired wakeup time
        self.time_inputMin = toga.NumberInput(min_value=00, max_value=59, style=Pack(flex=1)) # number input for the minute of latest desired wakeup time
        self.time_inputAmPm = toga.Selection(style=Pack(flex=1), items=['am', 'pm'])
        self.time_inputInterval = toga.Selection(style=Pack(flex=1), items=['30', '40', '50', '60']) # drop down menu of time interval range in minute
        self.check_time
        
        time_box = toga.Box(style=Pack(direction=ROW, padding=5)) # add the label and inputs to the same box
        time_box.add(time_label)
        time_box.add(self.time_inputHour)
        time_box.add(self.time_inputMin)
        time_box.add(self.time_inputAmPm)
        time_box.add(self.time_inputInterval)
        
        buttonEnter = toga.Button( # button to enter the user inputs related to time
            'enter',
            #on_press=self.say_time, # when enter is pressed, desired wakeup time printed in terminal
            on_press=self.check_time, # when enter is pressed, keep checking time until it equals input time and then sound alarm
            style=Pack(padding=5)
        )
        buttonSound = toga.Button( # button to test the alarm sound, will later be triggered by when actual time = optimal wakeup time
            'sound output test',
            on_press=self.play_sound,
            style=Pack(padding=5)
        )
        
        buttonStopAlarm = toga.Button( # button to stop the alarm sound
            'Alarm Off',
            on_press=self.stop_alarm,
            style=Pack(padding=5)
        )
        
        main_box.add(time_box) # add the time input and time label box to the main box
        main_box.add(buttonEnter) # add the 3 buttons to the main box
        main_box.add(buttonSound)
        main_box.add(buttonStopAlarm)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box # add the main box to the main window
        self.main_window.show() # show the main window

    def say_time(self, widget):
#        int(time_inputHour.value)
#        while time_inputHour.value < 1 or time_inputHour.value > 12:
#            warning_hour = toga.Label('Please enter a valid hour between 1 and 12.', style=Pack(padding=(0,5)))
        print("Latest wakeup time: ", self.time_inputHour.value, ":", self.time_inputMin.value, "Time interval: ", self.time_inputInterval.value)
            
    def play_sound(self, widget):
        pygame.init()
        pygame.mixer.init()
        soundA= pygame.mixer.Sound("alarm-normal-sound.wav") # set soundA to be the .wav file stored in sleepwave folder
        soundA.play(loops=-1) # play the alarm sound infinitely
        
    def check_time(self, widget):
        if self.time_inputAmPm.value == 'pm': # add 12 to wake up time inputs set to be pm since daytime is 24 hr time
            self.time_inputHour.value += 12
            print(self.time_inputAmPm.value)
            self.say_time
        while (1==1):
            if self.time_inputHour.value == datetime.datetime.now().hour and self.time_inputMin.value == datetime.datetime.now().minute:
                #self.play_sound(loops=-1)
                print(self.time_inputAmPm.value)
                break

    def stop_alarm(self, widget): # called by the stop button
        pygame.mixer.stop() # stops the alarm sound
        
def main():
    return HelloWorld()
