from nba_py import game
from time import sleep

infile = open("gameids.csv",'r')
outfile = open("nbagames.csv", 'a')
failfile = open("failgid.csv", 'a')

for line in infile:
    gameid = line.rstrip()
    try:
        bs = game.BoxscoreSummary("00" + str(gameid))
        for gamesum in bs.game_summary():
            outfile.write(str(gamesum['GAME_ID']) + ', ')
            outfile.write(str(gamesum['GAME_SEQUENCE']) + ', ')
            outfile.write(str(gamesum['GAME_STATUS_TEXT']) + ', ')
            outfile.write(str(gamesum['HOME_TEAM_ID']) + ', ')
            outfile.write(str(gamesum['VISITOR_TEAM_ID']) + ', ')
            outfile.write(str(gamesum['SEASON']) + ', ')
            outfile.write(str(gamesum['NATL_TV_BROADCASTER_ABBREVIATION']) + ', ')
        for gameinf in bs.game_info():
            outfile.write(str(gameinf['GAME_DATE']) + ', ')
            outfile.write(str(gameinf['GAME_TIME']) + ', ')
            outfile.write(str(gameinf['ATTENDANCE']) + '\n')
        print(gameid + " successful")
        sleep(2)
    except Exception as exception:
        failfile.write(gameid + '\n')
        print(exception)
        sleep(2)

infile.close()
outfile.close()
failfile.close()