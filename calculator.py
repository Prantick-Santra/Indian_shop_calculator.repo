# python program to add all numbers given to it, unless there is q
sum=0
print("If you want to quit the calculator, press q")
while True:
    input_user=input("Enter the price: ")
    if input_user=="q":
        print("Thanks, for using the calculator!")
        break
    else:
        sum=sum+int(input_user)
print(f"Your total price is {sum}")