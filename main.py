
import random

def create_deck():
    suits = ['Черви', 'Бубны', 'Трефы', 'Пики']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    deck = [{'ранг': rank, 'масть': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_players, cards_per_player):
    hands = [[] for _ in range(num_players)]
    for _ in range(cards_per_player):
        for player in range(num_players):
            card = deck.pop()
            hands[player].append(card)
    return hands

def display_hand(hand):
    for card in hand:
        print(f"{card['ранг']} {card['масть']}")

def evaluate_hand(hand):
    return "ХЗ КАК комбо делать"

def poker():
    num_players = 2
    cards_per_player = 2

    deck = create_deck()
    hands = deal_cards(deck, num_players, cards_per_player)

    for i in range(num_players):
        print(f"\n Игрок {i + 1}:\n")
        display_hand(hands[i])
        hand_value = evaluate_hand(hands[i])
        print(f"Комбинация: {hand_value}")

poker()

      # def is_king_move_possible(start, target):
#     start_col, start_row = start
#     target_col, target_row = target

#     col_diff = abs(target_col - start_col)
#     row_diff = abs(target_row - start_row)

#     return col_diff <= 1 and row_diff <= 1

# start_position = (4, 4)
# target_position = (5, 5)

# if is_king_move_possible(start_position, target_position):
#     print("Король может совершить ход на заданное поле.")
# else:
#     print("Король не может совершить ход на заданное поле.")
# firstmess = str(input(" введите товар из списка "))
   
