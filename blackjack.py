import random
ruka = 0
dealer = 0
rating = 0
while ruka <= 17:
    ruka += random.randrange(1, 7, 1)
    dealer += random.randrange(1, 7, 1)
if ruka < 22 and dealer > 21 or dealer < ruka:
    print("You win!")
    rating += 1
elif ruka == dealer:
    print("Draw!")
else:
    print("You lose!")
    rating -= 1
print(ruka, dealer, rating)
print("Зафиксировано")