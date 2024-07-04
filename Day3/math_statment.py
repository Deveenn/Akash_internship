# The match-case statement is similar to switch statements

ch = int(input("Enter choice:"))
match ch:
    case 1:
      print("This is one")
    case 2:
     print("This is two")
    case 3:
       print("This is three")
    case _:
       print("Invalid value")