from init import * # Imports code from the init.py file

# Create all of the cards		
annie_conda = Card('Annie Conda', 'python', 'java', 'bash', annie_conda_img, icon_python)
bayo_wolf = Card('Bayo Wolf', 'scratch', 'small_basic', 'java', bayo_wolf_img, icon_scratch)
captain_javo = Card('Captain Javo', 'java', 'scratch', 'python', captain_javo_img, icon_java)
cryptic_creeper = Card('Cryptic Creeper', 'bash', 'python', 'small_basic', cryptic_creeper_img, icon_bash)
emily_airheart = Card('Emily Airheart', 'small_basic', 'bash', 'scratch', emily_airheart_img, icon_small_basic)
grafika_turtle = Card('Grafika Turtle', 'small_basic', 'bash', 'scratch', grafika_turtle_img, icon_small_basic)
intelli_scents = Card('Intelli-Scents', 'scratch', 'small_basic', 'java', intelli_scents_img, icon_scratch)
java_lynn = Card('Java Lynn', 'java', 'scratch', 'python', java_lynn_img, icon_java)
jitter_bug = Card('Jitter Bug', 'java', 'scratch', 'python', jitter_bug_img, icon_java)
justin_timbersnake = Card('Justin Timbersnake', 'python', 'java', 'bash', justin_timbersnake_img, icon_python)
mrs_scratcher = Card('Mrs. Scratcher', 'scratch', 'small_basic', 'java', mrs_scratcher_img, icon_scratch)
paul_python = Card('Paul Python', 'python', 'java', 'bash', paul_python_img, icon_python)
queen_cobra = Card('Queen Cobra', 'python', 'java', 'bash', queen_cobra_img, icon_python)
ram_rom = Card('Ram Rom', 'java', 'scratch', 'python', ram_rom_img, icon_java)
sidewinder = Card('Sidewinder', 'python', 'java', 'bash', sidewinder_img, icon_python)
syntax_turtle = Card('Syntax Turtle', 'small_basic', 'bash', 'scratch', syntax_turtle_img, icon_small_basic)
viralmuto = Card('Viralmuto', 'bash', 'python', 'scratch', viralmuto_img, icon_bash)
virobotica = Card('Virobotica', 'bash', 'python', 'small_basic', virobotica_img, icon_bash)
# Copied the code here to add the Virobots and Woodchuck Norris cards
virobots = Card('Virobots', 'bash', 'python', 'small_basic', virobots_img, icon_bash)
woodchuck_norris = Card('Woodchuck Norris', 'scratch', 'small_basic', 'java', woodchuck_norris_img, icon_scratch)

DECK = []

# Add all cards to deck
DECK.append(annie_conda)
DECK.append(bayo_wolf)
DECK.append(captain_javo)
DECK.append(cryptic_creeper)
DECK.append(emily_airheart)
DECK.append(grafika_turtle)
DECK.append(intelli_scents)
DECK.append(java_lynn)
DECK.append(jitter_bug)
DECK.append(justin_timbersnake)
DECK.append(mrs_scratcher)
DECK.append(paul_python)
DECK.append(queen_cobra)
DECK.append(ram_rom)
DECK.append(sidewinder)
DECK.append(syntax_turtle)
DECK.append(viralmuto)
DECK.append(virobotica)
DECK.append(virobots)
DECK.append(woodchuck_norris)

# Copied the code here to shuffle the cards
random.shuffle(DECK)

