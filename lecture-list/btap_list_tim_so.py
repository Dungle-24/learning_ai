"""
    Cho 1 danh sách gồm các số
    Viết các chương trình để tìm ra:
    1. Số lớn nhất
    2. Số lớn thứ nhì
    3. k số lớn nhất

"""

numbers = [20, 10, -4, 5, 15, 36, -16]
#cau1
print(max(numbers))

#cau2
numbers = [20, 10, -4, 5, 15, 36, -16]
numbers.remove(max(numbers))
print(max(numbers))

#cau 3
numbers = [20, 36, 10, -4, 5, 15, 36, -16, 36]
print(numbers.count(max(numbers)))
