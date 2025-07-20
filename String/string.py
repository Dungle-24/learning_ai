
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
print(len(s))          
print(s.lower())   #hello python 
print(s.upper())   # HELLO PYTHON 
print(s.strip())     # Hello Python
print(s.replace("Python", "World"))  Hello World 

#kiểm tra chuỗi con
print("Hell" in s)     
print("Java" not in s) 
#tìm chuỗi con
print(s.find("Python")) 
print(s.find("Java"))    

# Duyệt chuỗi
for ch in s1:
    print(ch)

# tách, nối chuỗi
text = "red,green,blue"
colors = text.split(",")
print(colors)         
print(" - ".join(colors))  

# chuyển kiểu khác sang chuỗi
x = 123
print(str(x))

# ký tự thoát
s4 = "Hello\nWorld\t\"Python\"\\Example"
print("Ký tự thoát:", s4)

# Chuỗi bất biến
new_s1 = 'H' + s1[1:]
print("Chuỗi mới:", new_s1)  
