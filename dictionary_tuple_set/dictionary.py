data = {} #khởi tạo dic rỗng

data = {"name":"dung", "age":"20", "Ronaldo":"siuuu"}

data = {"name": "Viet", "age": 32, "name": "Thang"}
print(data) # cái value được gắn với key cuối cùng sẽ được nhận

# Bất biến (immutable)
# Number
# Bool
# String
# Tuple
a = "today"
print(id(a))
print(a + "is Saturday")
print(id(a))

# Khả biến (mutable)
# List
# Dictionary
# Set
a = [1, 2, 3]
print(id(a))
a.append(5)
a.extend([10, 20])
a.extend([10, 20])
a.extend([10, 20])
print(id(a))

# truy cập vào dic
data = {"name":"dung", "age":"20", "Ronaldo":"siuuu"}
print(data['name'])
# print(data['Messi']) #lỗi
print(data.get('Messi')) #nếu key ko có thì in none

# thêm, sửa dic
data = {"name": "dung", "age": 20, "job": "AI engineer"}
data["gender"] = "male" #thêm
data["age"] = 21        #update
print(data)

#xóa với key tương ứng
data = {"name": "Dung", "age": 20, "job": "AI engineer"} #cách 1 dùng pop
removed_value = data.pop("age")
print(data)
print(removed_value) # 20

data = {"name": "Dung", "age": 20, "job": "AI engineer"} #cách 2 dùng del
del data["age"]
print(data)

#duyệt qua các key, value, item
data = {"name": "Dung", "age": 20, "job": "AI engineer"}
print(data.keys())
print(data.values())
print(data.items())
for keys in data.keys():
    print(keys)
for key, value in data.items():
    print(value, key)

"""
Cho một danh sách numbers = [4, 2, 4, 5, 2, 3, 4, 3].
Hãy đếm số lần xuất hiện của từng số và lưu kết quả vào một dictionary.
"""
numbers = [4, 2, 4, 5, 2, 3, 4, 3]
count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)



"""
Cho 2 danh sách:
names = ["An", "Bình", "Chi"]
scores = [8, 9, 10]
Hãy tạo một dictionary ghép tên và điểm tương ứng như sau:

{"An": 8, "Bình": 9, "Chi": 10}
"""

names = ["An", "Bình", "Chi"]
scores = [8, 9, 10]

student_scores = {}

for i in range(len(names)):
    student_scores[names[i]] = scores[i]

print(student_scores)



"""Viết chương trình yêu cầu người dùng nhập vào một chuỗi ký tự, 
sau đó đếm số lần xuất hiện của từng chữ cái và lưu vào một dictionary. 
In ra kết quả cuối cùng.
"""
chuoi = input("Nhập một chuỗi: ")
dem_ky_tu = {}

for ky_tu in chuoi:
    if ky_tu in dem_ky_tu:
        dem_ky_tu[ky_tu] += 1
    else:
        dem_ky_tu[ky_tu] = 1

print(dem_ky_tu)




