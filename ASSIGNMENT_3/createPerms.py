import pickle as pkl
from itertools import permutations
from time import time
perms = []
print("hello")
for i in range(100):
    t = time()
    perms.append(permutations(range(i)))
    t = time() - t
    print(i," completed")
    if ( t > 2):
        print("Breaking Point",i)
        break
pkl.dump(perms,open("permutations.pkl","wb"))
