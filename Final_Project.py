import random
from time import sleep

## This is how we initially created the deck ##
"""
CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"
suits = ['\u2663', '\u2665', '\u2666', '\u2660']*13
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
trial_deck = {}
for i in range(1, 53):
	trial_deck[i] = {
						'card': values[i-1] + ' ' + suits[i-1],
						'actual_value': []
					}
"""

# Dictionary for a deck of 52 cards
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

class Player(object):
	"""Create a player with attributes and methods for player centered gameplay.

	Has attributes for player's current hand and overall balance.  Has methods
	for showing a hand or balance, getting a bet, drawing cards, checking for
	aces in a  hand, computing the value of the current hand, doubling
	the bet, updating the running balance, and resetting the attributesself.

	"""
	player_hand = []
	hand_value = 0
	ace_value = 0
	has_ace = False
	busted = False
	hand_won = None
	balance = 1000
	bet = 0

	def __init__(self, name):
		"""Initialize Player class. Takes parameter 'name'."""
		self.name = name

	def show_balance(self):
		"""Print the current balance."""
		print("\n{} currently has ${}.".format(self.name, self.balance))

	def show_hand(self):
		"""Print the player current hand."""
		to_print = []
		for i in range(len(player_1.player_hand)):
			to_print.append(player_1.player_hand[i][0])
		print(player_1.name + ": [" + "]  [".join(to_print) + "]")

	def get_wager(self):
		"""Get a bet input and add to bet."""
		while True:
			try:
				wager = int(input("\nHow much would you like to bet?" + \
				"(Minimum is $10)." + "\n" + "Bet: $ "))
				if wager < 10:
					print("\n" + "The minimum bet is $10.  Please try again..." \
					+ "\n")
					sleep(1)
				elif wager > self.balance:
					print("\n" + "You cannot bet more money than you have!" + \
					" You bet ${}, but you only have ${}.".format(wager, self.balance) + \
					" Please try again..." + "\n")
					sleep(1)
				else:
					self.bet += wager
					print("\n" + ("=" * 32) + "\n" + \
						"Your bet for this hand is ${}.".format(self.bet) + \
						"\n" + ("=" * 32) + "\n")
					break
			except:
				print("\n" + "Your bet must be an integar number." + \
				"Please try again..." + "\n")
				sleep(1)

	def get_card(self):
		"""Get a card and append to hand."""
		card_key = shuffled_cards.give_one_card()
		hand_card = [DECK_DICT[card_key]["card"], DECK_DICT[card_key]["value"]]
		self.player_hand.append(hand_card)

	def check_if_ace(self):
		"""Check last card in hand for ace and set has_ace."""
		if self.player_hand[len(self.player_hand)-1][0][0] == "A":
			self.has_ace = True

	def set_hand_values(self):
		"""Add card value to hand value and ace value if ace is in hand."""
		if self.has_ace == True:
			self.hand_value += self.player_hand[len(self.player_hand)-1][1][0]
			self.ace_value = self.hand_value + 10
		else:
			self.hand_value += self.player_hand[len(self.player_hand)-1][1][0]

	def double_down_bet(self):
		"""Double player bet."""
		self.bet = int(self.bet * 2)
		return self.bet

	def update_balance(self):
		"""Update running balance."""
		if self.busted == True or self.hand_won	== False:
			self.balance -= self.bet
		elif self.hand_won == True:
			self.balance += self.bet

	def reset_player_attr(self):
		"""Reset attributes except balance."""
		self.player_hand = []
		self.hand_value = 0
		self.ace_value = 0
		self.has_ace = False
		self.bet = 0
		self.hand_won = None
		self.busted = False

class Card_Deck(object):
	"""Create a deck of cards to be used by players and dealerself.

	Create new deck as list of integars, shuffle deck list, remove card from
	deck list and return.

	"""
	deck = []

	def new_deck(self):
		"""Create a new card deck list with 6 standard card decks."""
		self.deck = [x for x in range(1,53)] * 6

	def shuffle(self):
		"""Shuffle the deck list."""
		random.shuffle(self.deck)

	def give_one_card(self):
		"""Remove card from deck list and return."""
		card = self.deck.pop()
		return card

