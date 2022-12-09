from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from view import *


class Controller(QMainWindow, Ui_MainWindow):
    #Initialize class variables 
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #Set the intial values of object variables
        self.__status = False
        self.__muted = False
        self.__volume = Controller.MIN_VOLUME
        self.__channel = Controller.MIN_CHANNEL

        #Connect GUI buttons to their functions
        self.power_button.clicked.connect(lambda: self.power())
        self.volume_up_button.clicked.connect(lambda: self.volume_up())
        self.volume_down_button.clicked.connect(lambda: self.volume_down())
        self.channel_up_button.clicked.connect(lambda: self.channel_up())
        self.channel_down_button.clicked.connect(lambda: self.channel_down())
        self.mute_button.clicked.connect(lambda: self.mute())
        
        #Set the Volume display to the initial volume
        self.volume_level.insert(str(self.__volume))

        #Set up the screen display
        self.__screen = QPixmap('Images\\blank_screen.png')
        self.tv_screen.setPixmap(self.__screen)
        self.tv_screen.setScaledContents(True)
        
        
    def power(self):
        '''
        Turns the TV on and off. Sets the TV screen to a black screen if off and to a news channel if on
        '''
        if self.__status == False:
            self.__status = True
            self.screen_change()
        elif self.__status == True:
            self.__status = False
            self.screen_change()
            
    def mute(self):
        '''
        Changes the value of the muted variable. Updates the volume display to 0 if muted and to the current volume if unmuted
        '''
        if self.__muted == False:
            self.__muted = True
            self.volume_level.clear()
            self.volume_level.insert("0")
            
        elif self.__muted == True:
            self.__muted = False
            self.volume_level.clear()
            self.volume_level.insert(str(self.__volume))
            
    def channel_up(self):
        '''
        Only works if the TV is on:
        Incremets the channel or loops back to the first channel if at the max channel value. 
        Then it calls the screen_change function to update the screen display in the GUI.
        '''
        if self.__status == True:
            if self.__channel == Controller.MAX_CHANNEL:
                self.__channel = Controller.MIN_CHANNEL
            else:
                self.__channel += 1
            self.screen_change()
        
    def channel_down(self):
        '''
        Only works if the TV is on:
        Decrements the channel or loops back to the last channel if at the min channel value. 
        Then it calls the screen_change function to update the screen display in the GUI.
        '''
        if self.__status == True:
            if self.__channel == Controller.MIN_CHANNEL:
                self.__channel = Controller.MAX_CHANNEL
            else:
                self.__channel -= 1
            self.screen_change()
                
    def volume_up(self):
        '''
        Only works if the TV is on, not at max volume, and unmuted:
        Increments the volume and updates the volume display in the GUI.
        '''
        if self.__status == True:
            if self.__volume == Controller.MAX_VOLUME:
                pass
            else:
                if self.__muted == True:
                    pass
                else:  
                    self.__volume += 1  
                    self.volume_level.clear()
                    self.volume_level.insert(str(self.__volume))
                
    def volume_down(self):
        '''
        Only works if the TV is on, not at min volume, and unmuted:
        Decrements the volume and updates the volume display in the GUI.
        '''
        if self.__status == True:
            if self.__volume == Controller.MIN_VOLUME:
                pass
            else:
                if self.__muted == True:
                    pass
                else:   
                    self.__volume -= 1 
                    self.volume_level.clear()
                    self.volume_level.insert(str(self.__volume))

    def screen_change(self):
        '''
        Updates the screen display in the GUI according to the channel and status variables.
        '''
        if self.__status == False:
            self.__screen = QPixmap('Images\\blank_screen.png')
        else:
            if self.__channel == 0:
                self.__screen = QPixmap('Images\\3-news.jpg')
            elif self.__channel == 1:
                self.__screen = QPixmap('Images\ketv-logo.png')
            elif self.__channel == 2:
                self.__screen = QPixmap('Images\\6-news.png')
            elif self.__channel == 3:
                self.__screen = QPixmap('Images\\fox-42.jpg')
        self.tv_screen.setPixmap(self.__screen)
      