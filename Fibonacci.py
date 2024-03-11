num = int(input("Please enter number >= 1 "))

n1, n2, sum = 0, 1, 0
if num <= 0:
    print("Please enter number greater than 0")
else:
    for i in range(0, num):     
        print(sum)# Print the Fibonacci numbers as you generate them
        n1 = n2
        n2 = sum
        sum = n1 + n2


#Yay finished code wowowwwowowowowowoowow 