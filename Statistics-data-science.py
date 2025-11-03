# Statistics
 # - Thống kê là khoa học phân tích dữ liệu.
 # - Khi tạo ra 1 mô hình dự đoán => phải đánh giá độ tin cậy của dự đoán đó.
 # - Suy cho cùng, một dự đoán có giá trị nếu chúng ta không thể tin cậy vào nó.

# Các phép tính quan trọng trong một data set:
''' 
Count
Sum
Standard Deviation(std)
Percentile
Average
Etc...
(Đây là điểm khởi đầu quan trọng để làm quen với dữ liệu).
'''

# Sử dụng hàm  describe()  trong Python để tóm tắt dữ liệu:
import pandas as pd
full_health_data = pd.read_csv('data.csv', header=0, sep=',')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(full_health_data.describe())

# Thống kê phần trăm(Statistics Percentiles)
 # - Có 3 loại phần trăm: 25%, 50%, 75%
'''
Chúng ta hãy thử giải thích bằng một số ví dụ, sử dụng Average_Pulse.
 Phần trăm thứ 25 của Average_Pulse có nghĩa là 25% trong tổng số buổi tập có nhịp mạch trung bình là 100 nhịp mỗi phút hoặc thấp hơn. 
 Nếu đảo ngược câu lệnh, điều đó có nghĩa là 75% trong tổng số buổi tập có nhịp mạch trung bình là 100 nhịp mỗi phút hoặc cao hơn.
''' 
# TASK: Tìm phần trăm thứ 10% cho Max_Pulse
import pandas as pd
import numpy as np
full_health_data = pd.read_csv('data.csv', header=0, sep=',')
Max_Pulse = full_health_data['Max_Pulse']
percentile10 = np.percentile(Max_Pulse, 10)
print(percentile10)
'''Giải thích:
Max_Pulse = full_health_data["MaxPulse"] - Tách biến MaxPulse khỏi toàn bộ tập dữ liệu sức khỏe.
np.percentile() được sử dụng để xác định rằng chúng ta muốn phần trăm thứ 10% từ Max_Pulse.
Phần trăm thứ 10% của Max_Pulse là 119. Điều này có nghĩa là 10% trong số tất cả các buổi đào tạo có Max_Pulse là 119 hoặc thấp hơn. 
'''

# Độ lệch chuẩn(Standard Deviation)
 # - Độ lệch chuẩn là con số mô tả mức độ phân tán của các quan sát.
'''
Một hàm toán học sẽ gặp khó khăn trong việc dự đoán các giá trị chính xác nếu các quan sát "phân tán". Độ lệch chuẩn là thước đo mức độ không chắc chắn.
Độ lệch chuẩn thấp có nghĩa là hầu hết các con số đều gần với giá trị trung bình (trung bình cộng).
Độ lệch chuẩn cao có nghĩa là các giá trị được phân bổ trên một phạm vi rộng hơn.
'''
 # Mẹo: Độ lệch chuẩn thường được biểu thị bằng ký hiệu Sigma: σ

# Chúng ta có thể sử dụng hàm  std()  từ Numpy để tìm độ lệch chuẩn của một biến
 # Ví dụ:
import pandas as pd
import numpy as np
full_health_data = pd.read_csv('data.csv', header=0, sep=',')
std = np.std(full_health_data)
print(std)

# Hệ số biến thiên(Coefficient of Variation)
 # - Hệ số biến thiên được sử dụng để biết độ lệch chuẩn lớn đến mức nào.
 # Về mặt toán học, hệ số biến thiên được định nghĩa như sau:
 # Coefficient of Variation = Standard Deviation / Mean
 # Ví dụ:
import pandas as pd
import numpy as np
full_health_data = pd.read_csv('data.csv', header=0, sep=',')
coefficient_of_variation = np.std(full_health_data) / np.mean(full_health_data)
print(coefficient_of_variation)
'''
Chúng ta thấy rằng các biến Duration, Calorie_Burnage và Hours_Work có Độ lệch chuẩn cao so với Max_Pulse, Average_Pulse và Hours_Sleep.
'''

# Phương sai thống kê(Statistics Variance)
 # - Phương sai là một con số khác cho biết mức độ phân tán của các giá trị.
'''
Trên thực tế, nếu lấy căn bậc hai của phương sai, bạn sẽ có độ lệch chuẩn. Hoặc ngược lại, nếu nhân độ lệch chuẩn với chính nó, bạn sẽ có phương sai!
'''
 # Mẹo: Phương sai thường được biểu thị bằng ký hiệu Sigma Square: σ^2
