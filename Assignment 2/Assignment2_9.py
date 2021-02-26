#Write a program which accept number from user and return number of digits in that number.
#Input : 5187934 Output : 7

#--------------------------------------------------------------------------------


  
def digit_count(n):
	print("Output : ",len(n))
print("Input :",end=" ")
x=int(input())
digit_count(str(x))