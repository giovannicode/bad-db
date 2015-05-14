from random import randint

db_file = open('data.db', 'w')

for x in range (0, 9):
    random_int = randint(0, 9)
    db_file.write(str(random_int))
    db_file.write('\n')

db_file.close()
