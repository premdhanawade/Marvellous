#Write a program which accept N numbers from user and store it into List. Return Minimum
#number from that List.
#Input : Number of elements : 4
#Input Elements : 13 5 45 7
#Output : 5


if __name__ == '__main__':
    x = int(input("Enter number of elements: "))
    list = []



    for i in range(0,x):
        el=int(input("Enter element: "))
        list.append(el)
    min=min(list)



    print(min)

    print("Min of list is", min)