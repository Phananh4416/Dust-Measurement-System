import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi

# Đọc file CSV vào DataFrame
df = pd.read_csv('BUI.csv')

# Đếm số lượng hàng trong cột 1
row_count = df.shape[0]

# Tính tổng các giá trị của cột 1
total_col1 = df.iloc[:, 0].sum()

# Biến đổi các giá trị của cột 2 ra loga tự nhiên
log_col2 = np.log(df.iloc[:, 1])

# Tính tổng các giá trị đã biến đổi của cột 2
total_log_col2 = log_col2.sum()

# Tính bình phương các giá trị của cột 1 rồi tính tổng
sum_squared_col1 = (df.iloc[:, 0] ** 2).sum()

# Tính tích các giá trị cột 1 nhân với loga của cột 2 rồi tính tổng
product_col1_log_col2 = (df.iloc[:, 0] * log_col2).sum()

# Khởi tạo ba ma trận 2x2
matrix1 = np.array([
    [row_count, total_col1],
    [total_col1, sum_squared_col1]
])

matrix2 = np.array([
    [total_log_col2, total_col1],
    [product_col1_log_col2, sum_squared_col1]
])

matrix3 = np.array([
    [row_count, total_log_col2],
    [total_col1, product_col1_log_col2]
])

# Tính định thức của mỗi ma trận
det_matrix1 = np.linalg.det(matrix1)
det_matrix2 = np.linalg.det(matrix2)
det_matrix3 = np.linalg.det(matrix3)

# Tính B và A
A = np.exp(det_matrix2 / det_matrix1)
B = det_matrix3 / det_matrix1

# Tính độ lệch chuẩn của cột 2
std_dev_col2 = df.iloc[:, 1].std()

# Vẽ đồ thị hàm y = A * exp(B * x) + 1/(std_dev_col2 * sqrt(2 * pi))
x = np.linspace(min(df.iloc[:, 0]), max(df.iloc[:, 0]), 100)
y = A * np.exp(B * x) + 1 / (std_dev_col2 * sqrt(2 * pi))

plt.figure(figsize=(10, 6))

# Vẽ đồ thị hàm y = A * exp(B * x) + 1/(std_dev_col2 * sqrt(2 * pi))
plt.plot(x, y, label=f'y = {A:.4f} * e^({B:.4f}x) + 1/({std_dev_col2:.4f} * sqrt(2 * pi))')

# Vẽ đồ thị cột 2 theo cột 1
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], color='r', label='PM2.5')

# Đánh dấu các điểm trên đồ thị y = A * exp(B * x) tại các điểm trên trục hoành giống PM2.5
y_points = A * np.exp(B * df.iloc[:, 0]) + 1 / (std_dev_col2 * sqrt(2 * pi))
plt.scatter(df.iloc[:, 0], y_points, edgecolor='blue', facecolor='none', s=50)

# Thêm nhãn và tiêu đề
plt.xlabel('RH%')
plt.ylabel('Giá trị PM2.5')
plt.title('Phương Trình Hồi Quy Hàm Số Mũ')
plt.legend()

# Hiển thị đồ thị
plt.show()
