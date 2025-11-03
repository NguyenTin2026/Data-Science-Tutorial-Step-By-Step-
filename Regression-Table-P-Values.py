# Bảng hồi quy: Giá trị P
# "Thống kê của phần hệ số" trong bảng hồi quy
'''
Bây giờ, chúng ta muốn kiểm tra xem các hệ số từ hàm hồi quy tuyến tính có tác động đáng kể đến biến phụ thuộc (Calorie_Burnage) hay không.
Điều này có nghĩa là chúng ta muốn chứng minh rằng tồn tại mối quan hệ giữa Average_Pulse và Calorie_Burnage, bằng cách sử dụng các bài kiểm tra thống kê.

Có bốn thành phần giải thích số liệu thống kê của các hệ số:
std err là viết tắt của Standard Error
t là "giá trị t" của các hệ số
P>|t| được gọi là "Giá trị P"
 [0,025 0,975] biểu thị khoảng tin cậy của các hệ số
Chúng ta sẽ tập trung vào việc hiểu "Giá trị P" trong mô-đun này.
'''

# Giá trị P
'''
Giá trị P là một con số thống kê để kết luận xem có mối quan hệ nào giữa Average_Pulse và Calorie_Burnage hay không.
Chúng ta kiểm tra xem giá trị thực của hệ số có bằng 0 (không có mối quan hệ) hay không. Kiểm định thống kê cho trường hợp này được gọi là Kiểm định giả thuyết.
Giá trị P thấp (< 0,05) có nghĩa là hệ số có khả năng không bằng 0.
Giá trị P cao (> 0,05) có nghĩa là chúng ta không thể kết luận rằng biến giải thích ảnh hưởng đến biến phụ thuộc (ở đây: nếu Average_Pulse ảnh hưởng đến Calorie_Burnage).
Giá trị P cao cũng được gọi là giá trị P không đáng kể.

'''

# Kiểm định giả thuyết(Hypothesis Testing)
'''
Kiểm định giả thuyết là một thủ tục thống kê để kiểm tra xem kết quả của bạn có hợp lệ hay không.
Trong ví dụ của chúng tôi, chúng tôi đang kiểm tra xem hệ số thực của Average_Pulse và giá trị chặn có bằng 0 hay không.
Kiểm định giả thuyết có hai phát biểu: Giả thuyết không và giả thuyết đối.
Giả thuyết không có thể được viết ngắn gọn là H0
Giả thuyết thay thế có thể được viết ngắn gọn là HA
Viết theo dạng toán học:
 H0: Average_Pulse = 0
 HA: Average_Pulse ≠ 0
 H0: Intercept = 0
 HA: Intercept ≠ 0
 
 Dấu ≠ có nghĩa là "không bằng"
'''

# Kiểm định giả thuyết và giá trị P
'''
Giả thuyết không có thể bị bác bỏ hoặc không.
Nếu bác bỏ giả thuyết vô hiệu, chúng ta kết luận rằng tồn tại mối quan hệ giữa Nhịp tim trung bình và Lượng calo tiêu thụ. Giá trị P được sử dụng cho kết luận này.
Ngưỡng chung của giá trị P là 0,05.

Lưu ý: Giá trị P bằng 0,05 có nghĩa là 5% trường hợp, chúng ta sẽ bác bỏ giả thuyết vô hiệu một cách sai lầm. Điều này có nghĩa là chúng ta chấp nhận rằng 5% trường hợp, chúng ta có thể đã kết luận sai về một mối quan hệ.

Nếu giá trị P thấp hơn 0,05, chúng ta có thể bác bỏ giả thuyết không và kết luận rằng tồn tại mối quan hệ giữa các biến.
Tuy nhiên, giá trị P của Average_Pulse là 0,824. Vì vậy, chúng ta không thể kết luận mối quan hệ giữa Average_Pulse và Calorie_Burnage.
Điều này có nghĩa là có 82,4% khả năng hệ số thực của Average_Pulse bằng 0.
Giá trị cắt gốc được sử dụng để điều chỉnh khả năng dự đoán chính xác hơn của hàm hồi quy. Do đó, việc diễn giải giá trị P của giá trị cắt gốc là không phổ biến.
'''