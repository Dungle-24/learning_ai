# truy cập phần tử trong list
data = ["mèo", "chó", "dê", "chuột", "khỉ"]
print(data[2])
print(data[-2])

# truy cập p.tử trong list lồng nhau (nested list)
data = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(data[2][2])
print(data[2][2][0])
print(data [1])

# cắt list
data = [2, 4, 8, 16, 32, 64, 128, 256, 512]

print(data)         # [2, 4, 8, 16, 32, 64, 128, 256, 512]
print(data[0:3])
print(data[4:7])    # [32, 64, 128]
print(data[-6:-2])  # [16, 32, 64, 128]
print(data[:3])     # [2, 4, 8]
print(data[4:])     # [32, 64, 128, 256, 512]
print(data[:])      # [2, 4, 8, 16, 32, 64, 128, 256, 512]
print(data[-50:4])  # [2, 4, 8, 16]
print(data[3:100])  # [16, 32, 64, 128, 256, 512]
print(data[2::-2])  # [8, 32, 128]
print(data[::2])    # [2, 8, 32, 128, 512]
print(data[::-1])   # [512, 256, 128, 64, 32, 16, 8, 4, 2] #thường dùng để đảo list

# thêm phần tử vào list dùng hàm insert
dataset = [2, 4, 5, 7]
dataset.insert(2, 99) # đây là inplace function, không cần trả về, trả về trực tiếp list
print(dataset)

dataset.append(9999)   #thêm 1 phần từ vào cuối list dùng append
print(dataset)

dataset.extend([77, 88, 99])  #thêm các phần từ vào cuối list dùng extend
print(dataset)

# xóa phần tử khỏi list
dataset = [2, 4, 5, 7, 9, 223, 11, 35, 23, 93]
remove = dataset.pop(2) # cách 1 dùng pop
print(dataset)
print(remove)
del dataset[1] # cách 2
print(dataset)
del dataset[2:5]
print(dataset)

# xóa theo giá trị đầu tiên
dataset = [2, 4, 5, 7, 9, 223, 11, 35, 23, 11, 93]
dataset.remove(11)
print(dataset)

# tìm vị trí của phần tử ĐẦU TIÊN trong list khi biết giá trị
dataset = [2, 4, 5, 7, 9, 223, 11, 35, 23, 11, 93]
print(dataset.index(11))
print(sorted(dataset)) #sắp xếp thứ tự tăng dần
print(list(reversed(sorted(dataset))))

"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Đếm xem số k xuất hiện trong list bao nhiêu lần
"""

numbers = [20, 10, -4, 5, 10, 36, -16, 3, 5, 10, 16, -5, 5]
k = 10

def check (number, k):
    tong = 0
    for j in number:
        if j == k:
            tong +=1
    print(tong)
check(numbers,10)
#cách 2
def check(numbers, k):
    print(numbers.count(k))
check(numbers,10)
