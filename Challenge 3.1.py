def linearSearch(data, item):
    for i in range(len(data)):
    if data[i] == item:
    return i
return -1
data = [1, 9, 8, 7, 6, 3, 11, 4, 6, 9, 7, 2, 0, 19, -10]
item = int(input("Enter a number to search: "))
idx = linearSearch(data, item)
if idx >= 0:
    print("{} is found at index {}".format(item, idx))
else :
    print("{} was not found".format(item))