import random
import Day14_Data

data = Day14_Data.data
is_out = False
score = 0

while not is_out:

    ch1 = data[random.randint(0, len(data) - 1)]
    ch2 = data[random.randint(0, len(data) - 1)]

    while not is_out:
        print(f"Choice 1: {ch1['name']}. Is a {ch1['description']}. From {ch1['country']}.")

        print()

        print("V/S")

        print()

        print(f"Choice 2: {ch2['name']}. Is a {ch2['description']}. From {ch2['country']}.")

        print()

        user_choice = int(input("Who do you think has HIGHER POPULARITY (1/2): "))

        if ((user_choice == 1 and ch1['follower_count'] > ch2['follower_count']) or
                (user_choice == 2 and ch1['follower_count'] < ch2['follower_count'])):
            print("Congratulations! You guessed right.")
            print("Your Score + 1")
            print()
            score += 1
            ch3 = data[random.randint(0, len(data) - 1)]
            ch1, ch2 = ch2, ch3
            continue

        elif ((user_choice == 1 and ch1['follower_count'] < ch2['follower_count']) or
              (user_choice == 2 and ch1['follower_count'] > ch2['follower_count'])):
            print("Oops! That's a wrong guess!")
            print("Game Over!")
            is_out = True

        else:
            print("It's a tie!")
            print("Let's try again!")
            print()
            continue
    print()
    print("Your Total Score is: ", score)
    break
