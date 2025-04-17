class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._state = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL


    def power(self):
        if self._state == True:
            self._state = False
        elif self._state == False:
            self._state = True

    def mute(self):
        if self._state == True:
            self._muted = not self._muted

    def channel_up(self):
        if self._state == True:
            self._channel += 1
            if self._channel > Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL


    def channel_down(self):
        if self._state == True:
            self._channel -= 1
            if self._channel < Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL



    def volume_up(self):
        if self._state == True:
            if self._muted == False:
                if self._volume < Television.MAX_VOLUME:
                    self._volume += 1

    def volume_down(self):
        if self._state == True:
            if self._muted == False:
                if self._volume > Television.MIN_VOLUME:
                    self._volume -= 1

    def __str__(self):
        power_button = 'True' if self._state == True else 'False'
        volume_button = 0 if self._muted == True else self._volume
        return f' Power = {power_button}, Channel = {self._channel}, Volume = {volume_button}'
