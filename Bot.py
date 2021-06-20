from telegram.ext import Dispatcher, Updater, MessageHandler, Filters 
from Handlers import messageHandlers, commandHandlers

class Bot:
    
    __updater = None
    __dispatcher = None

    def __init__(self, token, offense = False, mute = False):
        self.token = token
        self.offense = offense
        self.mute = mute

    def start():
        self.__updater = Updater(token=self.token, use_context=True)
        self.__dispatcher = self.__updater.dispatcher

    def welcome(self):
        ...

    def goodbye(self):
        ...

    def offense(self):
        ...
        
    def job_appliance(self):
        ... 
