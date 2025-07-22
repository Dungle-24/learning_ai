
# MỞ FILE
#đường dẫn tương đối: đường dẫn từ chỗ mình đang ở tới chỗ mình cần
relative_path = "./src/dataset.py"
# đường dẫn tuyệt đối: từ gốc đến nơi mình muốn
absolute_path = "C:\\Users\\home\\Downloads\\Group4.docx"
#f = open(file_path, mode)
#"r": đọc (mặc định)
#"w": Ghi (ghi đè nọi dung cũ néu có)
#"a": Ghi thêm (append)
#"r+": Đọc và ghi (ghi đè nọi dung cũ néu có)
# "x": Tạo file mới, lỗi nếu file đã tồn tại
f = open(absolute_path,"r")

print(f.read()) #đọc hết
print(f.readline()) #đọc theo dòng
