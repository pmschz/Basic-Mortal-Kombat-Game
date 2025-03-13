# Mortal Kombat basic game

############################## NEW CLASS #####################################
# Keeps track of attack moves, character, enhancement, and final_kill move    
class Character:

  def __init__(self, player_num):
    self.character_list = ['Kitana', 'Frost', 'Shao Kahn', 'Scorpion', 'Spawn', 'Kano', 'Noob Saibot', 'Skarlet', 'Geras']
    ### moves damage 7, 9, 14 in order of list index 0, 1, 2
    self.attack_moves = {'Kitana': ['Fan Out', 'Low Slice', 'Full Slice', 'Back Throw'], 'Frost': ['Headbutt', 'Blade Lunge', 'Ice Spike', 'Frosted Uppercut'],'Shao Kahn': ['Dragon Toe', 'Hammer Slammer', 'Deadly Swipe', 'Rising Wrath'], 'Scorpion': ['Dark Soul', 'Flip Kick', 'Spear Slice', 'Rising Spear'],'Spawn': ['Shroud Strike', 'War Devil', 'Reflections', 'Rising Cape'], 'Kano': ['Blade Evade', 'Outback Bash', 'Kangaroo Kick', 'Black Dragon Bash'],'Noob Saibot': ['Shadow Sclice', 'Sickle Swipe', 'Wraith Kick', 'Rising Sickle'], 'Skarlet':['Whip Snap', 'Scythe Slam', 'Side Slice', 'Kutter'],'Geras':['Strong Step', 'Chrono Kick', 'Titan Toe', 'Rising Gauntlet']}
    self.character = ''
    self.final_kill_move = ''
    self.enhancement = ''
    self.final_kill_move_dict = {'Kitana': ['Gore Nado', 'Royal Execution'], 'Frost': ['Ice Sculpture', 'The Cyber Initiative'],'Shao Kahn': ['YOU SUCK', 'Head Kabob'],'Scorpion': ['Get Over Here', 'Ashes'], 'Spawn': ['Rest in Peices', 'Unchained'],'Kano': ['NOT HERE TO F#CK SPIDERS', 'Look what I found'],'Noob Saibot': ['Decapper', 'Together Again'], 'Skarlet': ['Bloody Fun', 'Gutted'], 'Geras': ['Stasis Assault', 'Pulled Apart']}
    self.player_num = player_num

# Allows user to select character from a list of available characters and will remove that character after chosen
  def choose_character(self):
    num = 1
    for character in player1.character_list:
      print(str(num) + ' ' + character)
      num += 1
    choice = int(input('Select a number for a player and press enter to select.\n')) - 1
    while choice not in range(0, 9):
        choice = int(input('Please enter a value 1-5\n')) - 1 
    character = self.character_list[choice]
    self.character = character
## Allows player to choose their final kill move
  def choose_final_kill(self):
    if self.character in self.final_kill_move_dict:
      final_kill_options = self.final_kill_move_dict.get(self.character)
      num = 1
      for move in final_kill_options:
        print(str(num) + ' ' + move) 
        num += 1
      choice = int(input('Type corresponding number for final kill choice.\n')) - 1
      while choice not in range(0,2):
          choice = int(input('Please enter a value 1-2\n')) - 1
      print('{choice} chosen.'.format(choice = final_kill_options[choice]))
      self.final_kill_move = final_kill_options[choice]
    else:
      return None
##Allows player to choose what enhancement they'd like
  def choose_enhancement(self):
    print('Now Select a character enhancement below')
    enhancement = int(input(' 1. Extra Health, will increase health to 150 \n 2. Extra Strength, increases attack power by 5 points (excludes final kill)\n Input a number and press enter to select.\n'))
    while enhancement not in range(1, 3):
      enhancement = int(input('Please type a number 1-4 and press enter to select\n'))
    if enhancement == 1 :
      self.enhancement = 'Extra Health'
    elif enhancement == 2:
      self.enhancement = 'Extra Strength'
