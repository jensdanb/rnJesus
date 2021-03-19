import random


def roll_player_start_tags():
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
    rolled_tags = []

    print('--------------------')
    print('Player --- Country')
    for player in lottery_book:
        tag = random.choice(lottery_book[player])
        if tag in rolled_tags:
            print(f'{player} rolled {tag}, which is taken')
            lottery_book[player].remove(tag)
            print(f'{player} rerolls with {lottery_book[player]}')
            tag = random.choice(lottery_book[player])
        print(f'{player} --- {tag}')
        rolled_tags.append(tag)
    print(f'Taken tags are: {rolled_tags}')
    print('--------------------')
    return rolled_tags


# Use code below to reroll or roll newcomers.
def roll_tag_manually(taken_tags):
    while True:
        print('--------------------')
        player_name = input('Write the next player name, or "END" to end: ')
        if player_name == 'END' or player_name == 'end':
            break

        picks = []
        i = 0
        number_of_picks = input('Write number of picks')
        while i < int(number_of_picks):
            picks.append(input('Write a country choice: '))
            if picks[-1] in taken_tags:
                print(f"Country {(picks.pop(-1))} is taken, and was removed. Try again.")
                i -= 1
            i += 1
        tag = random.choice(picks)

        print(f'{player_name} --- {tag}')
        taken_tags.append(tag)


def roll_teams():
    player_list = ['Diglett', 'NumberLine', 'Writer', 'Marko', 'Deluxe']
    random.shuffle(player_list)
    print(player_list)
    i = 0
    while i < len(player_list):
        partner1 = player_list[i]
        i += 1
        try:
            partner2 = player_list[i]
            print(f"{partner1} teams with {partner2}.")
            i += 1
        except IndexError:
            print(f"{partner1} ended up last, without a partner")


if __name__ == '__main__':
    #taken_tags = roll_player_start_tags()
    #roll_tag_manually(taken_tags)
    roll_teams()



