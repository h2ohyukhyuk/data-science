from scipy import stats
import numpy as np

'''
independence t-test
https://data101.oopy.io/ab-test-python-or-without-code

'''
design_A = [16.4, 12.6, 17.5, 18.8, 12.1, 13.2, 14.5, 12.4, 17.5, 25.4, 9.3, 10.4]
design_B = [12.1, 11.8, 14.7, 13.1, 13.8, 10.1, 9.1, 13.5, 11.2, 13.7]

print('avg A ', sum(design_A)/len(design_A))
print('var A ', np.var(design_A))
print('avg B ', sum(design_B)/len(design_B))
print('var B ', np.var(design_B))
# 검정 코드 실시
result = stats.ttest_ind(design_A,
                design_B,
                equal_var=False)

print(result)

result = stats.ttest_ind(design_B,
                design_A,
                equal_var=False)

print(result)
'''
avg A  15.008333333333335
var A  17.927430555555553
avg B  12.309999999999999
var B  2.8629000000000007
Ttest_indResult(statistic=1.933374622222914, pvalue=0.07227304704557012)
Ttest_indResult(statistic=-1.933374622222914, pvalue=0.07227304704557012)

가설: 높은 평균을 가지는 게 더 좋다.
검정 p-value: 0.05 보다 크면 기각.(0.07 > 0.5 기각됨)
결론: A, B 둘 중 어떤게 더 좋다고 할 수 없다.

둘의 분산은 17, 2 로 확연히 다르다. 
equal_var=False 이면 Welch t-test를 사용.
아니면 student t-test를 사용? 둘의 차이는?

'''