class Dealer():
	"""Create the dealer in Blackjack."""
	dealer_cards = []

	def dealer_get_initial_cards(self):
		"""Get dealer's initial two cards."""
		first_card = shuffled_cards.give_one_card()
		second_card = shuffled_cards.give_one_card()
		self.dealer_cards.append(first_card)
		self.dealer_cards.append(second_card)

	def get_dealer_face_up_card(self):
		"""Print out only the first of dealer's cards."""
		print('Dealer:\t', "[", DECK_DICT[self.dealer_cards[0]]['card'], "]")

	def get_dealer_two_card_sum(self):
		"""Get sum of dealer's two cards, and return their total along with
		True or False value for aces."""
		total = 0
		card_1_ace = dealer.check_if_ace(self.dealer_cards[0])
		card_2_ace = dealer.check_if_ace(self.dealer_cards[1])
		if card_1_ace == False and card_2_ace == False: # neither is an ace
			total += DECK_DICT[self.dealer_cards[0]]['value'][0] + DECK_DICT[self.dealer_cards[1]]['value'][0] # sum of both cards
		elif card_1_ace == True and card_2_ace == True: # both are aces - very rare
			total = 12
		elif card_1_ace == True: # card 1 is an Ace
			total += DECK_DICT[self.dealer_cards[0]]['value'][1] + DECK_DICT[self.dealer_cards[1]]['value'][0] # sum of both cards (where first is Ace = 11)
		elif card_2_ace == True: # card 2 is an Ace
			total += DECK_DICT[self.dealer_cards[0]]['value'][0] + DECK_DICT[self.dealer_cards[1]]['value'][1] # sum of both cards (where second is Ace = 11)
		return total, card_1_ace, card_2_ace

	def check_if_ace(self, card):
		"""Check if card is an Ace."""
		if len(DECK_DICT[card]['value']) == 2:
			return True
		else:
			return False


	def less_than_18(self, total, card_1_ace, card_2_ace):
		"""Direct dealer actions if card is a soft 17 or less."""
		if (card_1_ace == False and card_2_ace == False): # make sure no Aces
			soft_card = False
			while True:
				curr_card = shuffled_cards.give_one_card() # take card from deck
				self.dealer_cards.append(curr_card) # add to dealer's current hand
				temp_total = total + DECK_DICT[curr_card]['value'][0]

				if dealer.check_if_ace(curr_card) and total < 11: # if new card is an ace and total is less than 11
					total += 11 # ace is 11, we have a soft hand
					soft_card = True
				elif dealer.check_if_ace(curr_card) and total >= 11: # if new card is an ace and total is >= 11
					total += 1 # ace can only be 1, otherwise dealer busts
				elif soft_card == True and temp_total >= 22: # 'busted' w/ soft hand;  not real bust
					total = temp_total - 10
					soft_card = False
				else:
					total += DECK_DICT[curr_card]['value'][0]

				dealer.print_dealer_cards(running_total=total, turn=False) # print dealer cards after getting next card

				if total >= 17:
					break
			return total
		else:	# if ace exists in one/both of dealer's first two cards
			soft_card = True # assume it is a 'soft hand' (since it is either AA, A2, A3, A4, A5, A6)
			while True:
				curr_card = shuffled_cards.give_one_card() # take card from deck
				self.dealer_cards.append(curr_card) # add to dealer's current hand
				curr_card_value = DECK_DICT[curr_card]['value'][0] # Ace will always = 1 in this case
				temp_total = total + curr_card_value

				if temp_total >= 22 and soft_card: # check if dealer busts with soft hand
					total = temp_total - 10 # we previously assumed Ace is 11, this brings it back down by 10 so A = 1
					soft_card = False
				elif temp_total >= 22 and soft_card == False: # dealer busts
					total = temp_total
				else:
					total = temp_total

				dealer.print_dealer_cards(turn = False, running_total=total) # print dealer cards after getting next card

				if total >= 17:
					break
			return total


	def dealer_cards_check_total(self):
		"""Check if total is hard 17, > hard 17, or less than 18."""
		total, card_1_ace, card_2_ace = dealer.get_dealer_two_card_sum() # getting sum of first 2 cards in dealer's hand
		dealer.print_dealer_cards(running_total=total, turn = True) # Initial print out of dealer's 2 cards
		if total > 17 :
			return total
		elif total == 17 and card_1_ace == False and card_2_ace == False: # total is hard 17
			return total
		elif total <= 17: # soft 17 or less
			return dealer.less_than_18(total, card_1_ace, card_2_ace)


	def print_dealer_cards(self, running_total, turn):
		"""Print the dealer's current hand."""
		if turn == True:
			print('\nDealer\'s Hand:\n-----------\n') # header
			for card in self.dealer_cards:
				print("[", DECK_DICT[card]['card'], "]")
				turn = False
				sleep(0.5)
			print('Calculating...')
			sleep(0.5)
			print('\n\tTotal: ', running_total)
			sleep(0.5)
		else:
			print("[", DECK_DICT[self.dealer_cards[-1]]['card'], "]")
			sleep(0.5)
			print('Calculating...')
			sleep(0.5)
			print('\n\tTotal: ', running_total)
			sleep(0.5)

	def dealer_reset_attr(self):
		self.dealer_cards = []

	def dealer_blackjack(self):
		total = 0
		for card in self.dealer_cards:
			ace = self.check_if_ace(card)
			if ace:
				total += 11
			else:
				total += DECK_DICT[card]['value'][0]
		return total

