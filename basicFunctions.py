def main():
  print("Hello World")

def name(insertedName=None):
  if insertedName==None: return False
  print("Hello {0} ".format(insertedName))

main()
name("NameHere")
