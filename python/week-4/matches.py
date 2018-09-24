def orangecap(matchData):
    playerData = {}

    # For each set of scores in matches
    for scores in matchData.values():
        # for each player and score in the match
        for player, score in scores.items():
            # get the current score for the player
            currentScore = playerData.get(player)

            # if the current score is empty, this player 
            # has played the match for the first time
            # set his or her score to 0
            if(currentScore == None):
                playerData[player] = 0
                currentScore = 0

            # update the sum of the player's score
            currentScore += score

            # update the dictionary to the new score
            playerData[player] = currentScore

    max = 0
    maxPlayer = None
    for player, score in playerData.items():
        if(score > max):
            # if a score is greater than the previous max
            # then update the max
            maxPlayer = player
            max = score

    return (maxPlayer, max)


orangecap({'match1': {'player1': 57, 'player2': 38}, 'match2': {'player3': 9,
                                                                'player1': 42}, 'match3': {'player2': 41, 'player4': 63, 'player3': 91}})
# ('player3', 100)

orangecap({'test1': {'Ashwin': 84, 'Kohli': 120},
           'test2': {'ashwin': 59, 'Pujara': 42}})
# ('Kohli', 120)
