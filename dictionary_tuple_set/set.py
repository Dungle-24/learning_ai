#không trùng nhau
#không thứ tự
#không có chỉ số
#khả biến
#không chứa các phần tử khả biến


#khởi tạo set
data = {"red", "yellow", "green"}
d = {1, 3, 4, 6, "red", True}

data_1 = set("Wednesday")
print(data)

data_2 = set([1, 2, 3, 4, 5])
print(data) # {1, 2, 3, 4, 5}

#loại phần tử trùng
x = [3, 5, 6, 2, 3, 4, 3, 5, 3]
print(set(x))

#thêm phần tử
d = {1, 3, 4, 6, "red", True}
d.add(99)
print(d)

#thêm nhiều phần tử
d = {1, 3, 4, 6, "red", True}
d.update({2,3}, {5, 6, 7})
print(d)

#xóa phần tử
d = {1, 3, 4, 6, "red", True}
d.remove(4)
print(d)
#cách 2, nếu ko có phần tử đó vẫn ko lỗi
d = {1, 3, 4, 6, "red", True}
d.discard(2)
print(d)
#xóa ngẫu nhiên
d = {1, 3, 4, 6, "red", True}
d.pop()
print(d.pop())

#duyệt qua phần tử
d = {1, 3, 4, 6, "red", True}
for i in d:
    print(i)


