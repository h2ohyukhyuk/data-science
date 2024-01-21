from scipy import stats
import numpy as np

treatment = np.array([2, 3, 1, 4, 5, 3, 2, 5, 4, 5, 6, 5]) # 광고 집행 횟수
result = np.array([50, 72, 65, 58, 69, 67, 87, 85, 87, 65, 42, 76]) # 방문자 수
pearsonr, pvalue = stats.pearsonr(treatment, result)

print('len treatment ', len(treatment))
print('len result ', len(result))
print("p 값 :", format(pvalue, '.5f'))  # 상관계수가 0이다 즉, treatment와 result 간에는 아무런 상관이 없다는 걸 기각하려는 p-value임
print("피어슨 상관계수 (r) :", format(pearsonr, '.5f'))

'''
>>> p 값 : 0.76521
>>> 피어슨 상관계수 (r) : -0.09660

상관관계
p 값 이 유의수준 0.05보다 매우 높기 때문에 이번 광고와 방문자 수와는 상관관계가 없다는 결론을 내려야 한다.
pearson_r 값이 음수()이면 광고와 방문자수는 부정적인 상관관계를 갖는다.
오히려 광고를 많이 할수록 방문자수가 떨어질 수 있다는 것이다. 
그러나 p값이 애초에 유의수준에 비해 택도 없이 높으므로 상관관계를 따지는 것이 무의미하다.

'''