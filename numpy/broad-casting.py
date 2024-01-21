import numpy as np

'''
M1 + M2
0. 같은 차원끼리 비교해서 같거나 한쪽이 1 이어야한다. 
 연산이 되는 경우:   (2,3,4,5) + (3,4,1)
 연산이 안되는 경우: (2,3,4,5) + (3,2,1), 두번 째 차원에서 일치하지 않기 때문에
1. 차원을 비교한다.
2. 차원 개수가 적은 왼쪽을 1인 차원으로 채운다.
3. 양쪽에서 1인 차원을 상대방에 맞게 확장한다.
4. 양쪽 모양이 같다면 연산한다.

'''
a012 = np.array([0,1,2])
b555 = np.array([5,5,5])
one_3x3 = np.ones((3, 3))
one_3x2 = np.ones((3, 2))

print(one_3x3 + a012)
'''
(3,3) + (3)
(3,3) + (1,3) : 차원 추가
(3,3) + (3,3) : 브로드캐스팅
'''

print(b555[:,None] + a012)
'''
(3,1) + (3)
(3,1) + (1,3) : 차원 추가
(3,3) + (3,3) : 브로드캐스팅
'''

one_2x3 = np.ones((2,3))
print(one_2x3 + a012)
'''
(2,3) + (3)
(2,3) + (1,3)
(2,3) + (2,3)
'''

try:
    one_3x2 + a012
    '''
    (3,2) + (3)
    (3,2) + (1,3) : 차원 추가
    (3,2) + (3,3) : 브로드 캐스트, 연산 불가
    '''

except Exception as e:
    print('error at one_3x2 + a012', e)

x = np.linspace(0, 5, 5)
y = np.linspace(0, 5, 5)[:, None]
z = np.sin(x)**10 + np.cos(10 + y + x)
print(z)
'''
(5) + ((5,1) + (5))
(5) + ((5,1) + (1,5))
(5) + ((5,5) + (5,5))
(5) + (5,5)
(5, 5) + (5,5)

'''


h = np.random.random((3,4,6,3))

print((h + a012).shape)
'''
(3,4,6,3) + (3)
(3,4,6,3) + (6,3)
(3,4,6,3) + (4,6,3)
(3,4,6,3) + (3,4,6,3)
'''

u = np.random.random((6,1))
print((h+u).shape)
'''
(3,4,6,3) + (6,1)
(3,4,6,3) + (6,3)
(3,4,6,3) + (4,6,3)
(3,4,6,3) + (3,4,6,3)
'''