attempt = 0
while True:
  attempt = attempt + 1
  answer = input("What's 2 + 2 (attempt: %s/3)? " % attempt)
  if answer == "4":
    print("Correct")
    break
  else:
    print("Incorrect")
  if attempt >= 3:
    print("You are stupid.. . Good bye.")
    break
 
