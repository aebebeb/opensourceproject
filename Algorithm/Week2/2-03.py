# 정숫값 입력
# End 입력하면 그 시점에서 원소 수 확정

from max import max_of

print("배열의 최댓값을 구합니다.")
print("주의: ""End""를 입력하면 종료합니다.")

number = 0
x = []

while True:
    s = input(f'x[{number}]값을 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print("{}개를 입력했습니다.".format(number+1))
print("최댓값은 {}입니다.".format(max_of(list)))