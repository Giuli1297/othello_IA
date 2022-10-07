# 1 representa blanco, 2 representa negro
# 3 donde blanco puede jugar, 4 donde negro puede jugar, 5 donde pueden jugar los dos


def start_othello_game():
    othello_table = [[0 for i in range(8)] for j in range(8)]
    othello_table[3][3] = 1
    othello_table[4][4] = 1
    othello_table[3][4] = 2
    othello_table[4][3] = 2
    reachable_states_table(othello_table)
    return othello_table


def playableTopRight(i, j, othello_table):
    if j < 6 and i > 1 and othello_table[i][j] != 1 and othello_table[i][j] != 2:
        if othello_table[i-1][j+1] == 1:
            c1 = i-2
            c2 = j+2
            while c1 >= 0 and c2 < 8:
                if othello_table[c1][c2] == 2:
                    if othello_table[i][j] == 3 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 4
                    return True
                elif othello_table[c1][c2] == 0:
                    return False
                c1 = c1 - 1
                c2 = c2 + 1
        elif othello_table[i-1][j+1] == 2:
            c1 = i - 2
            c2 = j + 2
            while c1 >= 0 and c2 < 8:
                if othello_table[c1][c2] == 1:
                    if othello_table[i][j] == 4 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 3
                    return True
                elif othello_table[c1][c2] == 0:
                    return False
                c1 = c1 - 1
                c2 = c2 + 1
    return False


def playableBottomRight(i, j, othello_table):
    if j < 6 and i < 6 and othello_table[i][j] != 1 and othello_table[i][j] != 2:
        if othello_table[i+1][j+1] == 1:
            c1 = i+2
            c2 = j+2
            while c1 < 8 and c2 < 8:
                if othello_table[c1][c2] == 2:
                    if othello_table[i][j] == 3 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 4
                    return True
                elif othello_table[c1][c2] == 0:
                    return False
                c1 = c1 + 1
                c2 = c2 + 1
        elif othello_table[i+1][j+1] == 2:
            c1 = i + 2
            c2 = j + 2
            while c1 < 8 and c2 < 8:
                if othello_table[c1][c2] == 1:
                    if othello_table[i][j] == 4 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 3
                    return True
                elif othello_table[c1][c2] == 0:
                    return False
                c1 = c1 + 1
                c2 = c2 + 1
    return False


def playableTopLeft(i, j, othello_table):
    if i > 1 and j > 1 and othello_table[i][j] != 1 and othello_table[i][j] != 2:
        if othello_table[i-1][j-1] == 1:
            c1 = i-2
            c2 = j-2
            while c1 >= 0 and c2 >= 0:
                if othello_table[c1][c2] == 2:
                    if othello_table[i][j] == 3 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 4
                    return True
                elif othello_table[c1][c2] == 0:
                    return False
                c1 = c1 - 1
                c2 = c2 - 1
        elif othello_table[i-1][j-1] == 2:
            c1 = i - 2
            c2 = j - 2
            while c1 >= 0 and c2 >= 0:
                if othello_table[c1][c2] == 1:
                    if othello_table[i][j] == 4 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 3
                    return True
                elif othello_table[c1][c2] == 0:
                    return False
                c1 = c1 - 1
                c2 = c2 - 1
    return False


def playableBottomLeft(i, j, othello_table):
    if i < 6 and j > 1 and othello_table[i][j] != 1 and othello_table[i][j] != 2:
        if othello_table[i+1][j-1] == 1:
            c1 = i-2
            c2 = j-2
            while c1 < 8 and c2 >= 0:
                if othello_table[c1][c2] == 2:
                    if othello_table[i][j] == 3 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 4
                    return True
                elif othello_table[c1][c2] == 0:
                    return False
                c1 = c1 + 1
                c2 = c2 - 1
        elif othello_table[i+1][j-1] == 2:
            c1 = i + 2
            c2 = j - 2
            while c1 < 8 and c2 >= 0:
                if othello_table[c1][c2] == 1:
                    if othello_table[i][j] == 4 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 3
                    return True
                elif othello_table[c1][c2] == 0:
                    return False
                c1 = c1 + 1
                c2 = c2 - 1
    return False


def playableRight(i, j, othello_table):
    if j < 6 and othello_table[i][j] != 1 and othello_table[i][j] != 2:
        if othello_table[i][j+1] == 1:
            c = j+2
            while c < 8:
                if othello_table[i][c] == 2:
                    if othello_table[i][j] == 3 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 4
                    return True
                elif othello_table[i][c] == 0:
                    return False
                c = c +1
        elif othello_table[i][j+1] == 2:
            c = j+2
            while c < 8:
                if othello_table[i][c] == 1:
                    if othello_table[i][j] == 4 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 3
                    return True
                elif othello_table[i][c] == 0:
                    return False
                c = c +1
    return False


def playableLeft(i, j, othello_table):
    if j > 1 and othello_table[i][j] != 1 and othello_table[i][j] != 2:
        if othello_table[i][j-1] == 1:
            c = j-2
            while c >= 0:
                if othello_table[i][c] == 2:
                    if othello_table[i][j] == 3 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 4
                    return True
                elif othello_table[i][c] == 0:
                    return False
                c = c -1
        elif othello_table[i][j-1] == 2:
            c = j-2
            while c >= 0:
                if othello_table[i][c] == 1:
                    if othello_table[i][j] == 4 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 3
                    return True
                elif othello_table[i][c] == 0:
                    return False
                c = c -1
    return False


