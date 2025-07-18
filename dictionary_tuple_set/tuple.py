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

#đếm số lần xuất hiện
data = ("red", "green", "blue", "red")
print(data.count("red"))   
print(data.count("black")) 


"""
Cho một danh sách gồm nhiều tuple, mỗi tuple chứa tên học sinh và điểm của học sinh đó.

Hãy viết chương trình để:

1. Tính điểm trung bình của mỗi học sinh.

2. Lưu kết quả vào một dictionary với tên học sinh là key, và điểm trung bình là value.

3. In ra danh sách các học sinh có điểm trung bình lớn hơn hoặc bằng 5.
input:
students_scores = [
    ("An", [4, 6, 5]),
    ("Bình", [9, 8, 10]),
    ("Cường", [2, 3, 4]),
    ("Dung", [7, 5, 6])
]
output:
{'An': 5.0, 'Bình': 9.0, 'Cường': 3.0, 'Dung': 6.0}
Học sinh có điểm >= 5:
An: 5.0
Bình: 9.0
Dung: 6.0
"""
students_scores = [
    ("An", [4, 6, 5]),
    ("Bình", [9, 8, 10]),
    ("Cường", [2, 3, 4]),
    ("Dung", [7, 5, 6])
]

diem_tb = {}

for ten, diem_list in students_scores:
    trung_binh = sum(diem_list) / len(diem_list)
    diem_tb[ten] = round(trung_binh, 1)

print(diem_tb)

print("Học sinh có điểm >= 5:")
for ten, tb in diem_tb.items():
    if tb >= 5:
        print(f"{ten}: {tb}")

