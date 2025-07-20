
# khai báo chuỗi
s1 = "hello"
s2 = 'world'
s3 = """chuỗi nhiều dòng"""
print(s1, s2, s3)

# truy cập từng ký tự
print(s1[0])
print(s1[-1])

# cắt chuỗi
print(s1[1:4])
print(s1[:3])   
print(s1[2:])

# đảo
print(s1[::-1])

#1 số hàm xử li
s = "  Hello Python  "
print(len(s))           # 16
print(s.lower())        # "  hello python  "
print(s.upper())        # "  HELLO PYTHON  "
print(s.strip())        # "Hello Python"
print(s.replace("Python", "World"))  # "  Hello World  "

# Kiểm tra chuỗi con
print("Hell" in s)      # True
print("Java" not in s)  # True

# Duyệt chuỗi
for ch in s1:
    print(ch)

# Tách, nối chuỗi
text = "red,green,blue"
colors = text.split(",")
print(colors)           # ['red', 'green', 'blue']
print(" - ".join(colors))  # red - green - blue

# Chuyển kiểu khác sang chuỗi
x = 123
print(str(x))           # "123"
