import time


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%y-%b-%d %H:%M:%S', time.localtime())

    def log(self, message, notifier):
        notifier().write(f'{self.prefix} {message}')