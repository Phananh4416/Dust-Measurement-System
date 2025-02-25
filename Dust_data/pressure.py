import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('TADBH.csv')

# Vẽ biểu đồ đường
plt.figure(figsize=(10, 6))

# Đồ thị cột 4
plt.plot(df.iloc[:, 4], label='Áp Suất', color='orange')


# Đánh dấu các giá trị của cột 6, 7, 8 bằng dấu chấm


plt.xlabel('Step')
plt.ylabel('Giá Trị')
plt.title('Không Giảm Ẩm - Không Bật Quạt')
plt.grid(True)  # Thêm lưới cho biểu đồ

# Hiển thị chú thích
plt.legend()

plt.show()
