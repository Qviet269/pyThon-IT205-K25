import random # thư viện tạo số ngẫu nhiên

name_patient = input('Nhập tên bệnh nhân: ');
sex = input('Nhập giới tính: ');
year_birth = int(input('Nhập năm sinh: '));
phone = input('Nhập số điện thoại di động: ');
email = input('Nhập email: ');
symptom = input('Nhập triệu chứng ban đầu: ');
expense = float(input('Nhập chi phí khám: '));

ran_dom = random.randint(100,999) # 3 số ngẫu nhiên từ 100 tới 999

id_patient = f"BN{year_birth}{ran_dom}";

print('\n---- Thẻ bênh nhân ----');
print(f'Mã BN      : {id_patient} \n');
print(f'Tên        : {name_patient} ({type(name_patient)})');
print(f'Giới tính  : {sex}');
print(f'Năm sinh   : {year_birth}');
print(f'Điện thoại : {phone}');
print(f'email      : {email}');
print(f'Triệu chứng: {symptom}');
print(f'Chi phí    : {expense}');