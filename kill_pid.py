import os


def kill_pid():
    r = os.popen("fuser -v /dev/nvidia*")
    text = r.read()
    ls = text.strip().split(' ')
    for l in ls:
        if not l == '':
            os.popen('kill -9 ' + l)
    # print(ls, type(ls))


if __name__ == "__main__":
    kill_pid()