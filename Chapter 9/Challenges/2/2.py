import games, cards

deck = Deck()
deck.populate()
deck.shuffle()

player1 = Hand()
player2 = Hand()

players = [player1, player2]

deck.deal(players)

p1_card_val = player1.cards[0].rank
p2_card_val = player2.cards[0].rank


