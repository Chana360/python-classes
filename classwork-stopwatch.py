import time

print("Welcome to Chana's Stopwatch")
todo = int(input("Enter 1 to start, 2 to reset, 3 to stop, 4 to quit: "))

class Stopwatch:
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.duration = None
        self.running = False


