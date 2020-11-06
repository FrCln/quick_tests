def echo():
    msg_old = msg_new = None
    while True:
        tmp = yield msg_old
        msg_old = msg_new
        msg_new = tmp


e = echo()
next(e)
for i in range(7):
    print(i)
    print(e.send(10 + i))
