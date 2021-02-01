#Shreeji Patel
#105151171

matches = open('matches.txt', 'r')
matches_read = matches.read()
matches_list = matches_read.strip().split('\n')
match = []
for i in range(len(matches_list)):
    match.append(matches_list[i].split(','))

ranks = open('ranks.txt', 'r')
ranks_read = ranks.read()
ranks_list = ranks_read.strip().split('\n')

print("Underdog\t\t\tRank\tScore\tBets\tvs\tFavourite\tRank\tScore\tBets")
for i in range(len(match)):
    check1 = False
    check2 = False
    check3 = False
    team1 = match[i][0]
    score1 = match[i][1]
    bets_placed1 = int(match[i][2])
    team2 = match[i][3]
    score2 = match[i][4]
    bets_placed2 = int(match[i][5])
    total_bets = bets_placed1 + bets_placed2
    rank1 = ranks_list.index(team1)+1
    rank2 = ranks_list.index(team2)+1
    if rank1>rank2 and score2>score1: check1 = True
    elif rank2>rank1 and score1>score2: check1 = True
    else: check1 = False

    if(rank1>rank2):
        if score2 > score1:
            if rank1-rank2 > 10:
                check2 = True
        else: check2 = False
    else:
        if score1 > score2:
            if rank2-rank1 > 10:
                check2 = True
        else:
            check2 = False

    if score1>score2:
        ratio = bets_placed2/total_bets
        if ratio>0.8:
            check3=True
        else: check3 = False
    else:
        ratio = bets_placed1/total_bets
        if ratio>0.8:
            check3 = True
        else: check3 = False


    if check1: 
        if check2:
            if check3:
                if(score1 > score2):
                    print('true')
                    print(team2,'\t','\t','\t', rank2,'\t', score2,'\t', bets_placed2,'\t', 'vs','\t', team1,'\t', rank1,'\t', score1,'\t', bets_placed1)
                else:
                    print('false')
                    print(team1,'\t','\t','\t', rank1,'\t', score1,'\t', bets_placed1,'\t', 'vs','\t', team2,'\t', rank2,'\t', score2,'\t', bets_placed2)
                
