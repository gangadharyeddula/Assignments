class Demo:
  def add(self, a, b):
      return(a + b)
  def add(self, a, b, c=0):
      print(a + b + c)
obj = Demo()
obj.add(10,20)
obj.add(10, 20, 30)
