import math
number1 = input("たす数1: ")
number2 = input("たす数2: ")
number1_num = int(number1)
number2_num = int(number2)
keta1_size = int (math.log10(number1_num) + 1)
keta2_size = int (math.log10(number2_num) + 1)
kotae = number1_num + number2_num
if keta1_size == 2 and keta2_size == 2:
    print("  " + str(number1_num))
    print("+ " + str(number2_num))
    print("------")
    print(" " + str(kotae))
elif keta1_size == 3 and keta2_size == 2:
    print("  " + str(number1_num))
    print("+  " + str(number2_num))
    print("------")
    print(" " + str(kotae))
elif keta1_size == 3 and keta2_size == 3:
    print("  " + str(number1_num))
    print("+ " + str(number2_num))
    print("------")
    print(" " + str(kotae))
elif keta1_size == 4 and keta2_size == 2:
    print(" " + str(number1_num))
    print("+  " + str(number2_num))
    print("------")
    print(" " + str(kotae))
elif keta1_size == 4 and keta2_size == 3:
    print("  " + str(number1_num))
    print("+  " + str(number2_num))
    print("-------")
    print(" " + str(kotae))
elif keta1_size == 4 and keta2_size == 4:
    print("  " + str(number1_num))
    print("+ " + str(number2_num))
    print("-------")
    print(" " + str(kotae))
