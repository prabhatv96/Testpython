a=10
try:
    if a>5:
        raise Exception("should not exceed 5")
except:
    print("OK")

x=10
try:
  print(x)
except:
  print("An exception occurred")
else:
    print("No error")
finally:
    print("All Okay")
    