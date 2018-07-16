from GraphLoader import GraphLoader
from apiPoster import apiPoster

G = GraphLoader()
poster = apiPoster()
print(G)

x,y = poster.getposition()
currpos = int(150*y + x)
successvalue = 2 #iniitalize no flaws

'''recursive dijkstra and poster'''
def solvehackgps(currpos):
    optimalpath = G.getDijkstra(currpos, 22499)
    print('Dijkstra solved')
    dirlist = []
    for i in range(1,len(optimalpath)):
        diff = optimalpath[i] - optimalpath[i-1]
        if diff == 1: 
            direct = 'right'
        elif diff == 150: 
            direct = 'down'
        elif diff == -1:
            direct = 'left'
        else:
            direct = 'up'
        dirlist.append(direct)
    
    for i in range(0,len(dirlist)):
        if dirlist[i] == 'right':
            successvalue = poster.moveright()
        elif dirlist[i] == 'down':
            successvalue = poster.movedown()
        elif dirlist[i] == 'up':
            successvalue = poster.moveup()
        else:
            successvalue = poster.moveleft()
            
        if successvalue == 2:
            print('Success!')
        elif successvalue == 1:
            print('Glitch encountered')
            x,y = poster.getposition()
            nextpos = 150*y + x
            solvehackgps(nextpos)
            break
        else:
            print('GG')
            break

solvehackgps(currpos)