#Write a while loop that prints numbers from 1 to 5.
'''
i=1
while i<=6:
    print(i)
    i=i+1
'''
# Use a while loop to print all multiples of 3 from 3 to 30.
'''
i=1
while i<=31:
    if(i%3==0):
       print(i)
    i=i+1
'''
# Use a while loop to calculate the sum of all even numbers between 1 and 50.
'''
i=1
total=0

while i<=51:
    if (i%2 == 0):
        total= total+i
    i=i+1

print("Sum of even numbers from 1 to 50 is:",total)
'''
#Write a program that:
#Asks the user to enter a number (e.g. 1234)
#Reverses the number using a while loop
#Prints the reversed number (e.g. 4321)
'''
num=int(input("Enter a Number:"))
rev=-0
while num>0:
    last_digit= num %10
    rev= rev * 10 + last_digit
    num=num // 10

print("Reversd number is:",rev)
'''
#Count the Digits in a Number.
'''
num= int(input("Enter a number:"))
count=0
while num>0:
    num=num// 10
    count= count+1
print(count)
'''
# A number is called a palindrome if it reads the same backward as forward.
'''
inp=int(input("Enter a No.: "))
num = inp
rev=0
while num>0:
    last_digit= num%10
    rev= rev*10+ last_digit
    num=num//10
if(rev==inp):
    print("it is palindrome")
else:
    print("its not palindrome")
'''
