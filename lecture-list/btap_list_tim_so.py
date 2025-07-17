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
#tạo list mới không chứa số lớn nhất
max1 = max(numbers)
n = numbers.copy()
while max1 in n:
    n.remove(max1)
#tìm số lớn nhì
if n:
    max2 = max(n)
    print("Số lớn nhì là:", max2)
else:
    print("list toàn giống nhau")


#cau 3
# numbers = [20, 36, 10, -4, 5, 15, 36, -16, 36]
# print(numbers.count(max(numbers)))
#hiểu sai đề ròi để sửa lại
