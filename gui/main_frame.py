from typing import Self

import wx
from logbook import Logger


my_log = Logger(__name__)


class MainFrame(wx.Frame):
    """
    Main frame class
    """
    __instance = None

    @classmethod
    def get_instance(cls) -> Self:
        """
        Get a sepcific instance of this class

        :return: TBC
        """
        return cls.__instance

    def __init__(self, *args, **kwargs) -> None:
        """
        Create a main frame

        :param args: not used
        :param kwargs: title, config
        """
        wx.Frame.__init__(self, *args, title=kwargs['title'])
        MainFrame.__instance = self

        self.title = kwargs['title']
        self.config = kwargs['config']
        self.SetIcon(wx.Icon(self.config['gui']['icon']))

        # do some interesting stuff here
        my_log.info("I'm doing something interesting")

        # display the frame
        self.Show()
