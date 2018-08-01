from time import sleep

CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"
suits = ['\u2663', '\u2665', '\u2666', '\u2660']*13
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
trial_deck = {}
for i in range(1, 53):
	trial_deck[i] = {
						'card': values[i-1] + ' '+ suits[i-1],
						'value': []

					}

DECK_DICT = {
				1: {'card': 'A ♣', 'value': [1, 11]},
				2: {'card': '2 ♥', 'value': [2]},
				3: {'card': '3 ♦', 'value': [3]},
				4: {'card': '4 ♠', 'value': [4]},
				5: {'card': '5 ♣', 'value': [5]},
				6: {'card': '6 ♥', 'value': [6]},
				7: {'card': '7 ♦', 'value': [7]},
				8: {'card': '8 ♠', 'value': [8]},
				9: {'card': '9 ♣', 'value': [9]},
				10: {'card': '10 ♥', 'value': [10]},
				11: {'card': 'J ♦', 'value': [10]},
				12: {'card': 'Q ♠', 'value': [10]},
				13: {'card': 'K ♣', 'value': [10]},
				14: {'card': 'A ♥', 'value': [1, 11]},
				15: {'card': '2 ♦', 'value': [2]},
				16: {'card': '3 ♠', 'value': [3]},
				17: {'card': '4 ♣', 'value': [4]},
				18: {'card': '5 ♥', 'value': [5]},
				19: {'card': '6 ♦', 'value': [6]},
				20: {'card': '7 ♠', 'value': [7]},
				21: {'card': '8 ♣', 'value': [8]},
				22: {'card': '9 ♥', 'value': [9]},
				23: {'card': '10 ♦', 'value': [10]},
				24: {'card': 'J ♠', 'value': [10]},
				25: {'card': 'Q ♣', 'value': [10]},
				26: {'card': 'K ♥', 'value': [10]},
				27: {'card': 'A ♦', 'value': [1, 11]},
				28: {'card': '2 ♠', 'value': [2]},
				29: {'card': '3 ♣', 'value': [3]},
				30: {'card': '4 ♥', 'value': [4]},
				31: {'card': '5 ♦', 'value': [5]},
				32: {'card': '6 ♠', 'value': [6]},
				33: {'card': '7 ♣', 'value': [7]},
				34: {'card': '8 ♥', 'value': [8]},
				35: {'card': '9 ♦', 'value': [9]},
				36: {'card': '10 ♠', 'value': [10]},
				37: {'card': 'J ♣', 'value': [10]},
				38: {'card': 'Q ♥', 'value': [10]},
				39: {'card': 'K ♦', 'value': [10]},
				40: {'card': 'A ♠', 'value': [1, 11]},
				41: {'card': '2 ♣', 'value': [2]},
				42: {'card': '3 ♥', 'value': [3]},
				43: {'card': '4 ♦', 'value': [4]},
				44: {'card': '5 ♠', 'value': [5]},
				45: {'card': '6 ♣', 'value': [6]},
				46: {'card': '7 ♥', 'value': [7]},
				47: {'card': '8 ♦', 'value': [8]},
				48: {'card': '9 ♠', 'value': [9]},
				49: {'card': '10 ♣', 'value': [10]},
				50: {'card': 'J ♥', 'value': [10]},
				51: {'card': 'Q ♦', 'value': [10]},
				52: {'card': 'K ♠', 'value': [10]}}



user_list = [
			{
			'name': 'dealer',
			'current_hand': [6, 2]
			},
			{
			'name': 'Eden',
			'current_hand': [],
			'total_money': 1000,
			'current_bet': 0
			}


]
deck = [46, 34, 24, 13, 27, 35, 29, 12, 8, 2, 30, 50, 18, 42, 32, 3, 20, 21, 23, 28, 17, 40, 25, 1, 5, 33, 22, 45, 9, 19, 39, 51, 15, 44, 14, 47, 36, 4, 43, 10, 48, 11, 49, 41, 37, 7, 31, 26, 52, 38, 16]


def get_dealer_face_up_card(user_list, deck):
	print('Dealer:\t', DECK_DICT[user_list[0]['current_hand'][0]]['card']) # printing out only the first of dealer's cards




def get_dealer_two_card_sum(user_list, deck):
	"""Getting sum of dealer's two cards, and returning their total along with
	length of the first and second card (to check which is an ace)."""
	total = 0
	card_1_ace = check_if_ace(user_list[0]['current_hand'][0])
	card_2_ace = check_if_ace(user_list[0]['current_hand'][1])
	if card_1_ace == False and card_2_ace == False: # neither is an ace
		total += DECK_DICT[user_list[0]['current_hand'][0]]['value'][0] + DECK_DICT[user_list[0]['current_hand'][1]]['value'][0] # sum of both cards
	elif card_1_ace == True and card_2_ace == True: # both are aces - very rare
		total = 12
	elif card_1_ace == True: # card 1 is an Ace
		total += DECK_DICT[user_list[0]['current_hand'][0]]['value'][1] + DECK_DICT[user_list[0]['current_hand'][1]]['value'][0] # sum of both cards (where first is Ace = 11)
	elif card_2_ace == True: # card 2 is an Ace
		total += DECK_DICT[user_list[0]['current_hand'][0]]['value'][0] + DECK_DICT[user_list[0]['current_hand'][1]]['value'][1] # sum of both cards (where second is Ace = 11)

	return total, card_1_ace, card_2_ace

