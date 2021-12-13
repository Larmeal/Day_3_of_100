# ทำนายว่าคู่รักของแต่ละคน มีคามเข้ากันได้ขนาดไหน

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is her/his name? \n")

family = name1 + name2
count_family = family.lower()

score_name1 = count_family.count("t")
score_name2 = count_family.count("r")
score_name3 = count_family.count("u")
score_name4 = count_family.count("e")

score_name5 = count_family.count("l")
score_name6 = count_family.count("o")
score_name7 = count_family.count("v")
score_name8 = count_family.count("e")

true_1 = score_name1 + score_name2 + score_name3 + score_name4
love_1 = score_name5 + score_name6 + score_name7 + score_name8

result = str(true_1) + str(love_1)
final_result = int(result)

if final_result < 10 or final_result > 90:
    print(f"Your score is {final_result}, you go together like coke and mentos.")
elif final_result >= 40 and final_result <= 50:
    print(f"Your score is {final_result}, you are alright together.")
else:
    print(f"Your score is {final_result}, General family.")

