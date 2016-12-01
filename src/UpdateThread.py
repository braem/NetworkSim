import threading
from time import sleep

class UpdateThread(threading.Thread):

    callback_function = None
    active = False
    # update_interval unit is seconds.
    update_interval = None

    def __init__(self, update_callback):
        threading.Thread.__init__(self)
        self.callback_function = update_callback
        # Set the target of this thread object to the function passed in.
        self._target = self.callback_function
        # Set daemon to true so this thread does not keep the process up if the application ends.
        self.daemon = True

    def setActive(self, is_active):
        self.active = is_active

    def setUpdateInterval(self, interval):
        self.update_interval = interval

    def run(self):
        while True:
            if self.active:
                self.callback_function()
                sleep(self.update_interval)
