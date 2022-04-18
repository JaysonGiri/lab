class Television:
    """
    A class representing the functionality of a TV remote object
    """

    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a TV remote object
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        """"
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """
    def power(self) -> None:
        """
        Method to turn on/off TV (pressing power button on TV remote).
        :return: TV status
        """
        if self.__status is False:
            self.__status  = True
        else:
            self.__status = False
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """

    def channel_up(self) -> None:
        """
        Method to change channel up
        :return: New TV channel
        """
        if self.__status is True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            pass
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """

    def channel_down(self) -> None:
        """
        Method to change channel down
        :return: New TV channel
        """
        if self.__status is True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """

    def volume_up(self) -> None:
        """
        Method to turn volume up
        :return: Higher TV volume
        """
        if self.__status is True:
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
        else:
            pass
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
    def volume_down(self) -> None:
        """
        Method to turn volume down
        :return: Lower TV volume
        """
        if self.__status is True:
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        else:
            pass
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """

    def __str__(self) -> str:
        """
        Method to display TV status, channel, and volume
        :return: TV on/off status, New TV channel, Higher/Lower TV volume
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

