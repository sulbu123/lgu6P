import streamlit as st
import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib.font_manager as fm 


# 한글폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic' 
plt.rcParams['axes.unicode_minus'] = False 
sns.set(font='Malgun Gothic', 
        rc={'axes.unicode_minus' : False}, 
        style='darkgrid')

# 페이지 설정
# st.set_page_config(page_title="Matplotlib & Seaborn 튜토리얼", layout="wide") 
st.title("Matplotlib & Seaborn 튜토리얼") 

# 데이터셋 불러오기 
tips = sns.load_dataset('tips') 

# 데이터 미리보기 
st.subheader('데이터 미리보기')
st.dataframe(tips.head())

# 기본 막대 그래프, matplotlit + seaborn 
st.subheader("1. 기본 막대 그래프")
# 객체지향방식으로 차트 작성 하는 이유
# 그래프를 그리는 목적 : (예쁘게) 잘 나오라고
fig, ax = plt.subplots(figsize=(10, 6)) # matplotlib

sns.barplot(data=tips, x='day', y='total_bill', ax=ax) # seaborn

ax.set_title('요일별 평균 지불 금액') # matplotlib
ax.set_xlabel('요일')               # matplotlib
ax.set_ylabel('평균 지불 금액($)')   # matplotlib

# plt.show() ==> 이 문법은 jupyter notebook, google colab에서 활용할 때 사용
st.pyplot(fig) # streamlit 문법

# 산점도
# x축, y축이 연속형 변수여야 합니다. 
st.subheader("2. 산점도")
fig1, ax1 = plt.subplots(figsize=(10, 6)) # matplotlib

sns.barplot(data=tips, x='day', y='total_bill', ax=ax) # seaborn
sns.scatterplot(data=tips, x = 'total_bill', y = 'tip', hue='day', size='size', ax=ax1)
st.pyplot(fig1)

# 히트맵
st.subheader("3. 히트맵") 

# 요일과 시간별 평균 팁 계산 
pivot_df = tips.pivot_table(values='tip', index='day', columns='time', aggfunc='mean')
fig2, ax2 = plt.subplots(figsize=(10, 6)) 
sns.heatmap(pivot_df, annot=True, fmt='.2f', ax=ax2)
st.pyplot(fig2)

#회귀선이 있는 산점도
st.subheader('4. 회귀선이 있는 산점도')
fig3, ax3 = plt.subplots(figsize=(10,6))
sns.regplot(data=tips, x='total_bill', y = 'tip', scatter_kws = {'alpha':0.5}, ax=ax3)
st.pyplot(fig3)

# chatGPT 질문 던지기 팁 : fig, ax = plt.subplots() 이런방식으로 만드세요!

# import streamlit as st
# import pandas as pd 
# import matplotlib.pyplot as plt 
# import seaborn as sns 

# # 한글폰트 설정
# plt.rcParams['font.family'] = 'Malgun Gothic' 
# plt.rcParams['axes.unicode_minus'] = False 
# sns.set(font='Malgun Gothic', 
#         rc={'axes.unicode_minus' : False}, 
#         style='darkgrid')

# # 데이터셋 불러오기
# tips = sns.load_dataset('tips')

# # 데이터 미리보기
# st.subheader('데이터 미리보기')
# st.dataframe(tips.head())

# # 5. 박스 플롯
# st.subheader("5. 박스 플롯")
# fig4, ax4 = plt.subplots(figsize=(10, 6))
# sns.boxplot(data=tips, x='day', y='total_bill', ax=ax4)
# ax4.set_title('요일별 총 지불 금액의 분포')
# ax4.set_xlabel('요일')
# ax4.set_ylabel('총 지불 금액($)')
# st.pyplot(fig4)

# # 6. 히스토그램
# st.subheader("6. 히스토그램")
# fig5, ax5 = plt.subplots(figsize=(10, 6))
# sns.histplot(data=tips, x='total_bill', kde=True, ax=ax5)
# ax5.set_title('총 지불 금액의 분포')
# ax5.set_xlabel('총 지불 금액($)')
# ax5.set_ylabel('빈도수')
# st.pyplot(fig5)

# # 7. 파이 차트
# st.subheader("7. 파이 차트")
# time_counts = tips['time'].value_counts()
# fig6, ax6 = plt.subplots(figsize=(8, 8))
# ax6.pie(time_counts, labels=time_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
# ax6.set_title('점심과 저녁의 비율')
# st.pyplot(fig6)

# # 8. 상관 관계 히트맵
# st.subheader("8. 상관 관계 히트맵")

# # 숫자형 데이터만 추출
# numeric_tips = tips.select_dtypes(include=['float64', 'int64'])

# # 상관 행렬 계산
# corr_matrix = numeric_tips.corr()

# # 히트맵 시각화
# fig7, ax7 = plt.subplots(figsize=(10, 6))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax7)

# ax7.set_title('변수 간 상관 관계 히트맵')
# st.pyplot(fig7)

# # 9. 성별 평균 팁
# st.subheader("9. 성별 평균 팁")
# fig8, ax8 = plt.subplots(figsize=(10, 6))
# sns.barplot(data=tips, x='sex', y='tip', ax=ax8)
# ax8.set_title('성별 평균 팁')
# ax8.set_xlabel('성별')
# ax8.set_ylabel('평균 팁($)')
# st.pyplot(fig8)

# # 10. 팁과 총 지불 금액 간의 관계
# st.subheader("10. 팁과 총 지불 금액 간의 관계")
# fig9, ax9 = plt.subplots(figsize=(10, 6))
# sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', size='size', ax=ax9)
# ax9.set_title('팁과 총 지불 금액 간의 관계')
# ax9.set_xlabel('총 지불 금액($)')
# ax9.set_ylabel('팁($)')
# st.pyplot(fig9)