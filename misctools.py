def sign():
    print('Leevi Aaltonen 2017')


def log(s):
    print(s)
    from datetime import datetime
    now = datetime.now()
    date = str(now.day) + '-' + str(now.month) + '-' + str(now.year)
    time = str(now.time())
    while True:
        try:
            with open('logs/' + date + '.log', 'a') as logfile:
                logfile.write(time + ' ' + s + '\n')
                break
        except FileNotFoundError:
            import os
            os.makedirs('logs/', exist_ok=True)
            open('logs/' + date + '.log', 'x')
