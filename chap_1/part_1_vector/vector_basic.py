import numpy as np
### vector addition

v = np.array([4,5,6])
w = np.array([10,20,30])
u = np.array([0,3,6,9])

v_w = v + w
print(v_w)
try:
    u_w = u + w
    print(u_w)
except ValueError as e:
    print(f"Error : {e}")

###broadcasting

w = np.array([[10,20,30]])
v = np.array([v])
#deep copy
w_t = w.T
print(v+w_t)

### Scala-vector Multiplication

s = 2
a = [3,4,5]

print(s*a)

b = np.array(a)

print(s*b)


### SCala-vector Addition
#Broadcasting
print(s+b)


### vector len,norm

v = np.array([1,2,3,7,8,9])
v_dim = len(v)
v_magnitude = np.linalg.norm(v)

print(v_dim,v_magnitude)


### vector dot product

v = np.array([1,2,3,4])
w = np.array([5,6,7,8])

print(np.dot(v,w))

# 10 * dot(v,w) == dot(10*v,w) == dot(v,10*w)
s = 10
print(np.dot(s*v,w))
print(np.dot(v,w*s))




