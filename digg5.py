import random
import time






def region(arr,xlim,ylim,xd,yd,xp,yp,x,y):
  if xd < xlim-1 and yd < ylim-1 and xd > 0 and yd > 0:
    if arr[yd][xd] == 0:
      arr[y+yp][x+xp]=1
      return 0,xd,yd
    else:
      return 1,x,y
  else:
    print('wall flag')
    return 1,x,y

def chk(arr,xlim,ylim,x,y):
  if x+2 < xlim-1:
    if arr[y][x+2] == 0:
      return 0
  if x-2 > 0:
    if arr[y][x-2] == 0:
      return 0
  if y+2 < ylim-1:
    if arr[y+2][x] == 0:
      return 0
  if y-2 > 0:
    if arr[y-2][x] == 0:
      return 0
  print('return')
  return 1




def maze(arr,x,y,xlim,ylim,keiro,count):
  check = chk(arr,xlim,ylim,x,y)
  for i in range(ylim):
    print(arr[i])
  time.sleep(0.1)
  if check == 0:
    drc = random.randint(0,3)
    if drc == 0:
      xd = x+2
      yd = y
      xp = 1
      yp = 0
      renew,x,y = region(arr,xlim,ylim,xd,yd,xp,yp,x,y)
    elif drc == 1:
      xd = x-2
      yd = y
      xp = -1
      yp = 0
      renew,x,y = region(arr,xlim,ylim,xd,yd,xp,yp,x,y)
    elif drc == 2:
      xd = x
      yd = y+2
      xp = 0
      yp = 1
      renew,x,y = region(arr,xlim,ylim,xd,yd,xp,yp,x,y)
    else:
      xd = x
      yd = y-2
      xp = 0
      yp = -1
      renew,x,y = region(arr,xlim,ylim,xd,yd,xp,yp,x,y)
    print(x,y)
    arr[y][x]=1
    if renew== 0:
      keiro.append([y,x])
      count += 1
    maze(arr,x,y,xlim,ylim,keiro,count)
  elif count > 1:
    [y,x]=keiro[count-2]
    count -= 1
    print(x,y)
    keiro.pop()
    maze(arr,x,y,xlim,ylim,keiro,count)

 
  
    
  

xlim = 17
ylim = 17

arr = [[0 for i in range(xlim)]for j in range(ylim)]

print("")

x = random.randint(1,(xlim-1)/2)*2-1
y = random.randint(1,(ylim-1)/2)*2-1
arr[y][x]=1

keiro =[[y,x]]
count = 0
maze(arr,x,y,xlim,ylim,keiro,count)

print('')
print('')

for i in range(ylim):
  print(arr[i])

print('  ')

mp = [['E' for i in range(xlim)]for j in range(ylim)]

for i in range(ylim):
  for j in range(xlim):
    if arr[i][j]==1:
     mp[i][j] = ' '

for i in range(ylim):
  print(mp[i])
