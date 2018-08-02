import random

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
deck = [2, 37, 28, 47, 6, 35, 22, 44, 29, 24, 51, 23, 13, 20, 14, 48, 43, 18, 32, 7, 10, 41, 1, 19, 30, 11, 52, 5, 25, 34, 50, 12, 45, 46, 36, 8, 27, 15, 40, 16, 26, 39, 17, 3, 38, 33, 21, 31, 9, 42, 4, 49]

user_list = [
			{
			'name': 'dealer',
			'current_hand': []
			},
			{
			'name': 'vidya',
			'current_hand': [],
			'total_money': 1000,
			'current_bet': 0
			}


]

#code



def check_if_ace(card):
	if len(DECK_DICT[card]['value']) == 2:
		return True
	else:
		return False

def shuffle_deck(deck):
	shuffled_list = []
	for key in deck.keys():
		shuffled_list.append(key)
	random.shuffle(shuffled_list)
	return shuffled_list


def deal_card(deck, user):
	current_card = deck.pop()
	return current_card

def tally(user):
	total = []
	card1 = check_if_ace(user_list[1]['current_hand'][0])
	card2 = check_if_ace(user_list[1]['current_hand'][1])
	if card1 == False and card2 == False:
		total.append(DECK_DICT[user_list[1]['current_hand'][0]]['value'][0]+DECK_DICT[user_list[1]['current_hand'][1]]['value'][0]) #make two values anyway
		total.append(DECK_DICT[user_list[1]['current_hand'][0]]['value'][0]+DECK_DICT[user_list[1]['current_hand'][1]]['value'][0])
	elif card1 and card2:
		total = [2,12]
	elif card1:
		total = [(DECK_DICT[user_list[1]['current_hand'][1]]['value'][0]+1),(DECK_DICT[user_list[1]['current_hand'][1]]['value'][0]+11)]
	elif card2:
		total = [(DECK_DICT[user_list[1]['current_hand'][0]]['value'][0]+1),(DECK_DICT[user_list[1]['current_hand'][0]]['value'][0]+11)]
	if len(user_list[1]['current_hand'])==2:
		if total[0] == total[1]:
			print("tally: ", total[0])
		elif total[0]<total[1]:
			print("your tally can be ",total[0], " or ", total[1])
	if len(user_list[1]['current_hand'])>2:  #if more cards have been added
		for c in new_cards:
			if check_if_ace(c)==False:       #if the new card is NOT an ace
				total[1]+= DECK_DICT[c]['value'][0]
				total[0]+= DECK_DICT[c]['value'][0]
			elif check_if_ace(c):            #if it IS an ace:
				if card1 or card2:           #need to check if any other card is an ace
					total[0]+= 1             #need to add corresponding ace values
					total[1]+= 1
				else:
					total[0]+=1
					total[1]+=11
	try:
		if total[0] > 21:
			print('bust!')
	except:
		if total[1] >21:
			print("can't use this tally: ", total[1])
	print('tally:' ,total)
	return total

def blackjack(user):
    if len(user_list[1]['current_hand'])==2:
        if tally(user)==21:
            return True
    else:
        False

def print_hand(user):
    for x in user_list[1]['current_hand']:
        print('your cards: ', DECK_DICT[x]['card'])
    return user_list[1]['current_hand']

def hit(deck,user):
		new_card = deal_card(deck, user_list[1])
		user_list[1]['current_hand'].append(new_card)
		return new_card

new_cards= []
deck = shuffle_deck(DECK_DICT) # deck is a list of shuffled numbers
								#correlating to values in DECK_DICT
print (deck)

#deal cards to user
user_list[1]['current_hand'].append(deal_card(deck,user_list[1]))
user_list[1]['current_hand'].append(deal_card(deck,user_list[1]))
print('first hand: ',user_list[1]['current_hand'])
print('your hand: ', DECK_DICT[user_list[1]['current_hand'][0]]['card'], DECK_DICT[user_list[1]['current_hand'][1]]['card'])
tally(user_list[1])

#check if blackjack
blackjack(user_list[1])

#dealer cards
(user_list[0]['current_hand']).append(deal_card(deck,user_list[1]))
(user_list[0]['current_hand']).append(deal_card(deck,user_list[1]))
#get_dealer_face_up_card(user_list[0], deck)




while True:

	#check if blackjack
	if blackjack(user_list[1]):
		print('blackjack!')
		break
	hs_input = input('Would you like to hit (h) or stand (s)?' )
	if hs_input.lower() in ['s', 'stand']:
		# Function for standing
		# player cards tally
		tally(user_list[1])
		break
	elif hs_input.lower() in ['h', 'hit']:
			#new_cards= []
			new_cards.append(hit(deck,user_list[1]))
			for x in (user_list[1]['current_hand']):
				print('your cards now: ', DECK_DICT[x]['card'])
			#print('new tally: ', tally(user_list[1]))
			if tally(user_list[1])[0]>21:
				print(tally(user_list[1])[1])
			if tally(user_list[1])[1]>21:
				print(tally(user_list[1])[0])
			if tally(user_list[1])[1]>21 and tally(user_list[1])[0]>21:
				#call dealer
				print('you lost!')
				break
			#print('card: ', DECK_DICT[hit()]['value'])
			print(user_list[1]['current_hand'])
			continue
	else:
		print('Please only put hit (h) or stand (s)')
		continue
	print(deck)

	play_again = input('Would you like to play again (yes/no)? ')
	if play_again == 'y' or play_again == 'yes':
		continue
	else:
		print('Thanks for playing!')
		break
