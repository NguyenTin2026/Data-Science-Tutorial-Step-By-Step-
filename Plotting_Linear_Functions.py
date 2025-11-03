# Plot the Existing Data in Python
'''
Now, we can first plot the values of Average_Pulse against Calorie_Burnage using the matplotlib library.
The  plot()  function is used to make a 2D hexagonal binning plot of points x,y:

''' 
#   # Three lines to make our compiler able to draw
# import sys
# import matplotlib
# matplotlib.use('Agg') # Giá trị AGG viết tắt của "Anti-Grain Geometry", được thiết kế trong môi trường ko có giao diện đồ họa => ko chạy được ra hình

  #Three lines to make our compiler able to draw:
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu và làm sạch tên cột (xóa khoảng trắng dư)
health_data = pd.read_csv('data-linear-functions.csv', header=0, sep=',')
health_data.columns = health_data.columns.str.strip()

# Vẽ biểu đồ Average_Pulse vs Calorie_Burnage
health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line')

# Giới hạn trục
plt.xlim(xmin=0)
plt.ylim(ymin=0)

# Tiêu đề và nhãn trục
plt.title('Average Pulse vs Calorie Burnage')
plt.xlabel('Average Pulse')
plt.ylabel('Calorie Burnage')

# Hiển thị biểu đồ trong VS Code
plt.show()

#   # Two lines to make our compiler able to draw(in ra nhị phân trong VScode):
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
'''
Example Explained
Import the pyplot module of the matplotlib library
Plot the data from Average_Pulse against Calorie_Burnage
kind='line' tells us which type of plot we want. Here, we want to have a straight line
plt.ylim() and plt.xlim() tells us what value we want the axis to start on. Here, we want the axis to begin from zero
plt.show() shows us the output

Why is The Line Not Fully Drawn Down to The y-axis?
==> The reason is that we do not have observations where Average_Pulse or Calorie_Burnage are equal to zero. 80 is the first observation of Average_Pulse and 240 is the first observation of Calorie_Burnage.
We can use the diagonal line to find the mathematical function to predict calorie burnage.
As it turns out:
If the average pulse is 80, the calorie burnage is 240
If the average pulse is 90, the calorie burnage is 260
If the average pulse is 100, the calorie burnage is 280
There is a pattern. If average pulse increases by 10, the calorie burnage increases by 20.

'''