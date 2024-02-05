import wx


class MyApplicationApp(wx.App):
    """
    A class for my-application
    """
    def __init__(self) -> None:
        """
        Create the my-application app
        """
        super(MyApplicationApp, self).__init__()
        self.app_name = "My Application's Name"
