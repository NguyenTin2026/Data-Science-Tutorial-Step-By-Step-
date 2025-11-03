# Remove Blank Rows
 # - We can use  .dropna)_ to remove blank depending on axis=0(rows), axis=1(columns)
import pandas as pd
health_data = pd.read_csv('data.csv', header=0, sep=',')
health_data.dropna(axis=0, inplace=True) # Chú thích: inplace=True => Xóa các ô lỗi theo hàng ; inplace=False => giữ nguyên các ô lỗi theo hàng
print(health_data)

# Data Types
 # - We can use the  info()  function to list the data types within our data set: 
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
print(health_data.info())

 # - We can use the astype() function to convert the data into float64.
import pandas as pd
health_data = pd.read_csv('data.csv', header=0, sep=',')
health_data['Hours_work'] = health_data['Hours_work'].astype(float)
health_data['Hours_sleep'] = health_data['Hours_sleep'].astype(float)
print(health_data.info())

# Analyze the data
 # - We can use the  describe()  function in Python to summarize data:
import pandas as pd
health_data = pd.read_csv('data.csv',header=0, sep=',')
pd.set_option('display.max_columns', None) # Có thể dùng thêm  pd.set_option('display.max_rows', None)
print(health_data.describe())
    # Count - Counts the number of observations
    # Mean - The average value
    # Std - Standard deviation (explained in the statistics chapter)
    # Max - The highest value
    # Min - The lowest value
    # 25%, 50% and 75% are percentiles (explained in the statistics chapter)
