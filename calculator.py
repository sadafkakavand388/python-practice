score = float(input("Enter your score (between 0 and 20): "))

if score < 0 or score > 20:
    print("Invalid score!")
elif score < 10:
    print("You failed 😞")
elif score < 15:
    print("You passed 🙂")
else:
    print("Excellent! 🌟")
