import random
import time

# Boot Screen Animation
def boot_screen():
    print("Booting up Power Run 1.1...\n")
    for i in range(3):
        time.sleep(1)
        print("Loading" + "." * (i + 1))
    print("\nSystem Ready!\n")
    print("Power Run 1.1 Managed by: IPGC SOFTWARE BRANCH")
    print("All rights reserved. Copyright IPGC NETWORK - https://sites.google.com/moe-dl.edu.my/innerpower/home\n")

# Zenith AI Chatbox with even smarter responses
def zenith_chatbox():
    print("\nZenith AI Chatbox activated!")
    print("Type 'exit' to leave the chat.\n")
    
    # Store user info
    user_name = ""
    favorite_game = ""
    favorite_food = ""
    interests = []

    # Example responses
    greetings = ['hello', 'hi', 'hey', 'greetings', 'yo']
    responses = {
        'how are you': "I'm doing great, thank you for asking! How about you?",
        'what is your name': "I am Zenith, your personal AI assistant.",
        'what is the meaning of life': "The meaning of life is to find your own purpose and make the most of your time.",
        'tell me a joke': "Why don't skeletons fight each other? They don't have the guts!",
        'bye': "Goodbye! Have a great day ahead!",
        'help': "I'm here to help you with various tasks! Ask me questions or try playing some mini-games.",
    }
    
    # Personalized greeting based on user's name
    def get_user_info():
        nonlocal user_name, favorite_game, favorite_food, interests
        if not user_name:
            user_name = input("Zenith: Hi! What's your name? ")
            print(f"Zenith: Nice to meet you, {user_name}!")
        if not favorite_game:
            favorite_game = input(f"Zenith: What's your favorite game, {user_name}? ")
            print(f"Zenith: Nice! {favorite_game} is awesome!")
        if not favorite_food:
            favorite_food = input(f"Zenith: What's your favorite food, {user_name}? ")
            print(f"Zenith: Yum! {favorite_food} sounds delicious!")
        if not interests:
            interests = input(f"Zenith: What are some of your hobbies or interests, {user_name}? ").split(", ")
            print(f"Zenith: That sounds amazing! I'll remember you're into {', '.join(interests)}.")

    get_user_info()
    
    while True:
        user_input = input(f"{user_name}: ").lower()

        # Greeting
        if any(greeting in user_input for greeting in greetings):
            print(f"Zenith: Hello, {user_name}! How can I assist you today?")
        
        # Handle personalized questions and commands
        elif user_input == 'how are you':
            print("Zenith: I'm doing great, thank you for asking! How about you?")
        
        elif user_input == 'what is your name':
            print("Zenith: I am Zenith, your personal AI assistant.")
        
        elif user_input == 'tell me a joke':
            print("Zenith: Why don't skeletons fight each other? They don't have the guts!")
        
        elif user_input == 'what is the meaning of life':
            print("Zenith: The meaning of life is to find your own purpose and make the most of your time.")
        
        elif user_input == 'bye':
            print(f"Zenith: Goodbye, {user_name}! Have a great day ahead!")
            break
        
        elif 'weather' in user_input:
            print("Zenith: I can't check the weather, but I can recommend a cozy indoor activity!")
        
        elif 'music' in user_input:
            print("Zenith: I can't play music, but I can suggest some music genres or artists if you'd like!")
        
        elif 'favorite game' in user_input:
            print(f"Zenith: I know your favorite game is {favorite_game}! That’s awesome.")
        
        elif 'favorite food' in user_input:
            print(f"Zenith: I know your favorite food is {favorite_food}! Sounds delicious.")
        
        # Handle complex or unexpected inputs with fun activities
        elif 'riddle' in user_input:
            riddle = random.choice([
                ("What has keys but can't open locks?", "A piano."),
                ("What has a head, a tail, but no body?", "A coin."),
                ("What comes once in a minute, twice in a moment, but never in a thousand years?", "The letter 'M'.")
            ])
            print(f"Zenith: Here's a riddle for you: {riddle[0]}")
            answer = input("Your answer: ").lower()
            if answer == riddle[1].lower():
                print("Zenith: Correct! You're good at this!")
            else:
                print(f"Zenith: Nice try! The correct answer was: {riddle[1]}")

        # Default response if unrecognized input
        else:
            print(f"Zenith: Hmm... I don't quite understand. Could you ask something else or type 'help' for assistance?")

# Number Guesser Game
def number_guesser():
    print("\nWelcome to Number Guesser!")
    print("Guess the number between 1 and 100.\n")
    number = random.randint(1, 100)
    attempts = 0
    guess = None
    
    while guess != number and attempts < 10:
        guess = int(input(f"Attempt {attempts + 1}/10: Your guess: "))
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} tries!")
            break

    if attempts >= 10 and guess != number:
        print(f"Sorry, you've used all your attempts. The correct number was {number}.")

# Rock-Paper-Scissors Game
def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print("\nWelcome to Rock-Paper-Scissors!")
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in options:
            print("Invalid choice, try again.")
            continue
        computer_choice = random.choice(options)
        print(f"Computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Main Menu
def main_menu():
    boot_screen()  # Call your boot screen here
    print("Welcome to Power Run 1.1\n")
    print("Choose an option:")
    print("1. Play Number Guesser")
    print("2. Play Rock-Paper-Scissors")
    print("3. Chat with Zenith AI")
    print("4. Visit Our Website")
    print("5. Exit Power Run\n")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            number_guesser()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            zenith_chatbox()
        elif choice == "4":
            print("\nVisit our website at: https://www.powerrun1.1.com\n")
        elif choice == "5":
            print("Exiting Power Run 1.1... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Start the program
if __name__ == "__main__":
    main_menu()
