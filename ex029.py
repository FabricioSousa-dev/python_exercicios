v = int(input("What is the current speed of your vehicle? "))
m = (v - 80) * 7.00

if v > 80:
 print("Sorry your speed is too high!")
 print("Em {:.2f} R$".format(m))
else:
 print("follow your path!")
