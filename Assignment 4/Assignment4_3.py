from functools import reduce

def acceptList():
    list = []
    no=int(input("Enter the number of elements : "))
    for i in range(no):
        el=int(input("Enter the elements:"))
        list.append(el)
    return list

def filFun(n):
    return 70 <= n <= 90

def mapFun(n):
    return n+10

def redFun(n1,n2):
    return n1*n2

def main():
    lst=acceptList()
    print("Input list : ",lst)
    filtered=list(filter(filFun,lst))
    print("list after filter:",filtered)
    mapped=list(map(mapFun,filtered))
    print("list after Map: ",mapped)
    reduced=reduce(redFun,mapped)
    print("output of reduce: ",reduced)


if __name__ == '__main__':
    main()