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
print(s.strip())        # "Hello Python"
s = "Hello Python  "
print(s.capitalize())
s = "  Hello Python  "
print(s.replace("Python", "World"))

# Kiểm tra chuỗi con
s = "  Hello Python  "
print("Hell" in s)
print("Java" not in s)

# Duyệt chuỗi
for ch in s1:
    print(ch)

# Tách chuỗi
text = "red,green,blue"
text1 = '''
The sun dipped below the horizon, painting the sky in fiery hues of orange and purple. A gentle breeze rustled through
the palm trees, carrying the faint scent of salt from the nearby ocean. On the beach, a few lingering figures watched 
as the last rays of light faded, marking the peaceful end of another day. It was a moment of quiet reflection, a serene 
pause before the stars began to pepper the darkening canvas above.
'''
colors = text.split(".")
print(colors)
print(" - ".join(colors))

# Chuyển kiểu khác sang chuỗi
x = 123
print(str(x))

# Tìm kiếm chuỗi con
s = "Hello Python  "
print(s.find("Python"))
print(s.find("Java"))

# Định dạng string
ten = 'dung'
string = "ho va ten: {}".format(ten)
print(string)
string = 'toi ten la {1}, toi {0} tuoi, toi dang di du lich o {2}'.format('dung', 20, 'dat lat')
print(string)

# Đếm ký tự trong string không phân biệt hoa thường
text = '''
The sun dipped below the horizon, painting the sky in fiery hues of orange and purple. A gentle breeze rustled through
the palm trees, carrying the faint scent of salt from the nearby ocean. On the beach, a few lingering figures watched 
as the last rays of light faded, marking the peaceful end of another day. It was a moment of quiet reflection, a serene 
pause before the stars began to pepper the darkening canvas above.
'''
def dem_ky_tu(string):
    dem = {}
    for key in string.lower():
        if key in dem.keys():
            dem[key] += 1
        else:
            dem[key] = 1
    print(dem)

dem_ky_tu(text)

# Phân tích thừa số nguyên tố
def get_string(n):
    if n != 1:
        goc = n
        result = []
        for i in range(2, n+1):
            while n % i == 0:
                n //= i
                result.append(str(i))
        print(goc, "=", " x ".join(result))
    else:
        print(n, "= 1")
get_string(100)

# Loại bỏ ký tự tại vị trí k
string = "Today is a beautiful day!"
def remove_char(string, k):
    print(string[:k-1] + string[k:])
remove_char(string, 5)

# Đếm nguyên âm
text = "A A A Today is a beautiful day"
def count_vowels(string):
    vowels = ['u', 'e', 'o', 'a', 'i']
    count = 0
    for i in string.lower():
        if i in vowels:
            count += 1
    print(count)
count_vowels(text)

# Anagram
def are_anagrams(str1, str2):
    c1 = str1.replace(' ','').lower()
    c2 = str2.replace(' ','').lower()
    if sorted(c1) == sorted(c2):
        print(str1, 'là anagrams của', str2)
    else:
        print(str1, 'không là anagrams của', str2)

s1 = 'New York Times'
s2 = 'monkeys write'
are_anagrams(s1, s2)

# Các ký tự chung - cách 1
def common_chars(str1, str2):
    s = set()
    str1 = str1.lower().replace(' ','')
    str2 = str2.lower().replace(' ', '')
    for i in str1:
        if i in str2:
            s.add(i)
    print(s)

s1 = 'New York Times'
s2 = 'monkeys vai ca chuong'
common_chars(s1, s2)

# Các ký tự chung - cách 2
def common_chars(str1, str2):
    str1 = set(str1.lower().replace(' ', ''))
    str2 = set(str2.lower().replace(' ', ''))
    print(str1.intersection(str2))

s1 = 'New York Times'
s2 = 'monkeys vai ca chuong'
common_chars(s1, s2)
