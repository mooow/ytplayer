from ui import UI
import ytlib
class CLI(UI):
    def __init__(self):
        UI.__init__(self)
    
    def main(self):
        UI.main(self)
        while True:
            try:
                self.download(input("query? "))
            except KeyboardInterrupt:
                self.close()
            except IndexError:
                print("Not found")
