"""
(1) PHÂN TÍCH LỖI:
- Trace code: Nhập dữ liệu đúng nhưng in ra bị lộn xộn.
- Không crash: Hàm `print()` tự động ép kiểu mọi dữ liệu thành text nên không báo lỗi.
- Nguyên nhân: Truyền nhầm tên biến vào lệnh print.

2. Giải thích vì sao chương trình không bị crash nhưng dữ liệu in ra sai:
   - Python là ngôn ngữ linh hoạt. Hàm `print()` 
   trong Python cho phép in nhiều giá trị cùng lúc (ngăn cách bằng dấu phẩy) bất kể kiểu dữ liệu của chúng là gì (chuỗi, số nguyên, v.v.).
   - Khi chạy lệnh `print('Triệu chứng:', age)`, 
   Python tự động chuyển số `25` thành chuỗi và in ra bên cạnh chữ 'Triệu chứng:' mà không báo lỗi xung đột kiểu dữ liệu (TypeError). 
   - Vì cấu trúc ngữ pháp (cú pháp code) hoàn toàn đúng chuẩn, 
   trình thông dịch không phát hiện ra lỗi, nên chương trình vẫn chạy từ đầu đến cuối một cách trơn tru.

3. Chỉ ra nguyên nhân gây lỗi logic:
   - Nguyên nhân chính là do sự nhầm lẫn trong việc truyền biến vào hàm `print()` ở phần xuất dữ liệu. 
   - Thay vì ghép nối nhãn 'Tên bệnh nhân:' với biến `name_patient`, 
   hệ thống cũ (legacy code) lại ghép nhầm với biến `symptom`. Sự sắp xếp chéo ngoe các biến ở 3 dòng lệnh print cuối cùng đã dẫn đến việc dữ liệu in ra không khớp với ý nghĩa thực tế.
"""

# phần sửa code chính xác
print('---Hệ Thống Tiếp Nhận Bệnh Nhân');
name_patient = input("Nhập họ tên bệnh nhân: ");
age = input('Mời bạn nhập tuổi: ');
symptom = input('Mời bạn nhập triệu chứng bệnh: ');

age = int(age);

print('-- Phiếu Khám Bệnh ---');
print ('Tên Bệnh Nhân: ', name_patient);
print('Tuổi: ', age);
print('Triệu Chứng: ', symptom);