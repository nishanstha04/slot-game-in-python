import random
MIN_BET=1
MAX_BET=100

def deposit():
    while True:
        amount=input("Enter amount to deposit: $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Invalid input. Please enter a number.")
    return amount




def get_bet():
    while True:
        bet = input("Enter your bet: $")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"Bet must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Invalid input. Please enter a number.")

    return bet


def spin(balance,bet):
    symbols = ['🍒', '🍋', '🍊', '🍉', '🔔', '⭐', "🍀"]  # Slot symbols
    for i in range(3):
        a=[random.choice(symbols) for _ in range(3)]
        for i in a:
            print(f"{i}\t"  ,end=' ')
        print()

    if a[0]==a[1]==a[2]:
        print("congratulations!!....Jackpot..You won")
        bet=bet*3
        print(f"You won ${bet}")
        print(f"your current balance is ${balance+bet}")
    elif a[0]==a[1] or a[1]==a[2] or a[0]==a[2]:
        print("Two pair matched")
        bet=bet*2
        print(f"You won ${bet}")
        print(f"your current balance is ${balance+bet}")
    else:
        print("You lost...Better luck next time!!")
        print(f"your current balance is ${balance-bet}")
        print("Thank you for playing!!")
                

def main():
        balance=deposit()
        bet=get_bet()
        spin(balance,bet)
        play_again=input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            main()
        else:
            print("Thank you for playing!")
            exit()
main()

