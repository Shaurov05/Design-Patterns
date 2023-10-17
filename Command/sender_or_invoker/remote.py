from Command.commands.turn_it_all_off import TurnItAllOff
from Command.commands.turn_tv_off import TurnTVOffCommand
from Command.commands.turn_tv_on import TurnTVOnCommand
from Command.commands.turn_volume_down import TurnTVVolumeDownCommand
from Command.commands.turn_volume_up import TurnTVVolumeUpCommand
from Command.receiver.radio import Radio
from Command.receiver.television import Television
from device_button import DeviceButton
from tv_remote import TVRemote


class PlayWithRemote:
    def play(self):
        device = TVRemote.get_device()

        #################################
        turn_on_command = TurnTVOnCommand(device)
        on_button_pressed = DeviceButton(turn_on_command)
        on_button_pressed.press()

        #################################
        turn_off_command = TurnTVOffCommand(device)
        off_button_pressed = DeviceButton(turn_off_command)
        off_button_pressed.press()

        #################################
        turn_vol_up_command = TurnTVVolumeUpCommand(device)
        vol_up_button_pressed = DeviceButton(turn_vol_up_command)
        vol_up_button_pressed.press()

        #################################
        turn_vol_down_command = TurnTVVolumeDownCommand(device)
        vol_down_button_pressed = DeviceButton(turn_vol_down_command)
        vol_down_button_pressed.press()

        #################################
        tv = Television()
        radio = Radio()
        all_devices = [tv, radio]
        turn_it_all_off = TurnItAllOff(all_devices)
        turn_it_all_off_button_pressed = DeviceButton(turn_it_all_off)
        turn_it_all_off_button_pressed.press()

