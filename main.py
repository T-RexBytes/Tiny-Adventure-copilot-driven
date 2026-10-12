print("You wake up in a quiet forest.")
print("Two paths are in front of you: a cave and a river.")

choice = input("Which path do you take? ").strip().lower()

if choice == "cave":
    print("You enter the cave and find a chest of treasure. You win!")
elif choice == "river":
    print("You follow the river and find a friendly village. You are safe!")
else:
    print("You stay in the forest and get lost. Game over!")