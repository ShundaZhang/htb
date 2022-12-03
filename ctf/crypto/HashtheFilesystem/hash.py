#!/usr/bin/python3.9

'''

#define _PyHASH_XXPRIME_1 ((Py_uhash_t)11400714785074694791ULL)
#define _PyHASH_XXPRIME_2 ((Py_uhash_t)14029467366897019727ULL)
#define _PyHASH_XXPRIME_5 ((Py_uhash_t)2870177450012600261ULL)
#define _PyHASH_XXROTATE(x) ((x << 31) | (x >> 33))  /* Rotate left 31 bits */

static Py_hash_t
tuplehash(PyTupleObject *v)
{
    Py_ssize_t i, len = Py_SIZE(v);
    PyObject **item = v->ob_item;

    Py_uhash_t acc = _PyHASH_XXPRIME_5;
    for (i = 0; i < len; i++) {
        Py_uhash_t lane = PyObject_Hash(item[i]);
        if (lane == (Py_uhash_t)-1) {
            return -1;
        }
        acc += lane * _PyHASH_XXPRIME_2;
        acc = _PyHASH_XXROTATE(acc);
        acc *= _PyHASH_XXPRIME_1;
    }

    /* Add input length, mangled to keep the historical value of hash(()). */
    acc += len ^ (_PyHASH_XXPRIME_5 ^ 3527539UL);

    if (acc == (Py_uhash_t)-1) {
        return 1546275796;
    }
    return acc;
}

'''

_PyHASH_XXPRIME_1=11400714785074694791
_PyHASH_XXPRIME_2=14029467366897019727
_PyHASH_XXPRIME_5=2870177450012600261
UINT64W=0xFFFFFFFFFFFFFFFF
UINT64=UINT64W+1
INT64=UINT64/2

def _PyHASH_XXROTATE(x):
	return (((x << 31) & UINT64W) | (x >> 33)) 

def _PyHASH_XXROTATE_R(x):
	return (((x << 33) & UINT64W) | (x >> 31)) 


def myhash(x):
	acc = _PyHASH_XXPRIME_5
	for i in range(len(x)):
		lane = x[i]
		acc += lane * _PyHASH_XXPRIME_2
		#print("============================")
		#print(acc)
		acc %= UINT64
		acc = _PyHASH_XXROTATE(acc)
		#print("============================")
		#print(acc)
		acc *= _PyHASH_XXPRIME_1
		#print("============================")
		#print(acc)
		acc %= UINT64

	acc += len(x) ^ (_PyHASH_XXPRIME_5 ^ 3527539)
	#print("****************************")
	#print(acc)
	acc %= UINT64
	if acc >= INT64:
		acc -= UINT64 
	return acc

print(hash(tuple([0])))
print(myhash(tuple([0])))
#print(hash(tuple([1])))
#print(myhash(tuple([1])))
#print(hash(tuple([1,2,3])))
#print(myhash(tuple([1,2,3])))
#print(hash(tuple([0,1,2,5,9,0])))
#print(myhash(tuple([0,1,2,5,9,0])))

#529344067295497451
'''
acc = _PyHASH_XXPRIME_5
lane = 2
acc += lane * _PyHASH_XXPRIME_2
acc &= UINT64W
acc = _PyHASH_XXROTATE(acc)
acc *= _PyHASH_XXPRIME_1
acc &= UINT64W
print(acc)

x = 529344067295497451 - (2^(_PyHASH_XXPRIME_5 ^ 3527539))
f = 0
for k in range(10000000):
	if (x + k*UINT64)%_PyHASH_XXPRIME_1 == 0:
		x = (x + k*UINT64)/_PyHASH_XXPRIME_1
		f = 1
		break
if f == 0:
	print("FAIL!!!")
f = 0
x = _PyHASH_XXROTATE(x)
x -= _PyHASH_XXPRIME_5
for k in range(10000000):
        if (x + k*UINT64)%_PyHASH_XXPRIME_2 == 0:
                x = (x + k*UINT64)/_PyHASH_XXPRIME_2
                f = 1
                break
if f == 0:
	print("FAIL2!!!")
print(x)
'''
