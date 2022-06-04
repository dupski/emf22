from tidal import *
from app import TextApp
import wifi

class MyApp(TextApp):
    
    SCR_WIDTH = 16
    
    BG = BLACK
    FG = GREEN

    def scrprint(self, text):
        remainder = text[self.SCR_WIDTH:]
        text = text[:self.SCR_WIDTH]
        self.window.println(text)
        if remainder:
            self.scrprint(remainder)

    def on_activate(self):
        super().on_activate()
        self.scrprint("EMF Schedule 1.1")

        self.scrprint(f"Currently-configured SSID is '{wifi.get_ssid()}'")
        # If not already connected...
        if not wifi.status():
            # ... connect to the default-configured AP...
            wifi.connect()
            # ... and synchronously wait for it to connect or time out...
            wifi.wait()
        if wifi.status():
            self.scrprint("Connected!")
        else:
            self.scrprint("Connection failed!")

def test_func():
    print('test 2')

# Set the entrypoint for the app launher
main = MyApp
