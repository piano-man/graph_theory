import numpy as np
import tensorflow as tf
from itertools import permutations
from time import sleep
from time import time
def P_A_Pt(a,arr):

  a = tf.convert_to_tensor(a,tf.float32)

  at = tf.transpose(a)

  ans = tf.multiply(arr,a)
  ans1 = tf.multiply(at,ans)

  return ans1

def createPerm(x):
  n = len(x)
  a = np.zeros((n,n))
  for i in range(n):
    #print(x[i])
    #type(x[i])
    a[i][x[i]] = 1
  return a
def checkIsomorphism(g,h):

  perms = list(permutations(range(n)))
  for a in perms:
    a = createPerm(a)
    #z = [[0,0],[0,0]]
    #a = np.asarray(z)
    x = P_A_Pt(a,g)
    equal = tf.equal(x,h)
    equal = tf.reduce_all(equal)
    with tf.Session() as sess:
      equal = sess.run(equal)
      if(equal):
        print("equal")
        return
  print("not equal")
n = 5
t2 = time()
arr = np.zeros((n,n))
t1 = time()
print(t1 - t2)
P = []
for i in range(n):
  P.append(n-i-1)
perms = list(permutations(P))
for i in range(n):
  for j in range(i):
    r = np.random.randint(2)
    if(i == j ):
      continue
    arr[i][j] = r
    arr[j][i] = r
    #arr[i][i] = 1
a = createPerm(P)
print(a)
arr = tf.convert_to_tensor(arr,tf.float32)
h = P_A_Pt(a,arr)
t = time()
checkIsomorphism(arr,h)
t = time() - t
print(t)
