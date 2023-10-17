from typing import List

from Command.commands.command import Command
from Command.receiver.parent import ElectronicDevice


class TurnItAllOff(Command):
    def __init__(self, devices: List[ElectronicDevice]):
        self.devices = devices

    def execute(self):
        for device in self.devices:
            device.off()
