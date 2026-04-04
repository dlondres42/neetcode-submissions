class Logger:

    def __init__(self):
        self.tracker = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.tracker:
            if timestamp >= self.tracker[message]:
                self.tracker[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.tracker[message] = timestamp + 10

        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
