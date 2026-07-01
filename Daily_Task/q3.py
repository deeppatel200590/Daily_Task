back_stack = []
forward_stack = []

while True:
    print("\n----- GPS Navigation -----")
    print("1. Visit New Place")
    print("2. Back")
    print("3. Forward")
    print("4. Show Current Location")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        place = input("Enter place name: ")

        back_stack.append(place)
        forward_stack.clear()

        print(f"Visited: {place}")

    elif choice == 2:
        if len(back_stack) <= 1:
            print("No previous location.")
        else:
            forward_stack.append(back_stack.pop())
            print(f"Current Location: {back_stack[-1]}")

    elif choice == 3:
        if len(forward_stack) == 0:
            print("No forward location.")
        else:
            back_stack.append(forward_stack.pop())
            print(f"Current Location: {back_stack[-1]}")

    elif choice == 4:
        if len(back_stack) == 0:
            print("No location visited yet.")
        else:
            print(f"Current Location: {back_stack[-1]}")
            print("History Stack :", back_stack)
            print("Forward Stack:", forward_stack)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")