# Bảng hồi quy
 # - Kết quả đầu ra từ hồi quy tuyến tính có thể được tóm tắt trong bảng hồi quy.
'''
Nội dung của bảng bao gồm:
Thông tin về mô hình
Hệ số của hàm hồi quy tuyến tính
Thống kê hồi quy
Thống kê các hệ số từ hàm hồi quy tuyến tính
Những thông tin khác mà chúng tôi sẽ không đề cập trong mô-đun này
'''

# Bảng hồi quy với Average_Pulse là biến giải thích
 # => Bây giờ bạn có thể bắt đầu hành trình phân tích đầu ra nâng cao!

# Tạo bảng hồi quy tuyến tính trong Python
 # - Sau đây là cách tạo bảng hồi quy tuyến tính trong Python:
import pandas as pd
import statsmodels.formula.api as smf
full_health_data = pd.read_csv('data.csv', header=0, sep=',')
model = smf.ols('Calorie_Burnage ~ Average_Pulse', data=full_health_data) 
'''
Giải thích: ols là Ordinary Least Squares(phương pháp bình phương tối thiểu)
👉Nghĩa là ta muốn tìm đường thẳng tốt nhất: Calorie_Burnage = a + b * Average_Pulse
trong đó:
a: hằng số (intercept)
b: hệ số góc (slope)
'''
results = model.fit() # Dòng này huấn luyện mô hình (fit model) trên dữ liệu. Tính toán giá trị a, b, sai số, R², p-value,...
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
Dep. Variable: is short for "Dependent Variable". Calorie_Burnage is here the dependent variable. The Dependent variable is here assumed to be explained by Average_Pulse.
Model: OLS is short for Ordinary Least Squares. This is a type of model that uses the Least Square method.
Date: and Time: shows the date and time the output was calculated in Python.
'''