class client:
  def __init__(self, arg1):
    self.arg1 = arg1

  def outputArg(self):
    print(self.arg1)

x = client("User")
x.outputArg()
