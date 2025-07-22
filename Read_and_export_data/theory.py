# MO FILE
#f = open(file_path, mode)
#"r": đọc (mặc định)
#"w": Ghi (ghi đè nọi dung cũ néu có)
#"a": Ghi thêm (append)
#"r+": Đọc và ghi (ghi đè nọi dung cũ néu có)
# "x": Tạo file mới, lỗi nếu file đã tồn tại

# ĐỌC FILE
# Đọc hết
f = open("data.txt", "r")
content = f.read()
print("Nội dung file:", content)
f.close()

# Đọc thoe dòng
f = open("data.txt", "r")
lines = f.readlines()
print("Danh sách dòng:", lines)
f.close()

# Đọc từng dòng =vòng lặp
f = open("data.txt", "r")
for line in f:
    print("Dòng:", line.strip())  # strip() loại bỏ \n
f.close()

# GHI FILE
# Ghi đè nội dung mới
f = open("data.txt", "w")
f.write("Overwrite existing data.\n")
f.close()

# GHI NHIEU DONG
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
f = open("data.txt", "w")
f.writelines(lines)
f.close()

# GHI THEM
f = open("data.txt", "a")
f.write("Append this text.\n")
f.close()

# dùng 'with' để tự động đóng file
# Đọc file với 'with'
with open("data.txt", "r") as f:
    content = f.read()
    print("Đọc với with:", content)

# ghi file với 'with'
with open("data.txt", "w") as f:
    f.write("New content with 'with' statement.\n")
# file tự động đóng

#xủ lý ngoại lệ
try:
    f = open("non_existent.txt", "r")
    content = f.read()
    f.close()
except FileNotFoundError:
    print("Lỗi: File không tồn tại")
