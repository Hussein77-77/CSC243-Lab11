class Point :
  def __init__ ( self , x , y ) :
    self . x = x
    self . y = y
  def __str__ ( self ) :
    return "(" + str ( self . x ) + " , " + str ( self . y ) + ") "
class Rectangle:
    def __init__(self,p,q):
        assert type(p)==Point and type(q)==Point and p.x<=q.x and p.y<=q.y, "Bad input!"
        self.p=p
        self.q=q
    def __str__(self):
        return (f"p=({self.p.x},{self.p.y}), q=({self.q.x},{self.q.y})")
    def get_width(self):
        return self.q.x-self.p.x
    def get_height(self):
        return self.q.y-self.p.y
    def get_parameter(self):
        return 2*(self.get_width()+self.get_height())
    def get_area(self):
        return (self.get_width()*self.get_height())
    def contains(self,pt):
        assert type(pt)==Point, "Bad input!"
        return (self.p.x<=pt.x<=self.q.x and
                self.p.y<=pt.y<=self.q.y)
