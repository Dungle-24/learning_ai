
# MỞ FILE
#đường dẫn tương đối: đường dẫn từ chỗ mình đang ở tới chỗ mình cần
relative_path = "./src/dataset.py"
# đường dẫn tuyệt đối: từ gốc đến nơi mình muốn
absolute_path = "C:\\Users\\home\\Downloads\\Assignment_4 (3)\\hoàng dung.txt"
#f = open(file_path, mode)

f = open(absolute_path,"r", encoding="utf-8")
a = open(absolute_path,"a")
a.write('siuuuu')

# print(f.read()) #đọc hết
# print(f.readline()) #đọc theo dòng
# print(f.readline())
# print(f.readline())
print(list(f))

w = open(absolute_path,"w", encoding="utf-8")
w.writelines(["today is a beautiful day\n", "aa\n", "bb\n"])


f.close() #đóng file
w.close()
a.close()

absolute_path = "C:\\Users\\home\\Downloads\\Assignment_4 (3)\\hoàng dung.txt"
#đóng file = with
with open(absolute_path, 'r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())


