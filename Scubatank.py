class ScubaTank:
    def __init__(self, label, bar):
        self.label=label
        self._bar=bar
    def get_bar(self):
        return self._bar
    def set_bar(self,bar):
        if 0<=bar<=300:
            self._bar=bar
        else:
            print("Invalid pressure")
    def fill(self,amount):
        if amount>0:
            self._bar+=amount
        else:
            print("Invalid amount")
    def release(self,amount):
        if amount<=0:
            print("Invalid amount")
        elif amount>self._bar:
            print("Not enough air")
        else:
            self._bar-=amount
    def __str__(self):
        return f"Tank{self.label}: {self._bar} bar"