# will print out to user what selections they have made
  def __repr__(self):
    line = '\nPlayer '
    line += str(self.player_num)
    line += ' has selected {char}'.format(char = self.character)
    line += ' with the final kill {kill}'.format(kill = self.final_kill_move)
    line += ', and {encmt}'.format(encmt = self.enhancement)
    line += ' as their enhancement.'
    return line

################ NEW CLASS #####################
# Keeps track of attacks, health, blocks, and if a player is dead or not
class Fight:

  def __init__(self, character, enhancement, health, fight_dict, kill_move):
    self.kill_move = kill_move
    self.attack_moves = fight_dict
    self.character =  character
    self.enhancement = enhancement
    self.health = health
    self.attacks = 0
    self.blocks = 0
    self.blocks = 0
    self.final_kill_damage = 30
    self.blocking = False
## Allows player to attack other player and decrease their health by an amount multiplied by the attack level
  def attack_other_player(self, other_player):
    character = self.character
    character2 = other_player.character
    character_attacks = self.attack_moves
    print('{char} choose your attack'.format(char = character))
    move_list = []
    damage = [5, 7, 9, 14]
    for num in range(0, 4):
      move = character_attacks[character][num]
      print(str(num + 1) + ' ' + move)
      move_list.append(move)
    attack = int(input('Type the number of the attack you would like to make, then press enter to selcet\n'))
    while attack not in range(1, 5):
      attack = int(input('Please enter the attack number 1-4\n'))
    attack -= 1
    other_player.health -= damage[attack]
    if self.enhancement == 'Extra Strength':
        other_player.health -= 5
    health1 = self.health
    health2 = other_player.health
    attack_name = move_list[attack - 1]
    print('{char1} uses {attack} on {char2}\n'.format(char1 = character, attack = attack_name, char2 = character2))
    if other_player.health <= 30:
      print('{char} has final kill move ready for use\n'.format(char = character))
  
  def attack_and_block(self, other_player):
    character = self.character
    character2 = other_player.character
    character_attacks = self.attack_moves.get(character)
    print('{char} choose your attack'.format(char = character))
    move_list = []
    for num in range(0, 3):
      move = character_attacks[num]
      print(str(num + 1) + ' ' + move)
      move_list.append(move)

    attack = int(input('Type the number of the attack you would like to make, then press enter to selcet\n'))
    while attack not in range(1, 5):
      attack = int(input('Please enter the attack number 1-4\n'))
    attack_name = character_attacks[attack - 1]
    print('{char2} has blocked {attack}'.format(char2 = character2, attack = attack_name))

  def block_attack(self, other_player):
    character = self.character
    character2 = other_player.character
    print('''{char1} blocks {char2}.\n'''.format(char1 = character, char2 = character2))
  
### Allows player to use final kill move if otehr players health is 30 or less
  def final_kill(self, other_player):
    final_kill = other_player.kill_move
    if other_player.health <= 30:
      other_player.health = 0
      print('{char1} uses {kill} on {char2}, {char1} wins. Flawless Victory!\n'.format(char1 = self.character, char2 = other_player.character, kill = final_kill))
    else:
      print('We are sorry, the final kill is not available for you yet\n')
  ### allows to print out fighting stats of the player selected
  def __repr__(self):
    char = self.character
    health = self.health
    line = char
    line += ' has ' + str(health) + ' health'
    return line
#######################################################################
############### STARTING PLAYER INPUT AND GAME ########################
#######################################################################
print('#      #    #####    #####  ########   ####    #        ')
print('# #  # #   #     #   #    #    #      #    #   #        ')
print('#  ##  #  #       #  #####     #     ########  #        ')
print('#      #  #       #  # #       #     #      #  #        ')
print('#      #   #     #   #  #      #     #      #  #        ')
print('#      #    #####    #   #     #     #      #  #######  ')
print('')
print('#     #    #####    #      #  ####     ####   #########  ') 
print('#   ##    #     #   # #  # #  #   #   #    #      #      ')
print('# ##     #       #  #  ##  #  #####  ########     #      ')
print('# ##     #       #  #      #  #   #  #      #     #      ')
print('#   ##    #     #   #      #  #   #  #      #     #      ')
print('#     #    #####    #      #  ####   #      #     #      ')

