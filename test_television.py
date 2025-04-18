import pytest

import television
from television import Television

TV = television.Television()

class TestTelevision:
    def test_init(self):
        if str(TV) != 'Power = False, Channel = 0, Volume = 0':
            return 'failed at test_init'


    def test_power(self):
        TV.power()
        if str(TV) != 'Power = True, Channel = 0, Volume = 0':
            return 'failed at test_power'


    def test_mute(self):
        TV.power()
        if str(TV) != 'Power = True, Channel = 0, Volume = 0':
            return 'failed at test_mute'
        elif str(TV) != 'Power = True, Channel = 0, Volume = 1':
            return 'failed at test_unmute'

    def test_channel_up(self):
        TV.power()
        if TV()._channel == TV.MAX_CHANNEL:
            TV.channel_up()
        elif TV()._channel != TV.MIN_CHANNEL:
            return 'failed at test_channel_up'

    def test_channel_down(self):
        TV.power()
        if TV()._channel == TV.MIN_CHANNEL:
            TV.channel_down()
        elif TV()._channel != TV.MAX_CHANNEL:
            return 'failed at test_channel_down'


    def test_volume_up(self):
        TV.power()
        TV().volume_up()
        if TV()._volume != 1:
            return ('failed at test_volume_up')

    def test_volume_down(self):
        TV.power()
        TV.volume = TV.MAX_VOLUME
        TV().volume_down()
        if TV()._volume != TV.MAX_VOLUME -1:
            return 'failed at test_volume_down'
