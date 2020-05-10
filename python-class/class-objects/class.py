class Computer():

    def __init__(self,cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config of system is", self.cpu, self.ram)

comp1 = Computer('ryzen3', 8)
comp2 = Computer('ryzen5', 16)

comp1.config()
comp2.config()

######INIT

