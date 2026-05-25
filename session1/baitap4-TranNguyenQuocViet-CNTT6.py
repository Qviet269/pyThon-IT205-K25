"""
(1) PHÂN TÍCH VÀ ĐỀ XUẤT GIẢI PHÁP:

- Input/Output: Hàm input() mặc định luôn hiểu dữ liệu nhập vào là chữ (chuỗi). 
Mình cần biến đổi nó thành số thực (float) cho nhiệt độ và số nguyên (int) cho nhịp tim để máy tính toán được.

- Đề xuất 2 cách ép kiểu:
  + Cách 1 (Ép trực tiếp luôn lúc nhập): VD: float(input()). 
    -> Ưu điểm: Code ngắn 1 dòng, chạy nhanh, đỡ tốn bộ nhớ tạo biến rác.
    -> Nhược điểm: Lỡ người dùng gõ sai chữ cái thì hơi khó dò lỗi.
  + Cách 2 (Nhập xong mới ép): VD: temp = input() rồi dòng dưới ghi num_temp = float(temp).
    -> Ưu điểm: Tách bạch, dễ dò lỗi từng bước.
    -> Nhược điểm: Dài dòng, tốn thêm bộ nhớ để lưu cái biến 'temp' dư thừa.

- phương án: Chọn Cách 1 (Ép trực tiếp). 
Trong môi trường y tế thao tác liên tục, cách này giúp phần mềm xử lý tức thì, 
tiết kiệm tối đa tài nguyên bộ nhớ của thiết bị mà code lại cực kỳ gọn gàng.
"""

id_patient = input('Nhập mã bênh nhân: ');
body_temperature = float(input('Nhập nhiệt độ cơ thể hiện tại: '));
heart_rate = int(input('Nhập nhịp tim hiện tại: '));

print('\n---Kết quả chuẩn hóa dữ liệu ---');
print('Mã bệnh nhân: ', id_patient);
print(f'Nhiệt độ cơ thể: {body_temperature} độ C');
print('=> Kiểu dữ liệu hệ thống ghi nhận: ', type(body_temperature));
print(f'Nhịp tim: {heart_rate} nhịp/phút');
print(f'=> Kiểu dữ liệu hệ thống ghi nhận: {type(heart_rate)}');
print('-----------------------------');
print('Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!');