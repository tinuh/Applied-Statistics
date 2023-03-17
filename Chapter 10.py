from random import randint, choice, shuffle

# number 21
num = 3
wins = 0
for i in range(10000):
  n = randint(0, 9)
  if n == num:
    wins += 1
  
print(f'{wins/100}%')

# number 30
money = 0
for i in range(10000000):
  ace = 1
  cards = [1, 2, 3, 4, 5]
  shuffle(cards)
  pick = 0
  while ace in cards:
    cards.remove(choice(cards))
    pick += 1
  
  if pick == 1:
    money += 100
  elif pick == 2:
    money += 50
  elif pick == 3:
    money += 20
  elif pick == 4:
    money += 10
  elif pick == 5:
    money += 5

print(f'${money/10000000}')
