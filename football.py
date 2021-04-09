# class Footballer:
#     def __init__(self, firstname,surname, club, wage):
#         self.firstname = firstname
#         self.surname = surname
#         self.club = club
#         self.wage = wage
#
#     def fullname(self):
#         return '{} {}'.format(self.firstname, self.surname)
#
#
#
# fb_1 = Footballer('Cristiano', 'Ronaldo', 'Juventus', 800000)
# fb_2 = Footballer('Mo', 'Salah', 'Liverpool', 200000)
#
# print(Footballer.fullname(fb_1))
# print(fb_1.fullname())
# print(fb_2.fullname())

# class Team:
#     numberofplayers = 0
#     def __init__(self, playername, positions, gamesplayed, goalsscored):
#         self.playername = playername
#         self.positions = positions
#         self.gamesplayed = gamesplayed
#         self.goalsscored = goalsscored
#         self.avggoals = self.goalsscored / self.gamesplayed
#
#         Team.numberofplayers += 1
#
#     def avg_goals_scored(self):
#         return ('{} '.format(self.playername)+ 'scored on average ' + str(self.avggoals) + ' goals per game')
class Players:
    no_of_players = 0
    def __init__(self, playersname, playersage):
        self.playersname = playersname
        self.playersage = playersage
# player1 = Team('Mo Salah', 'RW', 5, 4)
# player2 = Team('Diogo Jota', 'ST', 3, 2)
# player3 = Team('Sadio Mane', 'LW', 5, 9)
# print(player3.goalsscored)
#
# print(player1.avg_goals_scored())
# print(player2.avg_goals_scored())
# print(player3.avg_goals_scored())
#
# print(Team.numberofplayers)

def player():
    while True:
        question = input('Would you like to add a new player')
        question = question.upper()
        playerID = 0000
        if question == 'Y':
            Players.playersname = input('name')
            Players.playersage = input('age')
            playerID = playerID + Players.no_of_players
            P = [Players.playersname +', ' + Players.playersage]
            P.extend(str(playerID))
            Players.no_of_players += 1
            while True:
                if playerID == 0:
                    List = []
                    List.extend(P)
                    print(List)
                    break
                else:
                    List.extend(P)
                    print(List)
                    break
        elif question == 'N':
            if Players.no_of_players == 0:
                print('have a nice day')
                break
            else:
                print('thanks')
                print('final list of players: ', List, 'total players = ', Players.no_of_players)
                break
        else:
            print('incorrect input, please type Y for yes and N for no')

player()







