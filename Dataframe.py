import pandas as pd
d = {'col1': [1,2,3,4,7], 'col2':[4,5,6,9,8], 'col3':[11,14,16,15,10]}
df = pd.DataFrame(data=d)

count_column = df.shape[0] # Chú thích: 0 là số hàng, 1 là số cột
print('Number of columns: ')
print(df)
print(count_column)

# Tìm giá trị lớn nhất 
Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print(Average_pulse_max)

# Tìm giá trị nhỏ nhất
Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print(Average_pulse_min)

# Tìm giá trị trung bình
import numpy as np
Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
Average_calorie_burnage = np.mean(Calorie_burnage)
print(Average_calorie_burnage)

