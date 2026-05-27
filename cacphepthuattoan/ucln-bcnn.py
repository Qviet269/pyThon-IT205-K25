# muốn tìm bội chung nhỏ nhất thì phải tìm ước chung lớn nhất

a = int(input('Nhập số a: '));
b = int(input('Nhập số b: '));

u_c_l_n = 1;

for i in range(1, min(a,b) + 1):

    if a % i == 0 and b % i == 0:
        u_c_l_n = i;

    # bội chung nhỏ nhất
    b_c_n_n = (a*b) / u_c_l_n;

print("UCLN =", u_c_l_n)
print("BCNN =", b_c_n_n)