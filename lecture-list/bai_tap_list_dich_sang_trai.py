"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Trả về kết quả là 1 list, trong đó các phần tử bị dịch
    sang trái k đơn vị
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 2
    Output:
        array = [3, 4, 5, 1, 2]
"""

def sap_xep (array, k):
    so_ki_tu = len(array)
    new_array = [0] * so_ki_tu
    for i in range(so_ki_tu):
        new_array[i] = array[(i+k) % so_ki_tu]
    return new_array

data = [1, 2, 3, 4, 5, 6, 7]
sap_xep(data, 3)
print(sap_xep(data, 3))