def check_if_ace(card):
	if len(DECK_DICT[card]['value']) == 2:
		return True
	else:
		return False

def less_than_17(user_list, deck, total, card_1_ace, card_2_ace):
	if (card_1_ace == False and card_2_ace == False) or (card_1_ace == True and card_2_ace == True): # make sure no Aces or both aces
		soft_card = False
		while True:
			curr_card = deck.pop() # take card from deck
			user_list[0]['current_hand'].append(curr_card) # add to dealer's current hand
			temp_total = total + DECK_DICT[curr_card]['value'][0]
			
			if check_if_ace(curr_card) and total < 11 and total != 6: # if new card is an ace and total is less than 11 but not soft 17
				total += 11
				soft_card = True
			elif check_if_ace(curr_card) and total >= 11: # if new card is an ace and total is >= 11
				total += 1
			elif check_if_ace(curr_card) and total == 6: # soft 17
				total = 7
				total = soft_17(user_list, deck, total)
			elif soft_card == True and temp_total >= 22:
				total = temp_total - 10
				soft_card = False
			else:
				total += DECK_DICT[curr_card]['value'][0]

			print(print_dealer_cards(running_total=total)) # print dealer cards after getting next card

			if total >= 17:
				break
		return total
	else:	# if ace exists in ONE of dealer's first two cards
		soft_card = True # assume it is a 'soft hand' (since it is either A2, A3, A4, or A5)
		while True:
			curr_card = deck.pop() # take card from deck
			user_list[0]['current_hand'].append(curr_card) # add to dealer's current hand
			curr_card_value = DECK_DICT[curr_card]['value'][0] # Ace will always = 1 in this case
			temp_total = total + curr_card_value

			if temp_total >= 22 and soft_card: # check if dealer busts with soft hand
				total = temp_total - 10 # we previously assumed Ace is 11, this brings it back down by 10 so A = 1
				soft_card = False
			elif temp_total >= 22 and soft_card == False: # dealer busts
				total = temp_total
			elif temp_total <= 21  and temp_total != 17: # if we have a card that doesnt bust or equal 17
				total = temp_total
			elif temp_total == 17 and soft_card: # we have a soft 17 (rare)
				total = 7
				total = soft_17(user_list, deck, total)
			else: # temp_total is 17 and it is a hard 17
				total = temp_total
			print(print_dealer_cards(running_total=total)) # print dealer cards after getting next card

			if total >= 17:
				break
		return total

def soft_17(user_list, deck, total): # note that total always = 7 at start
	first_round = True
	while total < 17:
		curr_card = deck.pop()
		user_list[0]['current_hand'].append(curr_card)
		curr_card_value = DECK_DICT[curr_card]['value'][0]

		if curr_card_value in [1, 2, 3, 4] and first_round: # since soft 17 is either 7 or 17, this will make 18 to 21 only in first round
			total = 17 + curr_card_value # started off with total = 7, change back to 17
		else:
			first_round = False
			total += curr_card_value
		print(print_dealer_cards) # print dealer cards after getting next card
	return total

def dealer_cards_check_total(user_list, deck):
	"""This will see if total is soft 17, >= hard 17, or less than 17 """
	total, card_1_ace, card_2_ace = get_dealer_two_card_sum(user_list, deck) # getting sum of first 2 cards in dealer's hand
	print(print_dealer_cards(running_total=total)) # Initial print out of dealer's 2 cards
	if total > 17 :
		return total
	elif total < 17:
		return less_than_17(user_list, deck, total, card_1_ace, card_2_ace)
	elif total == 17 and card_1_ace == False and card_2_ace == False: # total is hard 17
		return total
	else: # soft 17
		total = 7
		return soft_17(user_list, deck, total)



## dealer_cards_check_total is the main function here.

def print_dealer_cards(running_total, user_list=user_list):
	""" Print the dealer's current hand"""
	print('Dealer\'s Hand:\n-----------\n') # header
	for card in user_list[0]['current_hand']:
		print(DECK_DICT[card]['card'])
	print('\n\tTotal: ', running_total)



dealer_cards_check_total(user_list, deck)

dealer_final_total = dealer_cards_check_total(user_list, deck)

## OUTCOMES ###
player_final_total = 17
print('FINAL OUTCOME\n-----------')
if dealer_final_total > 21:
	print('Dealer busts! You win.')
elif dealer_final_total < player_final_total:
	print('You win!\n\nDealer: {}\n{}: {}'.format(dealer_final_total, user_list[1]['name'], player_final_total))
elif dealer_final_total > player_final_total:
	print('You lose!\n\nDealer: {}\n{}: {}'.format(dealer_final_total, user_list[1]['name'], player_final_total))
elif dealer_final_total == player_final_total:
	print('Push!\n\nDealer: {}\n{}: {}'.format(dealer_final_total, user_list[1]['name'], player_final_total))
