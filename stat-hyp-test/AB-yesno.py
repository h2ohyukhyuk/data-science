import pandas as pd
from scipy.stats import chi2_contingency


def click_abtest(a_click, total_a, b_click, total_b):

    click = [a_click, b_click] # A와 B의 클릭한 유저 수
    no_click = [total_a - a_click, total_b - b_click]  # A와 B의 클릭 안 한 유저 수
    cont_table = pd.DataFrame([click, no_click], columns=['A', 'B'], index=['click', 'no_click'])
    chi2, p_val, d_f, expected = chi2_contingency([click, no_click])

    print("카이제곱 통계량 :", format(chi2, '.5f'))
    print("pvalue :", format(p_val, '.5f'))

# A의 클릭수(13)와 A의 데이터 전체 개수(244), B의 클릭수(23)와 A의 데이터 전체 개수(287)를 정의한 클래스에 넣어줍니다.
a_click = 13
total_a = 244
b_click = 23
total_b = 287
print('a prob ', 100*a_click/total_a)
print('b prob ', 100*b_click/total_b)
click_abtest(a_click, total_a, b_click, total_b)

'''

a prob  5.327868852459017
b prob  8.013937282229966
카이제곱 통계량 : 1.11053
pvalue : 0.29197

가설: 높은 확률을 가지는 게 더 좋다.
검정 p-value: 0.05 보다 크면 기각.(0.07 > 0.5 기각됨)
결론: A, B 둘 중 어떤게 더 좋다고 할 수 없다.

평균내기 어려운 데이터 -> nominal data
빈도주의 ->  카이제곱 검정
베이지안 -> ?
ANOVA -> ANalysis Of VAriance
'''