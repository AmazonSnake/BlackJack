import random


cards = (1,2,3,4,5,6,7,8,9,10,10,10, 10)
keepPlaying = True
playerCardTotal = 0
dealerCardTotal = 0

#This is where the game begins

def startGame():
  global dealerCardTotal
  global playerCardTotal
  player1 = (random.choice(cards))
  playerCardTotal += player1
  player2 = (random.choice(cards))
  playerCardTotal += player2
  if player1 and player2 == 1:
    print("You got 2 aces!")
    
  if player1 == 1:
    print("You got an ace!")
  if player2 == 2:
    print("You got an Ace!")
  print(f"You have been dealt 2 cards, they equal to {playerCardTotal}")
  if playerCardTotal == 21:
    print('Blackjack, you win!')
    playAgain()
  elif playerCardTotal > 21:
    print("You bust.")
    playAgain()
    
  dealerCardTotal += random.choice(cards)
  print(f"Dealer has 2 cards, {dealerCardTotal}, and one facedown card.")
  dealerCardTotal += random.choice(cards)
  
def ace():
  ace = int(input("Would you like to treat your ace as a 1, or 10?"))

def newCardPlayer():
  global playerCardTotal
  newCard = random.choice(cards)
  if newCard == 1:
    print("You got an Ace!")
  playerCardTotal += newCard
  print(f"Your cards now equal to {playerCardTotal}")
  if playerCardTotal > 21:
    checkWin()
  choices()

def newCardDealer():
  global dealerCardTotal
  print(f"Dealer has {dealerCardTotal}.")
  while dealerCardTotal < 17:
    dealerCardTotal += random.choice(cards)
    print("Dealer must take more cards to reach 17.")
    print(f"Dealer takes a card, he is now at {dealerCardTotal}.")
  if dealerCardTotal >= 17:
    checkWin()
  
def checkWin():
  global dealerCardTotal
  global playerCardTotal
  if playerCardTotal > 21:
    print("You lose")
    print(f"Dealer had {dealerCardTotal}, you had {playerCardTotal}.")
    playAgain()
  elif dealerCardTotal > 21:
    print("You win!")
    print(f"Dealer had {dealerCardTotal}, you had {playerCardTotal}.")
    playAgain()
  elif dealerCardTotal < playerCardTotal:
    print("You win!")
    print(f"Dealer had {dealerCardTotal}, you had {playerCardTotal}.")
    playAgain()
  elif dealerCardTotal > playerCardTotal:
    print("You lose!")
    print(f"Dealer had {dealerCardTotal}, you had {playerCardTotal}.")
    playAgain()
  else:
    print("You tied!")
    print(f"Dealer had {dealerCardTotal}, you had {playerCardTotal}.")
    playAgain()

def choices():
  
  choice = int(input("Enter 1 to hit, 2 to stand."))
  if choice == 1:
    newCardPlayer()
  elif choice ==2:
    newCardDealer()
    
    
def playAgain():
  global playerCardTotal
  global dealerCardTotal
  global keepPlaying
  play = int(input("Enter 1 to play again, 2 to quit playing."))
  if play == 1:
    keepPlaying = True
    playerCardTotal = 0
    dealerCardTotal = 0
  else:
    quit()
    



while keepPlaying:
  startGame()  
  choices()



