from parent import ElectronicDevice


class Radio(ElectronicDevice):
    def __init__(self):
        self._volume = 0

    def on(self):
        print("Radio is on")

    def off(self):
        print("Radio is off")

    def volume_up(self):
        self._volume += 1
        print("Radio volume is at : ", self._volume)

    def volume_down(self):
        self._volume -= 1
        print("Radio volume is at : ", self._volume)
