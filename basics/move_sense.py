#!/usr/bin/env python3

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]

pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = [p_ * pMiss if world[i] is not Z else p_ * pHit for i, p_ in enumerate(p)]  # hit or miss
    q = [norm / sum(q) for norm in q]  # normalize
    return q


def move(p, U):
    q = []
    for i in range(len(p)):
        s = p[(i-U - 1)%len(p)] * pUndershoot
        s = s + p[(i-U)%len(p)] * pExact
        s= s + p[(i-U + 1)%len(p)] * pOvershoot
        q.append(s)
    return q


if __name__ == '__main__':
    for i, mo in enumerate(motions):
        p = sense(p, measurements[i])  # sense then move
        p = move(p, mo)

    print(p)