# Get a player name
def get_player_name():
	while True:
		user_name = input("\nPlease enter your name: ")
		if not user_name:
			print("You must enter a name to play.  Please try again...")
			sleep(1)
		else:
			return user_name
			break

# Give player one card and print value of hand if player doubles down
def double_down():
	player_1.get_card()
	player_1.check_if_ace()
	player_1.set_hand_values()
	player_1.show_hand()

	if player_1.has_ace:
		print('\nTotal: {} '.format(player_1.ace_value))
	else:
		print('\nTotal: {} '.format(player_1.hand_value))

# Get final outcome
def get_outcome(dealer_final_total, player_final_total):
	print('\n', '='*15, '\n  FINAL OUTCOME\n', '='*15)
	sleep(1)
	if dealer_final_total > 21:
		print('Dealer busts! You win.')
		player_1.hand_won = True
	elif dealer_final_total < player_final_total:
		print('You win!\n\nDealer: {}\n{}: {}'.format(dealer_final_total, player_1.name, player_final_total))
		player_1.hand_won = True
	elif dealer_final_total > player_final_total:
		print('You lose!\n\nDealer: {}\n{}: {}'.format(dealer_final_total, player_1.name, player_final_total))
		player_1.hand_won = False
	elif dealer_final_total == player_final_total:
		print('Push!\n\nDealer: {}\n{}: {}'.format(dealer_final_total, player_1.name, player_final_total))

# Instructions for gameplay
rules = """
			Instructions:
			The point of the game is to beat the dealer's hand without
			going over 21. You will be dealt 2 cards, as will the dealer
			but only one of the dealer's cards will be shown. You can choose
			to stand (s) - stop being dealt cards, or hit (h) - continue
			to be dealth cards. All face cards are worth 10, an Ace can be
			either 1 or 11.
			The Dealer must continue to take cards until they are at a hard 17
			or above (Please Note: Ace + 6 = Soft 17, dealer must hit).

			Betting:
			You start off with $1000 and minimum bet is $10. If you have an
			initial hand of 10 or 11, you have the option to 'double down (d)',
			doubling your current bet, and receiving only 1 more card.
			If you win against the dealer, you double your money; lose, you lose
			your money, and tie (aka 'push') - keep your money.
			Blackjack pays 3 to 2.
			"""

logo = """
888888b.   888                   888       d8b                   888
888  "88b  888                   888       Y8P                   888
888  .88P  888                   888                             888
8888888K.  888  8888b.   .d8888b 888  888 8888  8888b.   .d8888b 888  888
888  "Y88b 888     "88b d88P"    888 .88P "888     "88b d88P"    888 .88P
888    888 888 .d888888 888      888888K   888 .d888888 888      888888K
888   d88P 888 888  888 Y88b.    888 "88b  888 888  888 Y88b.    888 "88b
8888888P"  888 "Y888888  "Y8888P 888  888  888 "Y888888  "Y8888P 888  888
                                           888
                                          d88P
                                        888P"
"""

# Create an instance of Card_Deck()
shuffled_cards = Card_Deck()

# Create instance of Dealer()
dealer =  Dealer()

print("\nWelcome to...\n")
sleep(1)
print(logo)
sleep(2)
print("\n", rules)
sleep(1)

# Get the player's name and assign to Player class object
player_1 = Player(get_player_name())

blackjack_running = True

