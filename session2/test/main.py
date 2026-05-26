# yêu cầu 1: cho người dùng nhập vào 2 số a, b kiểm tra số lớn nhất trong 2 số

#

# yêu cầu 2: Cho người dùng nhập vào 1 số nguyên dương
# dùng toán tử 3 ngôi kiểm tra> nếu như lớn hơn 20 thì in đúng
# ngược lại thì in sai

"""
element = int(input('Nhập vào một số nguyên: '));
if element < 0:
    print('Bắt buộc phải lớn hơn 0');
else:
 d = 'Đúng' if element > 20  else 'sai';
 print(d);
"""
# yêu cầu 3: cho người dùng nhập vào một số trong khoảng từ 2 đến 8
# tương ứng sẽ in ra màn hình với thứ tương ứng ().
# lưu ý: sẽ dùng match case

# user= int(input("Vui lòng nhập vào một số trong khoảng từ 2 đến 8: "));
    
# match user:
#         case 2:
#             print("Monday");
#         case 3:
#             print("Tuesday");
#         case 4:
#             print("Wednesday");
#         case 5:
#             print("Thursday");
#         case 6:
#             print("Friday");
#         case 7:
#             print("Saturday");
#         case 8:
#             print("Sunday");
#         case _:
#             print("Số bạn nhập không nằm trong khoảng từ 2 đến 8. Vui lòng thử lại!");

# vòng lặp for
# for i in range(1,6,2):
#     print(i, end = " ");

# # vòng lặp while
# i = 1
# while (i < 11):
#     print(i);
#     i += i;


# yêu cầu 3: in ra các số chẵn từ 1 đến 10 , bỏ qua số 4

# i = 1;
# while (i <= 10):
#     i += 1;
#     if (i == 4):
#         continue

#     if i % 2 == 0:
#         print(i);

# Yêu cầu 4: cho người dùng nhập vào một số,, nếu như số đó không phải số
#Nguyên dương, bắt nhập lại> và in số vừa nhập ra màn hình


# n = int(input('Nhập vào số nguyên: '));

# while (n < 0):
#     print('lỗi')
#     n = int(input("Vui lòng nhập lại một số nguyên dương > 0: "));
#     print(f" Số nguyên vừa nhập là: {n}");

# yêu cầu 5: cho hai số a b cho trước, tìm ước chung lớn nhất của hai số
# b1: tìm ra số nhỏ hơn trong 2 số
# b2: lặp từ 1 đến min
# b3: kiểm tra a và b đều chia hết cho số đó thì là ucln

a = int(input('Nhập số nguyên a:'));
b = int(input('Nhập số nguyên b: '));

if a < b:
    ucl = a;
else: uc = b;

while (uc > 0):
    
  if a % uc == 0 and b % uc == 0:
    break;

    uc-= 1;

print(f'Ước chung lớn nhất là {uc}');



# bội chung nhỏ nhất
a = 3; b = 6;

if a > b:
    max = a;
else: max = b;

while True:
    if(max % a == 0 and max % b == 0):
        print('B C N N là ', max);
        break;
    max += 1;

# cho biểu thức 2a + b = 10 , a và b là số nguyên dương
# tìm a và b thỏa mãn phương trình

a = int(input('nhập a: '));
b = int(input('nhập b: '));
