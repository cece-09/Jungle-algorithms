import sys
n = int(input())
k = int(input())
cards = [sys.stdin.readline().strip() for _ in range(n)]

# 만든 카드를 담을 배열
result = set()

# string: 카드를 합쳐 만든 문자
# select_number: 뽑은 카드 수
# picked: 이미 뽑은 카드의 idx 배열
def pick(string, select_num, picked):
    # n이 k가 되면 카드를 모두 뽑은 것
    if select_num == k:
        # 이미 뽑은 카드와 겹치는 지 확인하고,
        # 겹치지 않으면 카드 배열에 추가
        result.add(string)
        return

    for card_idx in range(len(cards)):
        # picked에 card_idx가 있으면 이미 뽑은 카드니까 제외
        if card_idx not in picked:
            # 지금 뽑은 카드의 idx를 뽑은 카드의 idx 배열에 추가
            picked.append(card_idx)
            # 지금 뽑은 카드의 값을 기존에 뽑은 값들 뒤에 더해서 새 변수에 할당
            new_string = string + cards[card_idx]
            # 지금 완성된 카드값, 뽑은 카드 수, 사용한 카드의 idx들
            pick(new_string, select_num+1, picked)
            # 다음 반복에서는 다른 카드를 뽑을 거니까 지금 뽑은 카드의 idx 제거
            picked.pop()


pick("", 0, [])
print(len(result))