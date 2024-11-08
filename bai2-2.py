import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
path = 'bai2.csv'
df = pd.read_csv(path)

# Lấy dữ liệu từ các cột
NOC = df['NOC'].values  # Mảng các quốc gia (NOC)
Gold = df['Gold'].values.astype(float)  # Mảng số huy chương vàng
Silver = df['Silver'].values.astype(float)  # Mảng số huy chương bạc
Bronze = df['Bronze'].values.astype(float)  # Mảng số huy chương đồng

# Tính tổng huy chương vàng (áp dụng quy tắc: 2 bạc = 1 vàng, 3 đồng = 1 vàng)
Total = Gold + (Silver / 2) + (Bronze / 3)

# Tính tổng huy chương (vàng, bạc, đồng)
Total_medals = Gold + Silver + Bronze

# Sắp xếp thứ hạng các quốc gia theo tổng huy chương vàng
ranked_indices = np.argsort(Total)[::-1]  # Sắp xếp giảm dần theo tổng huy chương vàng
ranked_NOC = NOC[ranked_indices]
ranked_Total = Total[ranked_indices]

# Tạo danh sách thứ hạng
ranks = np.arange(1, len(ranked_NOC) + 1)

# In ra thứ hạng
print("\nRanking of Countries by Total Gold Medals:")
for rank, noc, total in zip(ranks, ranked_NOC, ranked_Total):
    print(f"Rank {rank}: {noc} - Total Gold Medals: {total:.2f}")

# Tính các chỉ số thống kê cơ bản
mean_gold = np.mean(Total)
std_gold = np.std(Total)
min_gold = np.min(Total)
max_gold = np.max(Total)

print("\nStatistics for Total Gold Medals:")
print(f"Mean: {mean_gold:.2f}")
print(f"Standard Deviation: {std_gold:.2f}")
print(f"Min: {min_gold:.2f}")
print(f"Max: {max_gold:.2f}")

# Vẽ biểu đồ cột (Bar chart)
plt.figure(figsize=(10, 5))
plt.bar(ranked_NOC, ranked_Total, color='gold')
plt.title('Total Gold Medals by Country')
plt.xlabel('Country (NOC)')
plt.ylabel('Total Gold Medals')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('gold_medals_bar_chart.png')
plt.show()

# Vẽ biểu đồ tròn (Pie chart)
plt.figure(figsize=(8, 8))
plt.pie(ranked_Total, labels=ranked_NOC, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Total Gold Medals by Country')
plt.savefig('gold_medals_pie_chart.png')
plt.show()

# Vẽ histogram
plt.figure(figsize=(10, 5))
plt.hist(ranked_Total, bins=10, color='blue', edgecolor='black')
plt.title('Histogram of Total Gold Medals')
plt.xlabel('Total Gold Medals')
plt.ylabel('Frequency')
plt.savefig('gold_medals_histogram.png')
plt.show()

# Lưu danh sách thứ hạng vào file văn bản
with open('thuhanghcv.txt', 'w') as f:
    f.write("Ranking of Countries by Total Gold Medals:\n")
    for rank, noc, total_gold in zip(ranks, ranked_NOC, ranked_Total):
        f.write(f"Rank {rank}: {noc} - Total Gold Medals: {total_gold:.2f}\n")
print("\nRanking list exported to 'thuhanghcv.txt'")

# Lưu dữ liệu đã sửa vào file CSV
df['Total'] = Total  # Thêm cột tổng huy chương vàng vào DataFrame
df.to_csv('bai2-2moi.csv', index=False)
print("Data saved to 'bai2-2moi.csv'")
