## IT'S A PIZAAA........ DELIVERIES SYSTEM.!!!!!!!!!!    

print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ").upper()

bill = 0

 # Validate size input and set base price
if size == "S":
     bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed wrong order.")
    exit()  # Stop execution if size is invalid

 # Add pepperoni cost if user wants it
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add extra cheese if user wants it
if extra_cheese == "Y":
    bill += 5

print(f"Your final bill is: ₹{bill}") 