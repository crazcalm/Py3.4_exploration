from queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        loser = simqueue.dequeue()
        print(loser)

    return simqueue.dequeue()

if __name__ == "__main__":
    names = ["Marcus", "Emily", "Mohan", "Jo", "George"]

    print(hotPotato(names, 7))
