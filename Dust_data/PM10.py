import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('TADBH.csv')

# Vẽ biểu đồ đường
plt.figure(figsize=(10, 6))

# Đồ thị cột 4
plt.plot(df.iloc[:, 3], label='Độ Ẩm', color='orange')

# Đồ thị cột 5
plt.plot(df.iloc[:, 2], label='Nhiệt Độ', color='gray')

# Đồ thị cột 6

# Đồ thị cột 8
plt.plot(df.iloc[:, 7], label='PM10', color='red')

# Đánh dấu các giá trị của cột 6, 7, 8 bằng dấu chấm
for column_index, column_name in enumerate(df.columns[5:8]):
    plt.scatter(df.index, df[column_name], color='black', marker='.')

plt.xlabel('Step')
plt.ylabel('Giá Trị')
plt.title('Không Giảm Ẩm - Không Bật Quạt')
plt.grid(True)  # Thêm lưới cho biểu đồ

# Hiển thị chú thích
plt.legend()

plt.show()
