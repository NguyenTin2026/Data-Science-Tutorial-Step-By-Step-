# Trường hợp: Sử dụng Thời lượng + Nhịp tim trung bình để Dự đoán Lượng calo bị đốt cháy
 # - Tạo bảng hồi quy tuyến tính với Average_Pulse và Duration làm biến giải thích.
 # Ví dụ:
import pandas as pd
import statsmodels.formula.api as smf
full_health_data = pd.read_csv('data.csv', header=0, sep=',')
model = smf.ols('Calorie_Burnage ~ Average_Pulse + Duration', data=full_health_data) # Giải thích: dấu ~ nghĩa là dấu bằng(=)
'''
Giải thích: ols là Ordinary Least Squares(phương pháp bình phương tối thiểu)
👉Nghĩa là ta muốn tìm đường thẳng tốt nhất: Calorie_Burnage = a + b * Average_Pulse
trong đó:
a: hằng số (intercept)
b: hệ số góc (slope)
'''
results = model.fit()
print(results.summary())
'''
In ra bảng thống kê kết quả hồi quy tuyến tính, gồm:
 coef: hệ số của từng biến.
 std err: sai số chuẩn.
 t, P>|t|: giá trị kiểm định thống kê.
 R-squared: độ phù hợp của mô hình (giá trị càng gần 1 càng tốt).
 F-statistic, Prob(F-statistic): độ tin cậy chung của mô hình.
 Intercept: hệ số chặn 𝑎.
 Average_Pulse: hệ số góc b.
'''

'''
Giải thích ví dụ:
Nhập thư viện statsmodels.formula.api dưới dạng smf. Statsmodels là một thư viện thống kê trong Python.
Sử dụng bộ dữ liệu full_health_data.
Tạo mô hình dựa trên phương pháp Bình phương tối thiểu thông thường với smf.ols(). Lưu ý rằng biến giải thích phải được viết trước trong dấu ngoặc đơn. Sử dụng tập dữ liệu full_health_data.
Bằng cách gọi .fit(), bạn sẽ nhận được biến results. Biến này chứa rất nhiều thông tin về mô hình hồi quy.
Gọi summary() để lấy bảng kết quả hồi quy tuyến tính.
'''

'''
+) Hàm hồi quy tuyến tính có thể được viết lại theo phương pháp toán học như sau:
Calorie_Burnage = Average_Pulse * 3.1695 + Duration * 5.8424 - 334.5194

+) Làm tròn đến hai chữ số thập phân:
Calorie_Burnage = Average_Pulse * 3.17 + Duration * 5.84 - 334.52
'''

# Định nghĩa hàm hồi quy tuyến tính trong Python
'''
Xác định hàm hồi quy tuyến tính trong Python để thực hiện dự đoán.

Calorie_Burnage là gì nếu:
Nhịp tim trung bình là 110 và thời gian tập luyện là 60 phút?
Nhịp tim trung bình là 140 và thời gian tập luyện là 45 phút?
Nhịp tim trung bình là 175 và thời gian tập luyện là 20 phút?
'''
 # Ví dụ:
def Predict_Calorie_Burnage(Average_Pulse, Duration):
    return(Average_Pulse * 3.165 + Duration * 5.8424 - 334.5194)

print(Predict_Calorie_Burnage(110, 60))
print(Predict_Calorie_Burnage(140, 45))
print(Predict_Calorie_Burnage(175, 20))
'''
Câu trả lời:
 Nhịp tim trung bình là 110 và thời lượng luyện tập là 60 phút = 364 Calo
 Nhịp tim trung bình là 140 và thời lượng luyện tập là 45 phút = 371 Calo
 Nhịp tim trung bình là 175 và thời lượng luyện tập là 20 phút = 336 Calo
'''

# Truy cập các hệ số
'''
Hãy xem các hệ số:
Calorie_Burnage tăng lên 3,17 nếu Average_Pulse tăng thêm một.
Calorie_Burnage tăng 5,84 nếu Duration tăng thêm một.
'''

# Truy cập Giá trị P
'''
Hãy xem giá trị P cho từng hệ số.
Giá trị P là 0,00 đối với Average_Pulse, Duration và Intercept.
Giá trị P có ý nghĩa thống kê đối với tất cả các biến vì nó nhỏ hơn 0,05.
Vì vậy, ở đây chúng ta có thể kết luận rằng Average_Pulse và Duration có mối quan hệ với Calorie_Burnage.

'''
# R-Squared đã điều chỉnh
'''
Sẽ có vấn đề với R bình phương nếu chúng ta có nhiều hơn một biến giải thích.
R bình phương gần như luôn tăng nếu chúng ta thêm nhiều biến hơn và sẽ không bao giờ giảm.
Điều này là do chúng ta đang thêm nhiều điểm dữ liệu hơn xung quanh hàm hồi quy tuyến tính.
Nếu chúng ta thêm các biến ngẫu nhiên không ảnh hưởng đến lượng Calorie_Burnage, chúng ta có nguy cơ kết luận sai rằng hàm hồi quy tuyến tính là phù hợp. R-bình phương hiệu chỉnh sẽ điều chỉnh cho vấn đề này.
Do đó, tốt hơn là nên xem xét giá trị R bình phương đã điều chỉnh nếu chúng ta có nhiều hơn một biến giải thích.
R bình phương đã điều chỉnh là 0,814.
Giá trị của R-Squared luôn nằm trong khoảng từ 0 đến 1 (0% đến 100%).
Giá trị R-Squared cao có nghĩa là nhiều điểm dữ liệu gần với đường hồi quy tuyến tính.
Giá trị R-Squared thấp có nghĩa là đường hồi quy tuyến tính không phù hợp với dữ liệu.
🗸 Kết luận: Mô hình phù hợp với điểm dữ liệu!✅

✅Xin chúc mừng! Bạn đã hoàn thành mô-đun cuối cùng của thư viện khoa học dữ liệu!🎉🎉🎉
'''