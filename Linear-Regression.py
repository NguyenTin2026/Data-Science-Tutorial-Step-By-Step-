# Hồi quy tuyến tính
 # - Thuật ngữ hồi quy được sử dụng khi bạn cố gắng tìm mối quan hệ giữa các biến.
 # - Trong Học máy và mô hình thống kê, mối quan hệ đó được sử dụng để dự đoán kết quả của các sự kiện.
'''
Trong mô-đun này, chúng ta sẽ giải quyết các câu hỏi sau:
Chúng ta có thể kết luận rằng Average_Pulse và Duration có liên quan đến Calorie_Burnage không?
Chúng ta có thể sử dụng Average_Pulse và Duration để dự đoán Calorie_Burnage không?
'''

# Phương pháp bình phương nhỏ nhất(Least Square Method)
 # - Hồi quy tuyến tính sử dụng phương pháp bình phương nhỏ nhất.
 # - Khái niệm này là vẽ một đường thẳng đi qua tất cả các điểm dữ liệu đã được biểu diễn. Đường thẳng này được định vị sao cho khoảng cách đến tất cả các điểm dữ liệu là nhỏ nhất.
 # - Khoảng cách này được gọi là "giá trị còn lại" hoặc "lỗi".
 # - Các đường đứt nét màu đỏ biểu thị khoảng cách từ các điểm dữ liệu đến hàm toán học được vẽ.

# Hồi quy tuyến tính sử dụng một biến giải thích
'''
Trong ví dụ này, chúng ta sẽ thử dự đoán Calorie_Burnage với Average_Pulse bằng cách sử dụng Hồi quy tuyến tính:
'''
 # Ví dụ:
  # Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv('data.csv', header=0, sep=',')
x = full_health_data['Average_Pulse']
y = full_health_data['Calorie_Burnage']
slope, intercept, r, p, std_err = stats.linregress(x,y)
def my_function(x):
    return slope * x + intercept
mymodel = list(map(my_function,x))
plt.scatter(x,y)
plt.plot(x, mymodel)
plt.xlim(xmin=0, xmax=200)
plt.ylim(ymin=0, ymax=2000)
plt.xlabel('Average_Pulse')
plt.ylabel('Calorie_Burnage')
plt.show()
  # Two lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
'''
Giải thích ví dụ:
Nhập các mô-đun bạn cần: Pandas, matplotlib và Scipy
Cô lập Average_Pulse là x. Cô lập Calorie_burnage là y
Lấy các giá trị khóa quan trọng với: slope, intercept, r, p, std_err = stats.linregress(x, y)
Tạo một hàm sử dụng giá trị độ dốc và giá trị chặn để trả về một giá trị mới. Giá trị mới này biểu thị vị trí trên trục y của giá trị x tương ứng.
Chạy từng giá trị của mảng x thông qua hàm. Điều này sẽ tạo ra một mảng mới với các giá trị mới cho trục y: mymodel = list(map(myfunc, x))
Vẽ biểu đồ phân tán ban đầu: plt.scatter(x, y)
Vẽ đường hồi quy tuyến tính: plt.plot(x, mymodel)
Xác định giá trị lớn nhất và nhỏ nhất của trục
Gắn nhãn trục: "Mạch_xung_trung_bình" và "Lượng_calo_đốt_sôi"
'''

