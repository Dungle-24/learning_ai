# tuple tương tự list, nhưng là bất biến, đựng trong ()

data = 1, 2, 3, 4 #tuple packing
a, b, c, d = data #tuple unpacking
print(a, b, c, d)

#đổi vị trí
a = 5
b = 6
print(a, b)
a, b = b, a
print(a, b)

#list trong tuple
data = ("red", "green", ["light", "blue"], "yellow", "black")
data[2][0] = "dark"
print(data) # ('red', 'green', ['dark', 'blue'], 'yellow', 'black')

#nối
data = (2, 4, 6) + (1, 2, 3)
print(data)