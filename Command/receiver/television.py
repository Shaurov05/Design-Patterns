from parent import ElectronicDevice


class Television(ElectronicDevice):
    def __init__(self):
        self._volume = 0

    def on(self):
        print("Tv is on")

    def off(self):
        print("Tv is off")

    def volume_up(self):
        self._volume += 1
        print("Tv volume is at : ", self._volume)

    def volume_down(self):
        self._volume -= 1
        print("Tv volume is at : ", self._volume)
