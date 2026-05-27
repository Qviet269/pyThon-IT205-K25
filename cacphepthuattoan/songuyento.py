# số nguyên tố là chỉ chia được cho 1 và chính nó

n = int(input('Nhập số nguyên: '));

prime = True;

for i in range(2,n):

    if n % i == 0:
        prime = False;

    if prime == True:
        print('là số nguyên tố');
    else:
        print('Không phải số nguyên tố');