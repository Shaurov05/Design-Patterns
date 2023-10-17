from Command.receiver.television import Television
from command import Command


class TurnTVOffCommand(Command):
    def __init__(self, device: Television):
        self._device = device

    def execute(self):
        self._device.off()
