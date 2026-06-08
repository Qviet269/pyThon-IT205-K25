# n = int(input('n: '));

# for i in range(1, n + 1):
#     for j in range(n-i):
#         print(' ', end = "");
    
#     for j in range(2*i-1):
#         print('*', end = "");
#     print();



# n = int(input('Nhập số nguyên: '));

# prime = True;

# if n < 2:
#     print('không phải số nguyên tố');
# else:
#     for i in range(2, n):

#         if n % i == 0:
#             prime = False;
#             break;

#     if prime:
#         print('là số nguyên tố');
#     else:
#         print('không phải số nguyên tố');

# câu 2: tìm 30 số nguyên tố đầu tiên 


count = 0;
print ('------------------------------------------------------------------------------------------')
for i in range(2, 1000):
    prime = True;
    for j in range(2, i):
        if i % j == 0:
            prime = False;
    
    if prime:
        count +=1;
        print(i, end = " ");
    
    if count == 30:
        break
    
print("\n------------------------------------------------------------------------------------------");
    