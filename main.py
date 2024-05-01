import math
import decimal

authPass = ["Test"]
authLog = ["Max"]

ctx = decimal.getcontext()

print("[A] - Add to list")
print("[B] - Check list")
Opt = input("choice: ").upper()

if Opt == "A":
  with open("test.txt", "a") as f:
    list = input("Name: ")
    hour = int(input("Hours:"))
    Mins = int(input("Mins: "))
    if Mins >= 60:
      left = Mins / 60
      hour += int(left)  # Convert left to integer before adding to hour
      Mins = int(Mins %
                 60)  # Calculate remaining minutes after converting hours
    fhour = math.trunc(hour)
    HpM = str(fhour) + "h " + str(Mins) + "m "
    f.write(list + ': ' + HpM + ', ')
    f.close()
    print("---------------------------------")
    print("Confirmed, added to external file")
    print("---------------------------------")
  print(f)
if Opt == "B":
  LogC = input("Login: ")
  PassC = input("Password: ")
  if LogC == authLog and PassC == authPass:
    Look = input("Who would you like to look up?: ")
    with open("test.txt", "r") as f:
      content = f.readlines()  # Read lines as a list
      for line in content:
        if Look in line:  # Check each line for Look
          print(line.strip())  # Print the line without trailing newline