def ListToBeMultipled(ListOfNum):
    result = 1
    for x in ListOfNum:
        result = result * x
    return result
list_num = [int(num) for num in input('').split()]
print(ListToBeMultipled(list_num))
