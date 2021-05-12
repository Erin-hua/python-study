from die import Die

six_die = Die()
for r in range(1,11):
    six_die.roll_die()
print("------")

ten_die = Die(10)
for r in range(1,11):
    ten_die.roll_die()
print("------")

twenty_die = Die(20)
for r in range(1,11):
    twenty_die.roll_die()



