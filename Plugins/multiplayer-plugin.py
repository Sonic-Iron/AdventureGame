def cmd_intercept(cmd):
    if cmd.startswith('say'):
        file = open('multiplayer.txt', 'a')
        file.write('\nspeech:player1:' + cmd[4:])
        file.close()
        return False
    else:
        return True