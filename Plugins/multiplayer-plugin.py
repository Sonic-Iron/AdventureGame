def cmd_intercept(cmd):
    if cmd.startswith('say'):
        file = open('multiplayer.txt', 'a')
        file.append('\nspeech:player1:' + cmd[4:])
        return False
    else:
        return True