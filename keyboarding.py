def min_keystrokes(grid,text):
    r = len(grid)
    c = len(grid[0])
    i=0
    positions = {}
    for i in range(r):
        for j in range(c):
            if grid[i][j] in positions:
                positions[grid[i][j]].append((i, j))
            else:
                positions[grid[i][j]] = [(i, j)]
    keystrokes = 0
    prev = positions[grid[0][0]][0]
    for ch in text[0:]:
        curr = min(positions[ch], key=lambda x: abs(x[0] - prev[0]) + abs(x[1] - prev[1]))
        keystrokes += abs(curr[0] - prev[0]) + abs(curr[1] - prev[1])
        prev = curr
    curr = min(positions['*'], key=lambda x: abs(x[0] - prev[0]) + abs(x[1] - prev[1]))
    keystrokes += (abs(curr[0] - prev[0]) + abs(curr[1] - prev[1])+1)
    keystrokes += len(text)
      
    return keystrokes

r, c = map(int, input("Enter rows and columns : ").split())
keyboard = []
print("Enter keys: ")
for i in range(r):
    line = input().upper()
    # Remove any whitespaces from the input line
    line = line.replace(" ", "")
    keyboard.append(line)
word = input("Enter text : ").upper().replace(" ", "") 

print(min_keystrokes(keyboard, word))