'''
Bước 1 để tính phương sai: Tìm giá trị trung bình
Bước 2: Đối với mỗi giá trị - Tìm sự khác biệt so với giá trị trung bình
Bước 3: Đối với mỗi hiệu - Tìm giá trị bình phương
ưu ý: Chúng ta phải bình phương các giá trị để có được tổng mức chênh lệch.
Bước 4: Phương sai là số trung bình của các giá trị bình phương này
'''
# Sử dụng Python để tìm phương sai của health_data
 # - Sử dụng hàm  var()  từ Numpy để tìm phương sai(hãy nhớ rằng bây giờ chúng ta sử dụng tập dữ liệu đầu tiên với 10 quan sát)
import pandas as pd
import numpy as np
health_data = pd.read_csv('calculate-var-statistics.csv', header=0, sep=',')
var = np.var(health_data)
print(var)

# Sử dụng Python để tìm phương sai của toàn bộ tập dữ liệu
import pandas as pd
import numpy as np
full_health_data = pd.read_csv('data.csv', header=0, sep=',')
full_var = np.var(full_health_data)
print(full_var)

# Thống kê tương quan(Statistics Correlation)
 # - Hệ số tương quan đo lường mối quan hệ giữa hai biến.
 # - Hệ số tương quan không bao giờ được nhỏ hơn -1 hoặc lớn hơn 1.
'''
1 = có mối quan hệ tuyến tính hoàn hảo giữa các biến (như Average_Pulse so với Calorie_Burnage)
0 = không có mối quan hệ tuyến tính giữa các biến
-1 = có mối quan hệ tuyến tính âm hoàn hảo giữa các biến (ví dụ: Làm việc ít giờ hơn dẫn đến đốt cháy nhiều calo hơn trong một buổi tập luyện)
'''

# Ví dụ về mối quan hệ tuyến tính hoàn hảo (Hệ số tương quan = 1)
  # Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv('data-correlation-coefficient.csv', header=0, sep=',')
health_data.plot(x='Average_Pulse', y='Calorie_Burnage', title='Correlation Coefficient = 1', kind='scatter')
plt.show()

  # Two lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer) # buffer là bộ nhớ đệm
# sys.stdout.flush() # Hàm này ép Python in ra màn hình ngay lập tức thay vì đợi

# Ví dụ về mối quan hệ tuyến tính âm hoàn hảo (Hệ số tương quan = -1)
  # Three lines to make our compilers able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
negative_corr = {'Hours_Work_Before_Training':[10,9,8,7,6,5,4,3,2,1], 'Calorie_Burnage':[220,240,260,280,300,320,340,360,380,400]}
negative_corr = pd.DataFrame(data=negative_corr)
negative_corr.plot(x='Hours_Work_Before_Training', y='Calorie_Burnage', title='Correlation Coefficient = -1', kind='scatter')
plt.show()
  # Two lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer) # buffer là bộ nhớ đệm
# sys.stdout.flush() # Hàm này ép Python in ra màn hình ngay lập tức thay vì đợi

# Ví dụ về Không có mối quan hệ tuyến tính (Hệ số tương quan = 0)
  # Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
full_health_data = pd.read_csv('data.csv', header=0, sep=',')
full_health_data.plot(x='Duration', y='Max_Pulse', title='Correlation Coefficient = 0', kind='scatter')
plt.show()
  # Two lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer) # buffer là bộ nhớ đệm
# sys.stdout.flush() # Hàm này ép Python in ra màn hình ngay lập tức thay vì đợi
'''
Có thể thêm các tham số khác trong .plot : figsize, color, style, legend, grid, xlabel, ylabel, xlim, ylim, marker, alpha, linewidth, fontsize, rot, subplots, colormap, sharex, sharey
'''

# Ma trận tương quan thống kê(Statistics Correlation Matrix)
 # - Ma trận là một mảng số được sắp xếp theo hàng và cột.
 # - Ma trận tương quan đơn giản là một bảng hiển thị hệ số tương quan giữa các biến.
# Ma trận tương quan trong Python
 # - Sử dụng hàm  .corr()  trong Python để tạo ma trận tương quan. 
 # - Sử dụng hàm  round()  để làm tròn kết quả đầu ra thành hai chữ số thập phân.
 # Ví dụ:
