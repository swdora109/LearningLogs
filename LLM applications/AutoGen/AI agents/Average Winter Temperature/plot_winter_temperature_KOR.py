# filename: plot_winter_temperature_KOR.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ggplot 스타일 설정
plt.style.use('ggplot')

# 가상의 평균 기온 데이터 생성
years = np.arange(2014, 2025)
temperatures = np.random.uniform(-5, 5, size=len(years))  # -5도부터 5도 사이의 임의의 값

# 그래프 그리기
plt.figure(figsize=(10, 6))
sns.lineplot(x=years, y=temperatures, marker='o')

# X축과 Y축 설정
plt.xticks(years, labels=[str(year) for year in years])
plt.yticks(np.arange(-5, 5.5, 0.5))

# 제목 및 축 라벨 설정
plt.title('Changes in Average January Temperature in Korea (2014-2024)')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')

# 그래프 저장
plt.savefig('winter_temperature_KOR.png')