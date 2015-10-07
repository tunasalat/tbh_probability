#!/usr/bin/python
import random
Q = 4

def reroll_sixes(pool):
    while 6 in pool:
        pool.remove(6)
        pool.append(random.randint(1,6))
        pool.append(random.randint(1,6))
    return pool

def improve_fives(pool, boosts):
    while 5 in pool and boosts > 0:
        boosts -= 1
        pool.remove(5)
        pool.append(6)
    return pool

def improve_fail(pool, boosts):
    while Q - 1  in pool and boosts > 0:
        boosts -= 1
        pool.remove(Q - 1)
        pool.append(Q)
    return pool

def reroll_first_strategy(pool, boosts):
    while (boosts > 0 and (Q - 1  in pool or 5 in pool) or  6 in pool):
        if count_successes(pool)  >= 2:
            break
        reroll_sixes(pool)
        while 5 in pool and boosts > 0:
            boosts -= 1
            pool.remove(5)
            pool.append(random.randint(1,6))
            pool.append(random.randint(1,6))
            reroll_sixes(pool)
        if Q - 1 in pool and not 5 in pool and not 6 in pool and boosts > 0:
            boosts -= 1
            pool.remove(Q - 1)
            pool.append(Q)
    return pool

def improve_first_strategy(pool, boosts):
    while (boosts > 0 and (Q - 1  in pool or 5 in pool)) or  6 in pool:
        if count_successes(pool)  >= 2:
            break
        if Q - 1 in pool and boosts > 0:
            boosts -= 1
            pool.remove(Q - 1)
            pool.append(Q)
        elif 5 in pool and boosts > 0:
            boosts -= 1
            pool.remove(5)
            pool.append(6)
        else:
            reroll_sixes(pool)
    return pool

def bear_boson_strategy(pool, boosts, reserve):
    while boosts > 0 and (Q - 1  in pool or 5 in pool) or  6 in pool:
        if count_successes(pool)  >= 2:
            break
        if Q - 1 in pool and boosts > 0:
            boosts -= 1
            pool.remove(Q - 1)
            pool.append(Q)
        elif 6 in pool and boosts >= reserve:
            pool.remove(6)
            pool.append(random.randint(1,6))
            pool.append(random.randint(1,6))
        elif 5 in pool and boosts >= reserve + 1:
            boosts -= 1
            pool.remove(5)
            pool.append(random.randint(1,6))
            pool.append(random.randint(1,6))
        else:
            break
    return pool

def intelligent_strategy(pool, boosts):
    while boosts > 0 and (Q - 1  in pool or 5 in pool) or  6 in pool:
        if count_successes(pool) + min(boosts, (sum(i == Q - 1 for i in pool))) >= 2:
            while Q - 1  in pool and boosts > 0:
                boosts -= 1
                pool.remove(Q - 1)
                pool.append(Q)
            break
        elif 6 in pool:
            pool.remove(6)
            pool.append(random.randint(1,6))
            pool.append(random.randint(1,6))
        elif 5 in pool and boosts > 0:
            boosts -= 1
            pool.remove(5)
            pool.append(random.randint(1,6))
            pool.append(random.randint(1,6))
        else:
            break
    return pool





def count_successes(pool):
    return sum(i >= Q for i in pool)

def roll_3d6():
    pool = []
    for i in range(0, 3):
        pool.append(random.randint(1,6))
    return pool


### Zero boosts!!!

#Ordinary 3d6 roll
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    if count_successes(roll)  >= 2:
        probability += 1
print 'Ordinary 3d6 roll success probability: ' + str(probability / 100000.0 * 100.0) + '%'

#TBH exploding 3d6 roll
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    reroll_sixes(roll)
    if count_successes(roll)  >= 2:
        probability += 1
print 'TBH exploding 3d6 roll probability: ' + str(probability / 100000.0 * 100.0) + '%'

### Carefull strategy: improve fails only!

#Carefull strategy roll with 1 boost
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    improve_fail(roll, 1)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Ordinary 3d6 roll with 1 boost success probability: ' + str(probability / 100000.0 * 100.0) + '%'

