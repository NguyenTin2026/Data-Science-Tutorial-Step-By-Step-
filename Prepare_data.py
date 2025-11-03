# Chuẩn bị dữ liệu sử dụng thư viện Pandas
 # Đọc dữ liệu vào: .read_csv('tên_file.csv', header=0, sep=',')
import pandas as pd
health_data = pd.read_csv('data.csv', header=0, sep=",")
print(health_data) # ==> Nó sẽ hiển thị vài dòng rồi tự độngc cắt bớt và hiển thị chỉ vài dòng cuối

# Hiển thị tất cả các hàng và cột trong file data.csv
pd.set_option('display.max_rows', None) # Không giới hạn số hàng
pd.set_option('display.max_columns',None) # không giới hạn số cột

print(health_data)

# Xem một phần dữ liệu
print(health_data.head(10)) # xem 10 dòng đầu
print(health_data.tail(10)) # xem 10 dòng cuối
 # ==> nếu dùng .head() ; .tail() => mặc định in ra 5 dòng đầu ; 5 dòng cuối 

# Ghi ra file CSV để xem toàn bộ (đã sửa hoặc chưa sửa)
health_data.to_csv('output-full-data.csv', index=False)
