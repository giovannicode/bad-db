from random import randint

db_file = open('data.db', 'w')

for x in range (0, 9):
    db_file.write(str(x))

db_file.close()
