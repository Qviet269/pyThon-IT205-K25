n = int(input('nhập n: '));

count = 0;

for i in range(1, n + 1):

    if n % i == 0:
        count += 1; #Nếu tính tống thì thay 1 = i
print('Số lượng ước của n là: ', count);