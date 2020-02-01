'''
달팽이 2단계
'''
def PrintList(li):
    for i in range(len(li)):
        for j in range(len(li[i])):
            print('{:2} '.format(li[i][j]), end='')
        print()
    print()

#snail = []
#for i in range(5):
#    snail.append([0,0,0,0,0])
    


# 여기서부터 숫자를 대입하는 과정            # 길이 : 5 - 4 - 4 - 3 - 3 - 2 - 2 - 1 - 1
                                # 좌표 : y - x - y - x - y - x - y - x - y
                                # 증감 : +   +   -   -   +   +   -   -   +
                                # 값    : num += 1
          


# 1. 프로그램은 상수에 대한 의존도가 낮을수록 좋다 (변수로 처리하는게 더 좋다)
# 좌표값(x,y)
# 반복횟수(길이)

length = int(input('길이 입력 : '))
snail = [[0 for cols in range(length)]for rows in range(length)]

num = 0
x, y = 0, -1
sign = 1

while True:
    for i in range(length): # y 증가 (5)
        num += 1
        y += sign       # sign은 부호랍니다...      
        snail[x][y] = num
    length -= 1     # 길이 감소
    
    if length == 0: break
        
    for i in range(length): # x 증가 (4)
        num += 1
        x += sign
        snail[x][y] = num
    sign *= -1      # 부호 반전

# 여기까지

PrintList(snail)
