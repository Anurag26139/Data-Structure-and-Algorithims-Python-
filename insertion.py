def insertionsort(list):
    for index in range(1,len(list)):
        first_element = list[index]
        pos = index
        while first_element<list[pos-1] and pos>0:
            list[pos]=list[pos-1]
            pos=pos-1
        list[pos] = first_element
list1=[10,40,19,13,7,6]
insertionsort(list1)
print(list1)
