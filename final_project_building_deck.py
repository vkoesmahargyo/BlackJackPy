import random

DECK = ['A Spades', '2 Spades', '3 Spades', '4 Spades', '5 Spades', 
			'6 Spades', '7 Spades', '8 Spades', '9 Spades', '10 Spades', 
			'J Spades', 'Q Spades', 'K Spades', 'A Clubs', '2 Clubs', 
			'3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs', '7 Clubs', 
			'8 Clubs', '9 Clubs', '10 Clubs', 'J Clubs', 'Q Clubs', 
			'K Clubs', 'A Hearts', '2 Hearts', '3 Hearts', '4 Hearts',
			'5 Hearts', '6 Hearts', '7 Hearts', '8 Hearts', '9 Hearts', 
			'10 Hearts', 'J Hearts', 'Q Hearts', 'K Hearts', 'A Diamonds', 
			'2 Diamonds', '3 Diamonds', '4 Diamonds', '5 Diamonds', 
			'6 Diamonds', '7 Diamonds', '8 Diamonds', '9 Diamonds', 
			'10 Diamonds', 'J Diamonds', 'Q Diamonds', 'K Diamonds']
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']*13
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
trial_deck = {}
for i in range(1, 53):
	trial_deck[i] = {
						'card': values[i-1] + ' of ' + suits[i-1],
						'actual_value': []

					}

trial_deck = {
				1: {'card': 'A of Spades', 'actual_value': []}, 
				2: {'card': '2 of Hearts', 'actual_value': []}, 
				3: {'card': '3 of Clubs', 'actual_value': []}, 
				4: {'card': '4 of Diamonds', 'actual_value': []}, 
				5: {'card': '5 of Spades', 'actual_value': []}, 
				6: {'card': '6 of Hearts', 'actual_value': []}, 
				7: {'card': '7 of Clubs', 'actual_value': []}, 
				8: {'card': '8 of Diamonds', 'actual_value': []}, 
				9: {'card': '9 of Spades', 'actual_value': []},
				10: {'card': '10 of Hearts', 'actual_value': []}, 
				11: {'card': 'J of Clubs', 'actual_value': []}, 
				12: {'card': 'Q of Diamonds', 'actual_value': []}, 
				13: {'card': 'K of Spades', 'actual_value': []}, 
				14: {'card': 'A of Hearts', 'actual_value': []}, 
				15: {'card': '2 of Clubs', 'actual_value': []}, 
				16: {'card': '3 of Diamonds', 'actual_value': []}, 
				17: {'card': '4 of Spades', 'actual_value': []}, 
				18: {'card': '5 of Hearts', 'actual_value': []}, 
				19: {'card': '6 of Clubs', 'actual_value': []}, 
				20: {'card': '7 of Diamonds', 'actual_value': []}, 
				21: {'card': '8 of Spades', 'actual_value': []}, 
				22: {'card': '9 of Hearts', 'actual_value': []}, 
				23: {'card': '10 of Clubs', 'actual_value': []}, 
				24: {'card': 'J of Diamonds', 'actual_value': []}, 
				25: {'card': 'Q of Spades', 'actual_value': []}, 
				26: {'card': 'K of Hearts', 'actual_value': []}, 
				27: {'card': 'A of Clubs', 'actual_value': []}, 
				28: {'card': '2 of Diamonds', 'actual_value': []}, 
				29: {'card': '3 of Spades', 'actual_value': []}, 
				30: {'card': '4 of Hearts', 'actual_value': []}, 
				31: {'card': '5 of Clubs', 'actual_value': []}, 
				32: {'card': '6 of Diamonds', 'actual_value': []}, 
				33: {'card': '7 of Spades', 'actual_value': []}, 
				34: {'card': '8 of Hearts', 'actual_value': []}, 
				35: {'card': '9 of Clubs', 'actual_value': []}, 
				36: {'card': '10 of Diamonds', 'actual_value': []}, 
				37: {'card': 'J of Spades', 'actual_value': []}, 
				38: {'card': 'Q of Hearts', 'actual_value': []}, 
				39: {'card': 'K of Clubs', 'actual_value': []}, 
				40: {'card': 'A of Diamonds', 'actual_value': []}, 
				41: {'card': '2 of Spades', 'actual_value': []}, 
				42: {'card': '3 of Hearts', 'actual_value': []}, 
				43: {'card': '4 of Clubs', 'actual_value': []}, 
				44: {'card': '5 of Diamonds', 'actual_value': []}, 
				45: {'card': '6 of Spades', 'actual_value': []}, 
				46: {'card': '7 of Hearts', 'actual_value': []}, 
				47: {'card': '8 of Clubs', 'actual_value': []}, 
				48: {'card': '9 of Diamonds', 'actual_value': []}, 
				49: {'card': '10 of Spades', 'actual_value': []}, 
				50: {'card': 'J of Hearts', 'actual_value': []}, 
				51: {'card': 'Q of Clubs', 'actual_value': []}, 
				52: {'card': 'K of Diamonds', 'actual_value': []}
}

# for key, val in trial_deck.items():
# 	trial_deck[key] = {}



dealer_cards = []

def shuffle_deck(deck):
	random.shuffle(deck)
	return deck



