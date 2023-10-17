from Command.receiver.parent import ElectronicDevice
from Command.receiver.television import Television


class TVRemote:
    @staticmethod
    def get_device() -> Television:
        return Television()
