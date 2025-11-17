player_1 = input("Enter Rock, Paper or Scissors: ")
player_2 = input("Enter Rock, Paper or Scissors: ")

Rock = 'Rock'
Paper = 'Paper'
Scissors = 'Scissors'

if(player_1 == Rock and player_2 == Scissors);
	print("player_1 wins")

if(player_1 == Scissors and player_2 == Paper):
	print("player_1 wins")

if(player_1 == Rock and player_2 == Paper):
	print("player_2 wins")

if(player_2 == Rock and player_1 == Scissors):
	print("player_2 wins")

if(player_2 == Scissors and player_1 == Paper):
	print("player_2 wins")
