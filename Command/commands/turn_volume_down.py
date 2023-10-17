from Command.receiver.television import Television
from command import Command


class TurnTVVolumeDownCommand(Command):
    def __init__(self, device: Television):
        self._device = device

    def execute(self):
        self._device.volume_down()
