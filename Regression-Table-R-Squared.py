# R - Bình phương
 # - R-Squared và điều chỉnh R-Squared mô tả mức độ phù hợp của mô hình hồi quy tuyến tính với các điểm dữ liệu:
'''
Giá trị của R-Squared luôn nằm trong khoảng từ 0 đến 1 (0% đến 100%).

Giá trị R-Squared cao có nghĩa là nhiều điểm dữ liệu gần với đường hồi quy tuyến tính.
Giá trị R-Squared thấp có nghĩa là đường hồi quy tuyến tính không phù hợp với dữ liệu.
'''

# Ví dụ trực quan về giá trị R bình phương thấp (0,00)
'''
Mô hình hồi quy của chúng tôi cho thấy giá trị R-Squared bằng 0, điều này có nghĩa là đường hồi quy tuyến tính không phù hợp với dữ liệu.
Điều này có thể được hình dung khi chúng ta vẽ đồ thị hàm hồi quy tuyến tính thông qua các điểm dữ liệu của Average_Pulse và Calorie_Burnage.
'''

# Ví dụ trực quan về giá trị R bình phương cao (0,79)
 # - Tuy nhiên, nếu chúng ta vẽ đồ thị Duration và Calorie_Burnage , R-Squared sẽ tăng lên. Ở đây, chúng ta thấy các điểm dữ liệu gần với đường hồi quy tuyến tính:
 # - Sau đây là mã bằng Python:
 # Ví dụ:
  # Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv('data.csv', header=0, sep=',')
x = full_health_data['Duration']
y = full_health_data['Calorie_Burnage']
slope, intercept, r, p, std_err = stats.linregress(x,y)
def my_function(x):
    return slope * x + intercept
mymodel = list(map(my_function,x))
print(mymodel)
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.xlim(xmin=0, xmax=200)
plt.ylim(ymin=0, ymax=2000)
plt.xlabel('Duration')
plt.ylabel('Calorie_Burnage')
plt.title('Regression Table With R-Squared')
plt.show()
  # Two lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()


# Tóm tắt - Dự đoán lượng calo bị đốt cháy bằng Average_Pulse
'''
Làm thế nào chúng ta có thể tóm tắt hàm hồi quy tuyến tính với Average_Pulse là biến giải thích?

Hệ số 0,3296, nghĩa là Average_Pulse có tác động rất nhỏ đến Calorie_Burnage.
Giá trị P cao (0,824), nghĩa là chúng ta không thể kết luận mối quan hệ giữa Nhịp tim trung bình và Lượng calo đốt cháy.
Giá trị R-Squared bằng 0, nghĩa là đường hồi quy tuyến tính không phù hợp với dữ liệu.
'''
