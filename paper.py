
import random

# Initialize scores
robot_count = 0
human_count = 0

# Game choices
game_pos = ["stone", "paper", "scissor"]

while True:
    # Robot randomly selects a choice
    robot_choice = random.choice(game_pos)
    print(f"\nRobot choice: {robot_choice}")
    
    # Take input from the user
    user_choice = input(
        "Enter your choice (stone/paper/scissor) or type 'quit': "
    ).strip().lower()

    # Exit the game
    if user_choice == "quit":
        print("\nGame Over!")
        break

    # Validate user input
    if user_choice not in game_pos:
        print("Invalid choice! Please enter stone, paper, or scissor.")
        continue

    # Check for a draw
    if robot_choice == user_choice:
        print("Match Draw!")

    # Human wins
    elif (
        (user_choice == "stone" and robot_choice == "scissor")
        or (user_choice == "paper" and robot_choice == "stone")
        or (user_choice == "scissor" and robot_choice == "paper")
    ):
        human_count += 1
        print("Human Wins!")

    # Robot wins
    else:
        robot_count += 1
        print("Robot Wins!")

    # Display current score
    print(
        f"Score -> Human: {human_count} | Robot: {robot_count}"
    )

# Display final score
print("\n********* FINAL SCORE *********")
print(f"Human Score: {human_count}")
print(f"Robot Score: {robot_count}")

if human_count > robot_count:
    print("Congratulations! You won the game!")
elif robot_count > human_count:
    print("Robot won the game!")
else:
    print("The game ended in a tie!")

print("Thanks for playing!")
