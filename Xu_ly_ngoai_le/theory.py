
#loại ngoại lệ phổ biến
#syntaxError lỗi cú pháp
# indexError: chỉ số ngoài phạm vi danh sách/tuple
# attributeError: truy cập thuộc tính ko tồn tại
# importError: import module ko tồn tại
#keyError: truy cập key ko tồn tại trong dictionary
# nameError: truy cập biến ko tồn tại
#typeError: thực hiện phép toán trên kiểu dữ liệu ko phù hợp
#fileNotFoundError: môở file ko tồn tại

#cấu trúc try-except
try:
    data = [0, 1, 2]
    print(data[3])  #  IndexError
except IndexError:
    print("Lỗi: Chỉ số ngoài phạm vi danh sách")

# xử lý nhiều ngoại lệ
try:
    data = {"a": 1, "b": 2}
    print(data["c"])  #  KeyError
except KeyError:
    print("Lỗi: Key không tồn tại trong dictionary")
except TypeError:
    print("Lỗi: Kiểu dữ liệu không phù hợp")

# sử dụng else
try:
    x = 5
    result = x / 2  # Ko gây lỗi
except ZeroDivisionError:
    print("Lỗi: Chia cho 0")
else:
    print(f"Kết quả: {result}")  # Chỉ chạy nếu ko lỗi

#sử dụng finally
try:
    f = open("non_existent.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("Lỗi: File không tồn tại")
finally:
    print("Khối finally luôn được thực thi")  # chạy bất kể có lỗi hay ko


# vidụ
try:
    #import module không tồn tại
    import viethandsome
except ImportError:
    print("Lỗi: Module không tồn tại")

try:
    class MyClass:
        def __init__(self):
            self.first = 1
    obj = MyClass()
    print(obj.second)  #AttributeError
except AttributeError:
    print("Lỗi: Thuộc tính không tồn tại")

try:
    print(5 + "5")  #TypeError
except TypeError:
    print("Lỗi: Phép toán không phù hợp với kiểu dữ liệu")

try:
    print(undefined_var)  # NameError
except NameError:
    print("Lỗi: Biến không được định nghĩa")

