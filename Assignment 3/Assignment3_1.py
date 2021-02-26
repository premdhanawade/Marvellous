#Write a program which accept N numbers from user and store it into List. Return addition of all
#elements from that List.
#Input : Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output : 130



if __name__ == '__main__':
    x = int(input("Enter number of elements: "))
    list = []
    sum=0
    for i in range(0,x):
        el=int(input("Enter element: "))
        list.append(el)
        sum=sum+list[i]
    print("Sum of list is", sum)