### START OF GAME/WHILE LOOP ###
while blackjack_running == True:

	# Get new deck and shuffle
	shuffled_cards.new_deck()
	shuffled_cards.shuffle()

	# Get the player's bet
	player_1.get_wager()

	# Deal a card to the player, check for ace,
	# increment value of hand, repeat for 2nd card
	player_1.get_card()
	player_1.check_if_ace()
	player_1.set_hand_values()
	player_1.get_card()
	player_1.check_if_ace()
	player_1.set_hand_values()
	sleep(1)

	#Show the player's hand and current hand value:
	player_1.show_hand()

	if player_1.has_ace:
		print('Total: {} or {}\n'.format(player_1.hand_value, player_1.ace_value))
	else:
		print('Total: {}\n'.format(player_1.hand_value))
	sleep(1)

	# Deal cards to dealer, and show dealer's first card
	dealer.dealer_get_initial_cards()
	dealer.get_dealer_face_up_card()
	sleep(1)

	# Set variables for first turn blackjack
	turn_1 = True
	player_blackjack = False
	dealer_21 = False

	# Check for blackjack first turn
	while True:
		if player_1.ace_value == 21 and turn_1:
			print('\n\nBLACKJACK! \n', player_1.ace_value)
			player_final_total = player_1.ace_value
			player_blackjack = True
			sleep(1)
			break
		if dealer.dealer_blackjack() == 21:
			dealer_21 = True
			break

		# Get user input for gameplay: hit, stand or double down
		if (player_1.hand_value == 10 or player_1.hand_value == 11) and turn_1 and (player_1.bet*2) < player_1.balance:
			hs_input = input('\nWould you like to hit (h), stand (s), or double down (d)?\n' )
		else:
			hs_input = input('\nWould you like to hit (h) or stand (s)?\n')

		if hs_input.lower() in ['d', 'dd', 'double', 'double down'] and turn_1:
			player_1.double_down_bet()
			double_down()
			if player_1.has_ace:
				player_final_total = player_1.ace_value
			else:
				player_final_total = player_1.hand_value
				turn_1 = False
			break

		if hs_input.lower() in ['s', 'stand']:
			if player_1.ace_value > 21 or player_1.has_ace == False:
				player_final_total = player_1.hand_value
			else:
				player_final_total = player_1.ace_value
			break
		elif hs_input.lower() in ['h', 'hit']:
			player_1.get_card()
			player_1.check_if_ace()
			player_1.set_hand_values()
			player_1.show_hand()
			turn_1 = False
			sleep(1)

			if player_1.ace_value > 21 and player_1.hand_value <= 21:
				print('Total: ', player_1.hand_value)
			elif player_1.hand_value > 21:
				print('Total: ', player_1.hand_value)
				sleep(1)
				print('You busted!\n')
				sleep(1)
				player_final_total = player_1.hand_value
				player_1.busted = True
				break
			elif player_1.ace_value <= 21 and player_1.has_ace:
				print('Total: {} or {}'.format(player_1.hand_value, player_1.ace_value))
				sleep(1)
			else:
				print('Total: ', player_1.hand_value)
				sleep(1)

		else:
			sleep(1)
			print('Please only enter hit (h) or stand (s)')
			sleep(1)
			continue

	if player_blackjack == True:
		print("\nDealer's cards: [", DECK_DICT[dealer.dealer_cards[0]]['card'],"]",
								"[", DECK_DICT[dealer.dealer_cards[1]]['card'],"]")
		player_1.hand_won = True
		player_1.bet *= 1.5
	elif dealer_21 == True:
		print("\nDealer has Blackjack! Sorry!")
		sleep(1)
		print("\nDealer's cards: [", DECK_DICT[dealer.dealer_cards[0]]['card'],"]",
								"[", DECK_DICT[dealer.dealer_cards[1]]['card'],"]")
		player_1.hand_won = False
	elif player_1.busted == False:
		dealer_final_total= dealer.dealer_cards_check_total()
		get_outcome(dealer_final_total, player_final_total)
	else:
		print("\nDealer's cards: [", DECK_DICT[dealer.dealer_cards[0]]['card'], "]"
								"[", DECK_DICT[dealer.dealer_cards[1]]['card'], "]")

	# Adjust player balance
	player_1.update_balance()
	player_1.show_balance()

	# Reset player and dealer attributes
	player_1.reset_player_attr()
	dealer.dealer_reset_attr()

	# Ask if player would like to play again
	while True:
		if player_1.balance < 10:
			print("\nYour balance is ", player_1.balance, \
			" dollars which is below the minimum bet." + \
			"You do not have enough money to play again. Goodbye!")
			blackjack_running = False
			break

		play_again = input("\nWould you like to play again (yes/no)?")
		if play_again.lower() in ["y", "yes"]:
			sleep(.5)
			print("\nDealing new hand...\n\n")
			sleep(1)
			break
		elif play_again.lower() in ["n", "no"]:
			print("\nThanks for playing!")
			blackjack_running = False
			break
		else:
			print("\nPlease only enter 'yes' or 'no'\n")
			sleep(1)
