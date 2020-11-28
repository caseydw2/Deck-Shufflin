import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def perf_shuffle(deck):
    top, bottom = np.array_split(deck, 2)
    new_deck = np.zeros(deck.shape)
    for i in range(len(top)):
        j = i * 2
        new_deck[j] = top[i]
    for i in range(len(bottom)):
        j = i * 2 + 1
        new_deck[j] = bottom[i]
    return new_deck

def shuffle_algorithm(size):
    tally = 0
    r = size

    while (r != 1):
        if r % 2 == 0:
            r = r / 2
        else:
            r = r + ((size - 1) - r) / 2
        tally += 1
    return(tally)

def Shuffle_Deck_Size(max_size):

    x = np.arange(2, max_size, 2)
    y = np.zeros(len(x))
    b = 0
    for n in x:
        number_of_shuffles = shuffle_algorithm(n)
        y[b] = number_of_shuffles
        b += 1
    return x, y

def plotting(x,y,*lines):
    for i,line in enumerate(lines):
      plt.plot(x, line(x), '--', label= f'line {i+1}')
    plt.plot(x, y, 'ro',label = '(size,shuffles)')

    plt.legend()
    plt.xlabel('Deck Size')
    plt.ylabel('# of Shuffles')
    plot = plt.show()
    prime = x-1
    df = pd.DataFrame({'Deck': x, 'Shuffles': y, 'Deck-1': prime, 'Diff': x - y})
    return plot,df

def line_finder(point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    m = (y2-y1)/(x2-x1)
    b = m * (-x1)
    b += y1
    return m,b

def cycle(size,d=2):
  cycle = []
  n = 0
  sm = size - 1
  cycle.append(2)
  while(d != 2 or n == 0):
      d = (d + 2**n) % sm
      if d == 2:
          break
      cycle.append(d)
      n = n + 1
      return cycle,len(cycle)