print('Hello players and welcome to Mortal Kombat. We will start off by selecting characters, final kill moves, and enhancements before we start the game.')
## Starting player 1s character selection
print('''We will start off with Player 1's selection first.\n''')
player1 = Character(1)
player1_character = player1.choose_character()
player1_final_kill = player1.choose_final_kill()
player1_enhancement = player1.choose_enhancement()
print('\n' + str(player1) + '\n')

print('''\nNow we will do Player 2's character selection.\n''')
player2= Character(2)
player2_character = player2.choose_character()
player2_final_kill = player2.choose_final_kill()
player2_enhancement = player2.choose_enhancement()
print('\n'+ str(player2) + '\n')
print(player1.enhancement)
print(player2.enhancement)
#########################################################
########### Now the Fight between players begins ############################################################################
#########################################################

print('\nNow we will begin our fight between {char1} and {char2}\n'.format(char1 = player1.character, char2 = player2.character))
## Keeping track of the player fight stats with assigning each player their specific fight class
if player1.enhancement == 'Extra Health':
  player1_Fight = Fight(player1.character, player1.enhancement, 150, player1.attack_moves, player1.final_kill_move)
else:
  player1_Fight = Fight(player1.character, player1.enhancement, 100, player1.attack_moves, player1.final_kill_move)
if player2.enhancement == 'Extra Health':
  player2_Fight = Fight(player2.character, player2.enhancement, 150, player2.attack_moves, player2.final_kill_move)
else:
  player2_Fight = Fight(player2.character, player2.enhancement, 100, player2.attack_moves, player2.final_kill_move)
player1_health = player1_Fight.health
player2_health = player2_Fight.health
print(player1_Fight)
print(player2_Fight)
while (player1_health and player2_health) >= 30:
  print('Type number and press enter to choose move.')
  print('{char} select move.'.format(char = player1.character))
  player1_move = int(input('\n1.Block \n2. Attack\n'))
  print('{char} select move.'.format(char = player2.character))
  player2_move = int(input('\n1.Block \n2. Attack\n'))
  if player1_move == 1:
    if player2_move == 1:
      player1_Fight.block_attack(player2_Fight)
      player2_Fight.block_attack(player1_Fight)
    else:
      player2_Fight.attack_and_block(player1_Fight)
  elif player2_move == 2:
    if player1_move == 2:
      player1_Fight.attack_other_player(player2_Fight)
      player2_Fight.attack_other_player(player1_Fight)
    else:
      player2_Fight.attack_and_block(player1_Fight)
    
  print(player1_Fight)
  print(player2_Fight)
  player1_health = player1_Fight.health
  player2_health = player2_Fight.health
character1 = player1_Fight.character
character2 = player2_Fight.character
char1_kill = player1_Fight.kill_move
char2_kill = player2_Fight.kill_move
if (player1_health <= 30) and (player1_health < player2_health):
  print('''{char1}'s health is low, FINISH THEM'''.format(char1 = character1))
  player2_move = int(input('{char}, use {kill}\nType any number and press enter to continue.'.format(char = character2, kill = char1_kill)))
  player2_Fight.final_kill(player1_Fight)
elif (player2_health <= 30) and (player2_health < player1_health):
  print('''{char2}'s health is low, FINISH THEM'''.format(char2 = character2))
  player2_move = int(input('{char}, use {kill}\nType any number and press enter to continue.'.format(char = character1, kill = char1_kill)))
  player1_Fight.final_kill(player2_Fight)
