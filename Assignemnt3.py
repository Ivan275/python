from cards import *
import cards
import random
#shuffle card
d = deck()
random.shuffle(d)


#Player 1 & Player 2

player1 = d[0:7]
ptsP1 = 0
player2 = d[8:15]
ptsP2 = 0
player1.sort()
player2.sort()
#Stock
d = d[16:52]


player1, ptsP1 = drop_pair(player1)
player2, ptsP2 = drop_pair(player2)
#print "player2: ", hand_string(player2)


#print player1[0].__init__('2','C')

#compare
#print player2[0].__cmp__(player1[0]),player2[i].rank()
i = 0
c = 1
b = 0
m = 0
while i < 100:
    a = 0
    if ((-1) **c == -1):
        b = 1
    if ((-1) **c == 1):
        b = 2    
    print "Player ",b,"'s Turn"
    print
    print "Player 1 score: ", ptsP1
    print "Player 2 score: ", ptsP2
    print "Cards left in stock: ", len(d)
    print
##    print "Card Stock: ", hand_string(d)
    print 
    while (a < 2):
        if (b == 1):
            print "Your Cards: ", hand_string(player1)
##            print "Opponent Cards: ", hand_string(player2)
        elif (b == 2):
            print "Your Cards: ", hand_string(player2)
##            print "Opponent Cards: ", hand_string(player1)
        elif (len(player1) == 0 or len(player2)== 0 or len(d) == 0 ):
            print "Game Over"
            print "Player 1's score: ", ptsP1
            print "Player 2's score: ", ptsP2
            if (ptsP1 > ptsP2):
                print "Player 1 wins the game"
            elif (ptsP1 < ptsP2):
                print "Player 2 wins the game"
            else:
                print "Player 1 ties with Player 2"
        

        DrawC = raw_input("Ask other player for [23456789TJQKA]: ")
        print "Do you have any " + DrawC +"s?"

#Compare cards
        if (b == 1):
            x = has_a(player2, DrawC)
            if (x == True):
                player1, takenP1 = take_all(player1, DrawC)
                player2, takenP2 = take_all(player2, DrawC)
##                print "player1: ", hand_string(player1)
##                print "player2: ", hand_string(newhandP2)
                ptsP1 = ptsP1 + 1
                print "Yes: ", hand_string(takenP2)
                print "New Player 1 score: ", ptsP1
            else:
                a += 1
                print "You don't have any ",DrawC,"s. Make another choice."
            i += 1
        elif (b == 2):
            x = has_a(player1, DrawC)
            if (x == True):
                player1, takenP1 = take_all(player1, DrawC)
                player2, takenP2 = take_all(player2, DrawC)
##                print "player1: ", hand_string(player1)
##                print "player2: ", hand_string(newhandP2)
                ptsP2 = ptsP2 + 1
                print "Yes: ", hand_string(takenP1)
                print "New Player 1 score: ", ptsP2
            else:
                a += 1
                print "You don't have any ",DrawC,"s. Make another choice."
            i += 1  
    if (a >= 2):
        if (b == 1):
            i = 100
            print "Go fish."
            NewC = d[0]
            y = has_a(player1, NewC.rank())
            if (y == True):
                ptsP1 = ptsP1 + 2
            else:
#add a card to hand
##                C1 = cards.Card(NewC.rank(), NewC.suit())
##                player1 = player1[C1]
                print hand_string(player1)
##                player1=player1+deck.pop(0)
##                print ">>>>>>>>>>>>>>>>>>>>>>>>>>Problem: adding card to hand"
        elif (b == 2):
            i = 100
            print "Go fish."
            NewC = d[0]
            y = has_a(player2, NewC.rank())
            if (y == True):
                ptsP2 = ptsP2 + 2
            else:
#add a card to hand
##                C1 = Card(NewC.rank(), NewC.suit())
##                player2 = player2.append(C1)
                print hand_string(player2)
##                player2=player2+deck.pop(0)
##                print ">>>>>>>>>>>>>>>>>>>>>>>>>>Problem: adding card to hand"
        print "You picked up the ", NewC.longname(),"."
    if (len(player1) == 0 or len(player2)== 0 or len(d) == 0 ):
        print "Game Over"
        print "Player 1's score: ", ptsP1
        print "Player 2's score: ", ptsP2
        if (ptsP1 > ptsP2):
            print "Player 1 wins the game"
        elif (ptsP1 < ptsP2):
            print "Player 2 wins the game"
        else:
            print "Player 1 ties with Player 2"
        
    keybordStr = raw_input("End of turn, press enter.")
    print "----------------------------------------------------------------------"
    i = 0
    d = d[1:52] 
    c = c + 1    
    

    
