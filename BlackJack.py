import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Example card values

def deal_card():
    card = random.choice(cards)
    return card

def result(user_score, pc_score):
    if user_score > 21:
        print(f"You got {user_score} points. Your opponent got {pc_score} points.")
        print("It's a bust! You lost.")
    elif pc_score > 21:
        print(f"You got {user_score} points. Your opponent got {pc_score} points.")
        print("Your opponent got a bust! You Win!")
    elif user_score == 21:
        print(f"You got {user_score} points. Your opponent got {pc_score} points.")
        print("Congratulations, you got a Blackjack! You Win!")
    elif pc_score == 21:
        print(f"You got {user_score} points. Your opponent got {pc_score} points.")
        print("You lost, your opponent got a Blackjack!")
    elif user_score > pc_score:
        print(f"You got {user_score} points. Your opponent got {pc_score} points.")
        print("You Win!")
    elif pc_score > user_score:
        print(f"You got {user_score} points. Your opponent got {pc_score} points.")
        print("You lost!")
    else:
        print(f"You got {user_score} points. Your opponent got {pc_score} points.")
        print("It's a tie!")


end_game = False
while not end_game:
    user_cards = [deal_card(), deal_card()]
    pc_cards = [deal_card(), deal_card()]

    # Calculate initial scores
    user_score = sum(user_cards)
    pc_score = sum(pc_cards)
    
    print(f"Your cards: {user_cards}")
    print(f"oponnent {pc_cards}")
    print(f"You opponent got {pc_cards[0]} in the first card.")
    print(f"You got {user_score} points.")

    if user_score == 21 or pc_score == 21:
        result(user_score, pc_score)
        break

    give_cards = True
    while give_cards:
        add_card_user = input("Would you like another card? Type 'Y' for yes, 'N' for no: ").lower()
        
        if add_card_user == 'n':
            give_cards = False
            print(f"Your new score is {user_score} points.")
            print(f"Your cards: {user_cards}")
            print(f"oponnent {pc_cards}")
            result(user_score, pc_score)
            end_game = True
            break

            # Computer's turn to draw cards until it reaches at least 17
        while pc_score < 17:
            pc_cards.append(deal_card())
            pc_score = sum(pc_cards)

            print(f"Computer's final cards: {pc_cards}")
            result(user_score, pc_score)
            end_game = True
            break
    
        if add_card_user == 'y':
            user_cards.append(deal_card())
            user_score = sum(user_cards)

            if user_score >= 21:
                print(f"Your new score is {user_score} points.")
                print(f"Your cards: {user_cards}")
                print(f"oponnent {pc_cards}")
                result(user_score, pc_score)
                end_game = True
                break

            print(f"Your new score is {user_score} points.")
            print(f"Your cards: {user_cards}")
            print(f"oponnent {pc_cards}")
        else:
            print("Invalid input, please type 'Y' or 'N'.")


    # while True:
    #     restart = input("Do you want to play again? Type 'Y' for yes, 'N' for no: ").lower()
    #     if restart == 'y':
    #         os.system('cls' if os.name == 'nt' else 'clear')
    #         start_game()
    #         break
    #     elif restart == 'n':
    #         print("Thanks for playing!")
    #         break
    #     else:
    #         print("Invalid input, please type 'Y' or 'N'.")