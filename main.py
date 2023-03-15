import libs.game2 as game2
import sys


if len(sys.argv) != 4:
    print("Use => %s <numero_partidas> <nombre_user_uno> <nombre_user_dos>" % sys.argv[0])
    # print(len(sys.argv))
    sys.exit()
    
numPart = int(sys.argv[1])
name_one = sys.argv[2]
name_two =  sys.argv[3]

pointOne= 0
pointTwo= 0

for i in range(numPart+1):
    game = game2.TicTacToe(300,300,"hi")
    game.run()
    print("ganador main")
    print(game.ganador)
    

