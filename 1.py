list = [None]
for i in range(100):
    list.append(0)
commands = [None]
list[1] = 2
list[2] = 3
while True:
    s = input()
    if s == 'e':
        break
    commands.append(s.split())
print(commands)
def solve(commands, i, list):
    if i > len(commands)-1:
        return list
    if commands[i][0] == 'Z':
        list[int(commands[i][1])] = 0
        solve(commands, i + 1, list)
    elif commands[i][0] == 'S':
        list[int(commands[i][1])] += 1
        solve(commands, i + 1, list)
    elif commands[i][0] == 'T':
        list[int(commands[i][2])] = list[int(commands[i][1])]
        solve(commands, i+1, list)
    elif commands[i][0] == 'J':
        if list[int(commands[i][1])] == list[int(commands[i][2])] and int(commands[i][3]) <= len(commands):
            solve(commands, int(commands[i][3]), list)
        elif list[int(commands[i][1])] == list[int(commands[i][2])] and int(commands[i][3]) > len(commands):
            return
        else:
            solve(commands, i + 1, list)
    return list

print(solve(commands, 1, list))
