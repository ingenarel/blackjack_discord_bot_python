list = []

while True:
    try:
        list.append(input())
    except KeyboardInterrupt:
        exit(list)