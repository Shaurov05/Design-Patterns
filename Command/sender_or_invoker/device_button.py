from Command.commands.command import Command


class DeviceButton:
    def __init__(self, command: Command):
        self.command = command

    def press(self):
        self.command.execute()
