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

#phép hợp
set1 = {2, 4, 5, 6, 7}
set2 = {"vàng", "red", "green", 2, 4}
print(set1 | set2) #cách 1
print(set1.union(set2)) #cáh 2

#giao
set1 = {2, 4, 5, 6, 7}
set2 = {"vàng", "red", "green", 2, 4}
print(set1 & set2)
print(set1.intersection(set2))

#phép hiệu
set1 = {2, 4, 5, 6, 7}
set2 = {"vàng", "red", "green", 2, 4}
print(set1 - set2)
print(set2.difference(set1))

#phép hiệu đối xứng, bỏ những cái thuộc cả 2 tập
set1 = {2, 4, 5, 6, 7}
set2 = {"vàng", "red", "green", 2, 4}
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# bài tập list cho thêm
"""
    Viết hàm nhận 1 tham số đầu vào là 1 số tự nhiên n
    In ra kết quả là tích các thừa số nguyên tố của số đó
    Ví dụ, với n = 100
    Kết quả in ra màn hình là:
        100 = 2 x 2 x 5 x 5
"""

def get_string(n):
    if n!= 1:
        goc = n
        result = []
        for i in range(2,n+1):
            while n% i == 0:
                print(i)
                n/=i
                result.append(str(i))
        print(goc,"="," x ".join(result))
    else:
        print(n,"= 1")
get_string(100)





