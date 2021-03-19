import random

# Update with players and their list of country picks. It's a Python dictionary.
lottery_book = {
    'Aksel': ['Wu', 'Jianzhou', 'Denmark'],
    'Deluxe': ['Muscovy', 'Brandebeast', 'Milan'],
    'Viewless': ['Shimazu', 'Uesugi', 'Jianzhou'],
    'Lalaria': ['France', 'Florence', 'Castile'],
    'EE': ['Dai Viet', 'Pgaranga', 'Mahapajihit'],
    'Writer': ['Castile', 'Denmark', 'Georgia'],
    'Diglett': ['Muscovy', 'Venice', 'Sweden'],
    'Numberline': ['Bengal', 'Vijay', 'Jianzhou'],
    'Neighbour': ['Brandebeast', 'Poland', 'Milan'],
    'Marko': ['Mamluks', 'England', 'Poland'],
    'Lofu': ['Köln', 'Trier', 'Brandebeast']
}

# Display (print) random choice for each player in the lottery book:
print('--------------------')
#for player in lottery_book:
 #   print(f'{player} will play as: {random.choice(lottery_book[player])}')

# Use code below to reroll or roll newcomers.
while True:
    print('--------------------')
    reroll_name = input('Write a player to reroll, or "END" to end: ')
    if reroll_name == 'END' or reroll_name == 'end':
        break

    reroll_tags = []
    for i in range(3):  # Make one of the three "reroll" if rerolling 'cuz one is taken
        reroll_tags.append(input('Write a country choice: '))

    print(f'{reroll_name} will play as: {random.choice(reroll_tags)}')