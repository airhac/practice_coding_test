import sys
input = sys.stdin.readline
king, rock, n = input().rstrip().split()
alpha = ord('A')

d = {'R' : [1, 0], 'L' : [-1, 0], 'B' : [0, -1], 'T' : [0, 1], 'RT' : [1, 1], 'LT' : [-1, 1], 'RB' : [1, -1], 'LB' : [-1, -1]}
king_loc = [ord(king[0]) - alpha, int(king[1]) - 1]
rock_loc = [ord(rock[0]) - alpha, int(rock[1]) - 1]

for _ in range(int(n)):
    dx, dy = d[input().strip()]
    nx = (king_loc[0] + dx) 
    ny = (king_loc[1] + dy)
    if 0 <= nx < 8 and 0 <= ny < 8:
        king_loc[0] = nx  
        king_loc[1] = ny
        if rock_loc == king_loc:
            rx = (rock_loc[0] + dx) 
            ry = (rock_loc[1] + dy)
            if 0 <= rx < 8 and 0 <= ry < 8:
                rock_loc[0] = rx
                rock_loc[1] = ry
            else:
                king_loc[0] -= dx
                king_loc[1] -= dy
print(chr(king_loc[0] + alpha) + str(king_loc[1] + 1))
print(chr(rock_loc[0] + alpha) + str(rock_loc[1] + 1))