class PlayScreen(GameState):
	
	def __init__(self):
		super().__init__()
		self.next_state = "Victory"

		self.tech_attack_button = Button("TechType Attack", X_CENTER-105, 575, 210, 40, ondeck_teal, round_dark_blue, parent = self)		
		self.instructions_box = InfoBox(INSTRUCTIONS, dialog_inst, BLACK, (200, 300), (X_CENTER, 200), 200)

		self.coin = Coin(coin_img, (X_CENTER, 475))
		self.turn_counter = 1
		self.flipping = False
		self.attacking = False
		self.side_up = None
		
	def start(self, players):
		self.players = players
		self.player1 = players["player1"]
		self.player2 = players["player2"]
		
		self.attacker = self.player1 if self.player1.active_turn else self.player2
		self.defender = self.player1 if not self.player1.active_turn else self.player2
		
		self.player1_card_display = CardDisplay(self.player1, player1_card_display_data)
		self.player2_card_display = CardDisplay(self.player2, player2_card_display_data)

		self.player1_healthbar = Healthbar(self.player1, player1_healthbar_data)
		self.player2_healthbar = Healthbar(self.player2, player2_healthbar_data)
		
		self.player1_ondeck = OnDeck(self.player1, player1_ondeck_data)
		self.player2_ondeck = OnDeck(self.player2, player2_ondeck_data)

		self.dialog_box = DialogBox((200,300), (X_CENTER-100, 50))
		
	def get_event(self, event):
		if not self.flipping:
			# Added the code that checks if the player clicked the TechType Attack button
			self.tech_attack_button.get_event(event)
	
		# Added the code here to check if the players click an On Deck card
		self.player1_ondeck.get_event(event)
		self.player2_ondeck.get_event(event)
		
	def button_action(self, params):
		# Wrote the code here to flip the coin when the player clicks the button
		self.side_up = self.flip_coin()
		self.coin.set_side(self.side_up)
		self.flipping = True
				
	def update(self, dt):
		# Wrote the code here to update the healthbars, decks, and cards
		self.player1_healthbar.update()
		self.player2_healthbar.update()
		
		self.player1_ondeck.update()
		self.player2_ondeck.update()
		
		self.player1_card_display.update()
		self.player2_card_display.update()
		
		# Copied the code that checks if the player clicked the button
		if self.flipping:
			self.flipping = self.coin.update(dt)
			if not self.flipping:
				self.attacking = True
		
		if self.attacking:
			# Wrote the code for choosing the attacker and defender cards
			offense_card = self.attacker.current_card 
			defense_card = self.defender.current_card
			
			# This code creates and adds the turn's message
			message = add_to_message("", "{}".format(self.turn_counter))
			message = add_to_message(message, "{}".format(self.attacker.name))
			message = add_to_message(message, "{}".format(self.side_up))

			if self.side_up == 'Heads':
				damage = defense_card.attacked_by(offense_card)
				if damage == 2:
					turn_msg = "{} is resistant to {}'{} attack! They only take 2 damage.".format(defense_card.name, offense_card.name, offense_card.s_flag)
				elif damage == 4:
					turn_msg = "{} is weak to {}'{} attack! They receive 4 damage.".format(defense_card.name, offense_card.name, offense_card.s_flag)
				else:
					turn_msg = "{} took {} damage from {}'{} attack.".format(defense_card.name, damage, offense_card.name, offense_card.s_flag)
				message = add_to_message(message, turn_msg, defense_card)
			else:
				turn_msg = "{} took no damage from {}.".format(defense_card.name, offense_card.name)
				message = add_to_message(message, turn_msg)
			
			# Dialog box shows the result of the turn
			self.dialog_box.set_message(message)
			
			# Update player hands
			self.player1.refresh_hand()
			self.player2.refresh_hand()
			
			self.attacking = False
			self.turn_counter += 1
					
			# Switch active player
			self.switch_active_player()
		
			winner = self.check_game_end()
			if winner:
				winner.set_as_winner()
				self.done = True
			
	def flip_coin(self):
		side = "Heads" if random.random() < 0.5 else "Tails"
		return side

	def switch_active_player(self):
		if self.player1.active_turn:
			self.attacker = self.player2
			self.defender = self.player1
		else:
			self.attacker = self.player1
			self.defender = self.player2
		
		self.attacker.active_turn = True
		self.defender.active_turn = False

	def check_game_end(self):
		# Check status of both players, if one player surviving then end the game
		exiting = False
		if not self.player1.active:
			exiting = self.player2
		elif not self.player2.active:
			exiting = self.player1
		return exiting
		
	def draw(self, surface):
		super().draw(surface)
		
		if self.turn_counter == 1:
			self.instructions_box.draw(surface)
		self.dialog_box.draw(surface)
		
		self.player1_card_display.draw(surface)
		self.player2_card_display.draw(surface)
		
		self.player1_healthbar.draw(surface)
		self.player2_healthbar.draw(surface)
		
		self.player1_ondeck.draw(surface)
		self.player2_ondeck.draw(surface)
		
		self.coin.draw(surface)
		self.tech_attack_button.draw(surface)

states = {
		"Title" : TitleScreen(),
		"GetNames": GetNameScreen(),
		"CoinFlip": CoinFlipScreen(),
		"ChooseHand" : ChooseHandScreen(DECK),
		"Game" : PlayScreen(),
		"Victory" : VictoryScreen()
			}

game = GameRunner(SCREEN, states, "Title")

