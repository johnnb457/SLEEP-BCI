"""
CruX BCI Project W'21 Team 5
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.colors import WHITE, rgb


class SleepGUI(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
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
        
        main_box.add(time_box)
        main_box.add(buttonEnter)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
    def say_time(self, widget):
        print("Latest wakeup time", self.time_inputMax.value, "time interval", self.time_inputInterval)


def main():
    return SleepGUI()
