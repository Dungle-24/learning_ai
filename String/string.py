
# khai báo chuỗi
s1 = "hello"
s2 = 'world'
s3 ="""
chuỗi nhiều dòng
hello
hi
"""
print(s1, s2, s3)

# truy cập từng ký tự
print(s1[0])
print(s1[-1])

# cắt chuỗi
s1 = "hello"
print(s1[1:4])
print(s1[:3])   
print(s1[2:])

# đảo
print(s1[::-1])

# thay thế chuỗi, vì string bất biến nên nếu muốn đổi thì cộng thêm string khác vào
string = 'ABCDEF'
new = 'PPP' + string[1:] #nối dùng +
print(new)
# nối
string = 'con' ' cò' ' bé bé'
print(string)

#1 số hàm xử li
s = "  Hello Python  "
print(len(s))           # 16
print(s.lower())        # "  hello python  "
print(s.upper())        # "  HELLO PYTHON  "
print(s.strip())        # "Hello Python"    #loại bỏ khoảng trắng dư thừa. lstrip là xóa bên trái, rstrip là xóa bên phải
s = "Hello Python  "
print(s.capitalize()) #viết hoa kí tự đầu, còn lại viết thường
s = "  Hello Python  "
print(s.replace("Python", "World"))  # "  Hello World  " thay thế

# Kiểm tra chuỗi con
s = "  Hello Python  "
print("Hell" in s)      # True
print("Java" not in s)

# Duyệt chuỗi
for ch in s1:
    print(ch)

# Tách chuỗi, nối chỉ ra muốn tách nối bằng cái gì
text = "red,green,blue"
text1 = '''
The sun dipped below the horizon, painting the sky in fiery hues of orange and purple. A gentle breeze rustled through
the palm trees, carrying the faint scent of salt from the nearby ocean. On the beach, a few lingering figures watched 
as the last rays of light faded, marking the peaceful end of another day. It was a moment of quiet reflection, a serene 
pause before the stars began to pepper the darkening canvas above.
'''
colors = text.split(".")
print(colors)           # ['red', 'green', 'blue']
print(" - ".join(colors))  # red - green - blue

# Chuyển kiểu khác sang chuỗi
x = 123
print(str(x))           # "123"

# Tìm kiếm chuỗi con
s = "Hello Python  "
print(s.find("Python"))  # 6
print(s.find("Java"))    # -1

#định dạng string
ten = 'dung'
string = "ho va ten: {}".format(ten)
print(string)
string = 'toi ten la {1}, toi {0} tuoi, toi dang di du lich o {2}'.format('dung', 20, 'dat lat')
print(string)


#đếm ký tự trong string không phân biệt hoa thường
text = '''
The sun dipped below the horizon, painting the sky in fiery hues of orange and purple. A gentle breeze rustled through
the palm trees, carrying the faint scent of salt from the nearby ocean. On the beach, a few lingering figures watched 
as the last rays of light faded, marking the peaceful end of another day. It was a moment of quiet reflection, a serene 
pause before the stars began to pepper the darkening canvas above.
'''
def dem_ky_tu (string):
    dem = {}
    for key in string.lower():
        if key in dem.keys():
            dem[key] += 1
        else:
            dem[key] = 1
    print(dem)
dem_ky_tu(text)


"""
    Viết hàm nhận 1 tham số đầu vào là 1 số tự nhiên n
    In ra kết quả là tích các thừa số nguyên tố của số đó
    Ví dụ, với n = 100
    Kết quả in ra màn hình là:
        100 = 2 x 2 x 5 x 5
"""

def get_string(n):
    if n!= 1:
        goc = n
        result = []
        for i in range(2,n+1):
            while n% i == 0:
                n//=i
                result.append(str(i))
        print(goc,"="," x ".join(result))
    else:
        print(n,"= 1")
get_string(100)

"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 chuỗi ký tự bất kỳ
    2. 1 số tự nhiên i bất kỳ
    Loại bỏ phần tử thứ k khỏi chuỗi và trả về chuỗi kết quả
"""

string = "Today is a beautiful day!"
def remove_char (string, k):
    print(string[:k-1] + string[k:])

remove_char(string,5)
