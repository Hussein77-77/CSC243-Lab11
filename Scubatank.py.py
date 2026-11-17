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
t = ScubaTank (" A " , 80)
print ( t ) 
t . fill (40)
print ( t . get_bar () )
t . set_bar (250)
print ( t )
t . set_bar (400)
print ( t . get_bar () )
t . release (0)
t . release (300)
t . release (50)
print ( t )