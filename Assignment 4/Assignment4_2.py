#Write a program which contains one lambda function which accepts two parameters and return
#its multiplication.
#Input : 4 3 Output : 12
#Input : 6 3 Output : 18


fp = lambda no1,no2 : no1*no2


def main():
    value1=int(input("enter 1 no"))
    value2 = int(input("enter 2nd no"))
    ret = fp(value1,value2)
    print(ret)

if __name__=='__main__':
    main();