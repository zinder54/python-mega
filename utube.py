#num1 = float(input("enter first number: "))
#op = input("enter operator: ")
#num2 = float(input("enter second number: "))

#if op == "+":
 #   print(num1 + num2)
#elif op == "-":
 #   print(num1 - num2)
#elif op == "x":
 #   print(num1 * num2)
#elif op == "/":
 #   print(num1 / num2)
#else:
 #   print("please enter a number")
#-----------------------------------------
#i = 1
#while i <= 10:
 #   print(i)
  #  i += 1

#print("done with loop!")
#---------------------------------------------
secretword = "donkey"
guess = ""
guesscount = 0
guesslimit = 3
outofguesses = False

while guess != secretword and not(outofguesses):
    if guesscount < guesslimit:
        guess = input("guess the word!: ")
        guesscount += 1
    else:
        outofguesses = True

if outofguesses:
    print("out of guesses!!")
else:
    print("you win!!")