#Carefull strategy roll with 2 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    improve_fail(roll, 2)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Ordinary 3d6 roll with 2 boosts success probability: ' + str(probability / 100000.0 * 100.0) + '%'

#Carefull strategy roll with 3 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    improve_fail(roll, 3)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Ordinary 3d6 roll with 3 boosts success probability: ' + str(probability / 100000.0 * 100.0) + '%'


### Safe-explode strategy: improve fails first, then improve fives

#Safe-explode strategy roll with 1 boost
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    improve_first_strategy(roll, 1)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Safe-explode strategy with 1 boost success probability: ' + str(probability / 100000.0 * 100.0) + '%'

#Safe-explode strategy roll with 2 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    improve_first_strategy(roll, 2)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Safe-explode strategy with 2 boosts success probability: ' + str(probability / 100000.0 * 100.0) + '%'

#Safe-explode strategy roll with 3 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    improve_first_strategy(roll, 3)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Safe-explode strategy with 3 boosts success probability: ' + str(probability / 100000.0 * 100.0) + '%'


### Risky strategy: improve fails first, then improve fives

#Risky strategy roll with 1 boost
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    reroll_first_strategy(roll, 1)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Risky strategy with 1 boost success probability: ' + str(probability / 100000.0 * 100.0) + '%'

#Risky strategy roll with 2 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    reroll_first_strategy(roll, 2)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Risky strategy with 2 boosts success probability: ' + str(probability / 100000.0 * 100.0) + '%'

#Risky strategy roll with 3 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    reroll_first_strategy(roll, 3)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Risky strategy with 3 boosts success probability: ' + str(probability / 100000.0 * 100.0) + '%'


### Bear boson strategy: improve fails first, improve fives only if boosts are left 1 reserve boost

#Bear boson strategy roll with 1 boost
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    bear_boson_strategy(roll, 1, 1)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Bear boson strategy with 1 boost success probability 1 reserve boost: ' + str(probability / 100000.0 * 100.0) + '%'

#Bear boson strategy roll with 2 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    bear_boson_strategy(roll, 2, 1)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Bear boson strategy with 2 boosts success probability 1 reserve boost: ' + str(probability / 100000.0 * 100.0) + '%'

#Bear boson strategy roll with 3 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    bear_boson_strategy(roll, 3, 1)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Bear boson strategy with 3 boosts success probability 1 reserve boost: ' + str(probability / 100000.0 * 100.0) + '%'


### Bear boson strategy: improve fails first, improve fives only if boosts are left 2 reserve boosts

#Bear boson strategy roll with 1 boost
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    bear_boson_strategy(roll, 1, 2)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Bear boson strategy with 1 boost success probability 2 reserve boost: ' + str(probability / 100000.0 * 100.0) + '%'

#Bear boson strategy roll with 2 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    bear_boson_strategy(roll, 2, 2)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Bear boson strategy with 2 boosts success probability 2 reserve boost: ' + str(probability / 100000.0 * 100.0) + '%'

#Bear boson strategy roll with 3 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    bear_boson_strategy(roll, 3, 2)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Bear boson strategy with 3 boosts success probability 2 reserve boost: ' + str(probability / 100000.0 * 100.0) + '%'

### Intelligent strategy with 1 boost
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    intelligent_strategy(roll, 1)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Intelligent strategy with 1 boost success probability: ' + str(probability / 100000.0 * 100.0) + '%'

### Intelligent strategy with 2 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    intelligent_strategy(roll, 2)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Intelligent boson strategy with 2 boosts success probability: ' + str(probability / 100000.0 * 100.0) + '%'

### Intelligent strategy with 3 boosts
probability = 0.0
for i in range(1, 100000):
    roll = roll_3d6()
    intelligent_strategy(roll, 3)
    if count_successes(roll)  >= 2:
        probability += 1
print 'Intelligent strategy with 3 boosts success probability: ' + str(probability / 100000.0 * 100.0) + '%'
