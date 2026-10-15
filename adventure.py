"""A fictional campus adventure. Change the story with AI."""
name = input("Explorer name: ").strip() or "Explorer"
print(f"\nWelcome, {name}! The campus mascot has hidden a mystery prize.")
print("A clue points toward the library and the cafe.")
choice = input("Where do you go? Type library or cafe: ").strip().lower()

if choice == "library":
    print("You find a book labeled 'The Secret of Python.'")
    action = input("Do you open it or leave it? Type open or leave: ").strip().lower()
    if action == "open":
        print("A golden ticket falls out. You found the mystery prize!")
    elif action == "leave":
        print("You leave quietly. The mystery awaits another explorer.")
    else:
        print("That choice is not on the map. Run again and try open or leave.")
elif choice == "cafe":
    print("A talking muffin offers you a clue.")
    action = input("Do you listen or dance? Type listen or dance: ").strip().lower()
    if action == "listen":
        print("The muffin whispers: 'Check the library!' Your quest continues.")
    elif action == "dance":
        print("You win the muffin dance contest. Your prize is imaginary applause!")
    else:
        print("The muffin looks confused. Run again and try listen or dance.")
else:
    print("That location is not on the map. Run again and try library or cafe.")
