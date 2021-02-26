#Write a program which accept one number and display below pattern.
#Input : 5
#Output : 
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#-------------------------------------------------------------------
def Number(n):
          for i in range(n):
                    j=1
                    while j<=n:
                              print(j,end=" ")
                              j+=1
                    print("\n")

x=(int(input("Enter the  number")))
Number(x)