import pandas as pd
full_health_data = pd.read_csv('data.csv', header=0, sep=',')
Corr_matrix = round(full_health_data.corr(),2)
print(Corr_matrix)

# Sử dụng Bản đồ nhiệt
 # - Chúng ta có thể sử dụng Bản đồ nhiệt để trực quan hóa mối tương quan giữa các biến:
'''
Hệ số tương quan càng gần 1 thì hình vuông càng xanh.
Hệ số tương quan càng gần -1 thì hình vuông càng có màu nâu.
'''
 # - Sử dụng Seaborn để tạo bản đồ nhiệt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
full_health_data = pd.read_csv("data.csv", header=0, sep=",")
correlation_full_health = full_health_data.corr()
axis_corr = sns.heatmap(correlation_full_health, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(50, 500, n=500), square=True)
plt.show()
'''
Giải thích ví dụ:
Nhập thư viện seaborn dưới dạng sns.
Sử dụng bộ dữ liệu full_health_data.
Sử dụng sns.heatmap() để cho Python biết rằng chúng ta muốn có bản đồ nhiệt để trực quan hóa ma trận tương quan.
Sử dụng ma trận tương quan. Xác định giá trị cực đại và cực tiểu của bản đồ nhiệt. Xác định 0 là tâm.
Xác định màu sắc bằng sns.diverging_palette. n=500 nghĩa là chúng ta muốn có 500 loại màu trong cùng một bảng màu.
square = True nghĩa là chúng ta muốn nhìn thấy hình vuông.
'''

# Thống kê tương quan so với nhân quả(Statistics Correlation vs Causality)
 # - Hệ số tương quan đo lường mối quan hệ số giữa hai biến.
 # - Hệ số tương quan cao (gần 1) không có nghĩa là chúng ta có thể chắc chắn kết luận được mối quan hệ thực sự giữa hai biến.
'''
Một ví dụ điển hình:
Vào mùa hè, doanh số bán kem ở bãi biển tăng lên
Đồng thời, tai nạn đuối nước cũng gia tăng
Liệu điều này có nghĩa là việc tăng doanh số bán kem là nguyên nhân trực tiếp dẫn đến gia tăng số vụ tai nạn đuối nước không?
'''

# Ví dụ về Bãi biển trong Python
 # - Ở đây, chúng tôi xây dựng một tập dữ liệu hư cấu để bạn thử:
  # Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
Drowning_Accident = [20,40,60,80,100,120,140,160,180,200]
Ice_Cream_Sale = [20,40,60,80,100,120,140,160,180,200]
Drowning = {'Drowning_Accident': [20,40,60,80,100,120,140,160,180,200], "Ice_Cream_Sale": [20,40,60,80,100,120,140,160,180,200]}
Drowning = pd.DataFrame(data = Drowning)
Drowning.plot(x='Ice_Cream_Sale', y='Drowning_Accident', kind='scatter')
plt.show()
correlation_beach = Drowning.corr()
print(correlation_beach)
  # Two lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
  
# Tương quan so với nhân quả - Ví dụ về bãi biển
'''
Nói cách khác: chúng ta có thể sử dụng doanh số bán kem để dự đoán tai nạn đuối nước không?

Câu trả lời là - Có lẽ là không.
Có khả năng là hai biến này vô tình có mối tương quan với nhau.
Vậy nguyên nhân nào gây ra chết đuối?

Người bơi không có kỹ năng
Sóng
Chuột rút
Rối loạn co giật
Thiếu sự giám sát
Lạm dụng rượu
vân vân.
'''
'''
Chúng ta hãy đảo ngược lập luận:
Hệ số tương quan thấp (gần bằng 0) có nghĩa là sự thay đổi của x không ảnh hưởng đến y không?
Quay lại câu hỏi:
Chúng ta có thể kết luận rằng Average_Pulse không ảnh hưởng đến Calorie_Burnage vì hệ số tương quan thấp không?
Câu trả lời là không.
'''
'''
Có một sự khác biệt quan trọng giữa tương quan và quan hệ nhân quả:
- Hệ số tương quan là một con số đo lường mức độ liên quan chặt chẽ của dữ liệu
- Nguyên nhân là kết luận rằng x gây ra y.
'''
 # Mẹo: Luôn suy nghĩ nghiêm túc về khái niệm nhân quả khi đưa ra dự đoán!