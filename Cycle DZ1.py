import array
from collections import Counter, defaultdict

table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]
all_cards =
print(all_cards)
rev_hand = dict(k.split('_') for k in all_cards)
print(rev_hand)

d = defaultdict(int)

for suites in rev_hand.values():
    d[suites] += 1
    print(d)
for v in d.values():
    if d.values() == 5:
        print('Flush')

