username = input()

if username.lower() == "testuser":
  print("Done Succesfully")
elif username.upper() == "TESTADMIN":
  print("Admin Succesfully")
else:
  print("Failed")
