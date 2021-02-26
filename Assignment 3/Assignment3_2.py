#Write a program which accept N numbers from user and store it into List. Return Maximum
#number from that List.
#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56

if __name__ == '__main__':
    x = int(input("Enter number of elements: "))
    list = []
    max=0
    for i in range(0,x):
        el=int(input("Enter element: "))
        list.append(el)
        if list[i] > max:
            max=list[i]

    print("Max of list is", max)