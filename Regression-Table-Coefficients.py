# "Phần Hệ số" trong Bảng hồi quy
'''
- Coef là viết tắt của coefficient(hệ số). Đây là kết quả đầu ra của hàm hồi quy tuyến tính.
Hàm hồi quy tuyến tính có thể được viết lại theo phương pháp toán học như sau:
  Calorie_Burnage = 0.3296 * Average_Pulse + 346.8662
Những con số này có nghĩa là:
 Nếu Average_Pulse tăng thêm 1, Calorie_Burnage tăng thêm 0.3296(hoặc 0.3 làm tròn)
 Nếu Average_Pulse = 0, Calorie_Burnage bằng 346.8662(hoặc 346.9 làm tròn)
 Hãy nhớ rằng giá trị chặn(intercept) được sử dụng để điều chỉnh độ chính xác dự đoán của mô hình.
'''

# Định nghĩa hàm hồi quy tuyến tính trong Python
'''
Xác định hàm hồi quy tuyến tính trong Python để thực hiện dự đoán.
Calorie_Burnage là gì nếu Average_Pulse là: 120, 130, 150, 180?
'''
 # Ví dụ:
def Predict_Calorie_Burnage(Average_Pulse):
     return(0.3296 * Average_Pulse + 346.8662)
# Try some different Values: 120,130,150,180
print(Predict_Calorie_Burnage(120))
print(Predict_Calorie_Burnage(130))
print(Predict_Calorie_Burnage(150))
print(Predict_Calorie_Burnage(180))