def playableTop(i, j, othello_table):
    if i > 1 and othello_table[i][j] != 1 and othello_table[i][j] != 2:
        if othello_table[i-1][j] == 1:
            c = i-2
            while c >= 0:
                if othello_table[c][j] == 2:
                    if othello_table[i][j] == 3 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 4
                    return True
                elif othello_table[c][j] == 0:
                    return False
                c = c -1
        elif othello_table[i-1][j] == 2:
            c = i-2
            while c >= 0:
                if othello_table[c][j] == 1:
                    if othello_table[i][j] == 4 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 3
                    return True
                elif othello_table[c][j] == 0:
                    return False
                c = c -1
    return False


def playableBottom(i, j, othello_table):
    if i < 6 and othello_table[i][j] != 1 and othello_table[i][j] != 2:
        if othello_table[i+1][j] == 1:
            c = i+2
            while c < 8:
                if othello_table[c][j] == 2:
                    if othello_table[i][j] == 3 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 4
                    return True
                elif othello_table[c][j] == 0:
                    return False
                c = c +1
        elif othello_table[i+1][j] == 2:
            c = i+2
            while c < 8:
                if othello_table[c][j] == 1:
                    if othello_table[i][j] == 4 or othello_table[i][j] == 5:
                        othello_table[i][j] = 5
                    else:
                        othello_table[i][j] = 3
                    return True
                elif othello_table[c][j] == 0:
                    return False
                c = c +1
    return False


def reachable_states_table(othello_table):
    for i in range(8):
        for j in range(8):
            playableRight(i, j, othello_table)
            playableLeft(i, j, othello_table)
            playableTop(i, j, othello_table)
            playableBottom(i, j, othello_table)
            playableTopRight(i, j, othello_table)
            playableTopLeft(i, j, othello_table)
            playableBottomLeft(i, j, othello_table)
            playableBottomRight(i, j, othello_table)


def cleanReachableStateTable(table):
    for i in range(8):
        for j in range(8):
            if table[i][j] == 3 or table[i][j] == 4 or  table[i][j] == 5:
                table[i][j] = 0


def whoiswinnning(table):
    playerwhitecount = 0
    playerblackcount = 0
    for i in range(8):
        for j in range(8):
            if table[i][j] == 1:
                playerwhitecount = playerwhitecount + 1
            elif table[i][j] == 2:
                playerblackcount = playerblackcount + 1
    if playerwhitecount > playerblackcount:
        return 1
    elif playerblackcount > playerwhitecount:
        return 2
    else:
        return -1 #Empate


def playerCanPlay(table, player):
    canPlaySpot = player + 2
    for i in range(8):
        for j in range(8):
            if table[i][j] == canPlaySpot or table[i][j] == 5:
                return True
    return False


def calculate_game_result(table):
    player1 = 1 #black player
    player2 = 2 #white player

    player_ahead = whoiswinnning(table)
    if not playerCanPlay(table, player1) and not playerCanPlay(table, player2):
        return player_ahead
    else:
        return 0


def applyMov(table, mov, turno):
    player = 0
    opponent = 0
    i = mov[0]
    j = mov[1]
    if turno == 2:
        player = 2
        opponent = 1
    else:
        player = 1
        opponent = 2
    if playableRight(i, j, table):
        tempi = i
        tempj = j + 1
        while table[tempi][tempj] == opponent and 0 <= tempi <= 8 and 0 <= tempj <= 8:
            table[tempi][tempj] = player
            tempj = tempj + 1
    if playableBottomRight(i, j, table):
        tempi = i + 1
        tempj = j + 1
        while table[tempi][tempj] == opponent and 0 <= tempi <= 8 and 0 <= tempj <= 8:
            table[tempi][tempj] = player
            tempi = tempi + 1
            tempj = tempj + 1
    if playableBottom(i, j, table):
        tempi = i + 1
        tempj = j
        while table[tempi][tempj] == opponent and 0 <= tempi <= 8 and 0 <= tempj <= 8:
            table[tempi][tempj] = player
            tempi = tempi + 1
    if playableBottomLeft(i, j, table):
        tempi = i + 1
        tempj = j - 1
        while table[tempi][tempj] == opponent and 0 <= tempi <= 8 and 0 <= tempj <= 8:
            table[tempi][tempj] = player
            tempi = tempi + 1
            tempj = tempj - 1
    if playableLeft(i, j, table):
        tempi = i
        tempj = j - 1
        while table[tempi][tempj] == opponent and 0 <= tempi <= 8 and 0 <= tempj <= 8:
            table[tempi][tempj] = player
            tempj = tempj - 1
    if playableTopLeft(i, j, table):
        tempi = i - 1
        tempj = j - 1
        while table[tempi][tempj] == opponent and 0 <= tempi <= 8 and 0 <= tempj <= 8:
            table[tempi][tempj] = player
            tempi = tempi - 1
            tempj = tempj - 1
    if playableTop(i, j, table):
        tempi = i - 1
        tempj = j
        while table[tempi][tempj] == opponent and 0 <= tempi <= 8 and 0 <= tempj <= 8:
            table[tempi][tempj] = player
            tempi = tempi - 1
    if playableTopRight(i, j, table):
        tempi = i - 1
        tempj = j + 1
        while table[tempi][tempj] == opponent and 0 <= tempi <= 8 and 0 <= tempj <= 8:
            table[tempi][tempj] = player
            tempi = tempi - 1
            tempj = tempj + 1
    table[i][j] = player


def moves_quantity(player, table):
    canMove = player + 2
    value = 0
    for i in range(8):
        for j in range(8):
            if table[i][j] == canMove or table[i][j] == 5:
                value = value + 1
    return value
