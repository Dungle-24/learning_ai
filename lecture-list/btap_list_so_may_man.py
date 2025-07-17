"""
    Yêu cầu người dùng nhập vào 1 số nguyên dương
    Kiểm tra xem số đó có phải là 1 số may mắn hay không

    Số may mắn là số được định nghĩa theo quá trình sau: bắt đầu với số nguyên dương x
    và tính tổng bình phương y các chữ số của x, sau đó tiếp tục tính tổng bình phương
    các chữ số của y. Quá trình này lặp đi lặp lại cho đến khi thu được kết quả là 1
    thì dừng (tổng bình phương các chữ số của số 1 chính là 1) hoặc quá trình sẽ kéo dài vô tận.
    Số mà quá trình tính này kết thúc bằng 1 gọi là số may mắn.
    Số có quá trình tính kéo dài vô tận là số không may mắn hay còn gọi là số đen đủi
    Ví dụ: 19 là số may mắn vì
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1 (End)

    Some happy numbers are: 1, 7, 13, 19, 23, 28, 44, 49, 68, 79, 129, 133, 139, 167, 188,
    226, 236, 239, 338, 356, 367, 368, 379, 446, 469, 478, 556, 566, 888, 899
"""

n = input("nhap mot so nguyen duong: ")
def so_may_man (number):
    xuat_hien = []
    while number != 1 and number not in xuat_hien:
        tong = 0
        xuat_hien.append(number)
        for i in str(number):
            tong += (int(i)**2)
        number = tong

    else:
        if number == 1:
            print(n, "la so may man")
        else:
            print(n, "khong phai so may man")

so_may_man(int(n))






















# number = 23
# def is_happy_number(number):
#     seen = []
#     tong = 0
#     while number != 1 and tong not in seen:
#
#         for chu_so in str(number):
#             tong+=int(chu_so)**2
#             seen.append(tong)
#         print(tong)
#     if tong == 1:
#         print("la so may man")
#     else:
#         print("khong la so may man")
# print(is_happy_number(23))




# def is_happy_number(number):
#     seen = []
#     while number != 1 and number not in seen:
#         seen.append(number)
#         tong = 0
#         for chu_so in str(number):
#             tong += int(chu_so) ** 2
#         print(tong)  # In từng bước
#         number = tong  # cập nhật cho vòng lặp tiếp theo
#
#     if number == 1:
#         print("Là số may mắn")
#     else:
#         print("Không phải số may mắn")
#
# # Gọi hàm
# is_happy_number(23)
