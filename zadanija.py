import random
def first_hod():
    ruka = 0
    dealer = 0
    for i in range(0, 2, 1):
        ruka += random.randrange(1, 10, 1)
        dealer += random.randrange(1, 10, 1)
    print(ruka, dealer)
first_hod()

