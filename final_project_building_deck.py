import random
from getkey import getkey, keys


suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']*13
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
trial_deck = {}
for i in range(1, 53):
	trial_deck[i] = {
						'card': values[i-1] + ' of ' + suits[i-1],
						'actual_value': []

					}

DECK_DICT = {
				1: {'card': 'A of Spades', 'actual_value': [1, 11]}, 
				2: {'card': '2 of Hearts', 'actual_value': [2]}, 
				3: {'card': '3 of Clubs', 'actual_value': [3]}, 
				4: {'card': '4 of Diamonds', 'actual_value': [4]}, 
				5: {'card': '5 of Spades', 'actual_value': [5]}, 
				6: {'card': '6 of Hearts', 'actual_value': [6]}, 
				7: {'card': '7 of Clubs', 'actual_value': [7]}, 
				8: {'card': '8 of Diamonds', 'actual_value': [8]}, 
				9: {'card': '9 of Spades', 'actual_value': [9]},
				10: {'card': '10 of Hearts', 'actual_value': [10]}, 
				11: {'card': 'J of Clubs', 'actual_value': [10]}, 
				12: {'card': 'Q of Diamonds', 'actual_value': [10]}, 
				13: {'card': 'K of Spades', 'actual_value': [10]}, 
				14: {'card': 'A of Hearts', 'actual_value': [1, 11]}, 
				15: {'card': '2 of Clubs', 'actual_value': [2]}, 
				16: {'card': '3 of Diamonds', 'actual_value': [3]}, 
				17: {'card': '4 of Spades', 'actual_value': [4]}, 
				18: {'card': '5 of Hearts', 'actual_value': [5]}, 
				19: {'card': '6 of Clubs', 'actual_value': [6]}, 
				20: {'card': '7 of Diamonds', 'actual_value': [7]}, 
				21: {'card': '8 of Spades', 'actual_value': [8]}, 
				22: {'card': '9 of Hearts', 'actual_value': [9]}, 
				23: {'card': '10 of Clubs', 'actual_value': [10]}, 
				24: {'card': 'J of Diamonds', 'actual_value': [10]}, 
				25: {'card': 'Q of Spades', 'actual_value': [10]}, 
				26: {'card': 'K of Hearts', 'actual_value': [10]}, 
				27: {'card': 'A of Clubs', 'actual_value': [1, 11]}, 
				28: {'card': '2 of Diamonds', 'actual_value': [2]}, 
				29: {'card': '3 of Spades', 'actual_value': [3]}, 
				30: {'card': '4 of Hearts', 'actual_value': [4]}, 
				31: {'card': '5 of Clubs', 'actual_value': [5]}, 
				32: {'card': '6 of Diamonds', 'actual_value': [6]}, 
				33: {'card': '7 of Spades', 'actual_value': [7]}, 
				34: {'card': '8 of Hearts', 'actual_value': [8]}, 
				35: {'card': '9 of Clubs', 'actual_value': [9]}, 
				36: {'card': '10 of Diamonds', 'actual_value': [10]}, 
				37: {'card': 'J of Spades', 'actual_value': [10]}, 
				38: {'card': 'Q of Hearts', 'actual_value': [10]}, 
				39: {'card': 'K of Clubs', 'actual_value': [10]}, 
				40: {'card': 'A of Diamonds', 'actual_value': [1, 11]}, 
				41: {'card': '2 of Spades', 'actual_value': [2]}, 
				42: {'card': '3 of Hearts', 'actual_value': [3]}, 
				43: {'card': '4 of Clubs', 'actual_value': [4]}, 
				44: {'card': '5 of Diamonds', 'actual_value': [5]}, 
				45: {'card': '6 of Spades', 'actual_value': [6]}, 
				46: {'card': '7 of Hearts', 'actual_value': [7]}, 
				47: {'card': '8 of Clubs', 'actual_value': [8]}, 
				48: {'card': '9 of Diamonds', 'actual_value': [9]}, 
				49: {'card': '10 of Spades', 'actual_value': [10]}, 
				50: {'card': 'J of Hearts', 'actual_value': [10]}, 
				51: {'card': 'Q of Clubs', 'actual_value': [10]}, 
				52: {'card': 'K of Diamonds', 'actual_value': [10]}
}

user_list = [
			{
			'name': 'dealer',
			'current_hand': []
			},
			{
			'name': '',
			'current_hand': [],
			'total_money': 0,
			'current_bet': 0
			}


]

def shuffle_deck(deck):
	shuffled_list = []
	for key in deck.keys():
		shuffled_list.append(key)
	random.shuffle(shuffled_list)
	return shuffled_list

def deal_card(deck, user):
	current_card = shuffled_list.pop()


def instructions():
	rules = """The point of the game is to beat the dealer's hand without
			going over 21. You will be dealt 2 cards, as will the dealer
			but only one of the dealer's cards will be shown. You can choose
			to stand (s) - stop being dealt cards, or hit (h) - continue
			to be dealth cards. All face cards are worth 10, an Ace can be
			either 1 or 11. 
			The Dealer must continue to take cards until they are above 17.
			To quit at any time, press 'q'. 
			[WILL ADD BETTING STUFF LATER]
			"""
	return rules



while True:
	
	

