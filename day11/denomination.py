'''
2000
500
200
100
50
20
10

3000 = 2000+2*500

7750 = 3*2000+3*500+1*200+1*+1*50
'''



denominations = [500,100, 50, 20, 10, 5, 1]


def calculate_notes(amount):
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
        return
    
    print(f"Withdrawing ${amount}:")
    for denom in denominations:  
        if amount >= denom: 
            count = amount // denom
            amount %= denom
            if count > 0:
                print(f"{count} x ${denom} note(s)")
    
    if amount > 0:
        print(f"Remaining: ${amount}")


try:
    amount = int(input("Enter the withdrawal amount: "))
    calculate_notes(amount)
except ValueError:
    print("Please enter a valid integer amount.")
