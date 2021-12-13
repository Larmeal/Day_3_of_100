# แยกแยะว่าเลขใดเป็นเลขคู่ หรือเลขคี่ 

number = int(input("Which number do you want to check? "))
result = int(number % 2)

if result == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")