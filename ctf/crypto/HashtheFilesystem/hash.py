#!/usr/bin/python3.9

import json

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
		acc %= UINT64
		acc = _PyHASH_XXROTATE(acc)
		acc *= _PyHASH_XXPRIME_1
		acc %= UINT64

	acc += len(x) ^ (_PyHASH_XXPRIME_5 ^ 3527539)
	acc %= UINT64
	if acc >= INT64:
		acc -= UINT64 
	return acc

#print(hash(tuple([0])))
#print(myhash(tuple([0])))
#print(hash(tuple([1])))
#print(myhash(tuple([1])))
print(hash(tuple([1,2,3])))
print(myhash(tuple([1,2,3])))
print(hash(tuple([2**64,2**64,302715549475208033])))
#print(hash(tuple([2,3,])))
#print(hash(tuple([0,1,2,5,9,0])))
#print(myhash(tuple([0,1,2,5,9,0])))


def reverse_hash(x0, l):
	acc = _PyHASH_XXPRIME_5
	#for i in [1, 2]:
	for i in [2**64]*(l-1):
		lane = hash(i)
		acc += lane * _PyHASH_XXPRIME_2
		acc %= UINT64
		acc = _PyHASH_XXROTATE(acc)
		acc *= _PyHASH_XXPRIME_1
		acc %= UINT64

	x = x0 - ((l)^(_PyHASH_XXPRIME_5 ^ 3527539))
	x = x*pow(_PyHASH_XXPRIME_1, -1, UINT64)%UINT64
	x = _PyHASH_XXROTATE_R(x)
	x -= acc
	x = x*pow(_PyHASH_XXPRIME_2, -1, UINT64)%UINT64
	#print(x)
	#3
	return x

def recover_number(x):
	if x[:2] == 'ff':
		return 0-int(x[2:],16)
	else:
		return int(x,16)

x0 = 529344067295497451
l = 3
print(reverse_hash(x0,l))
#302715549475208033

x0 = 0x69a20345a9b57143
l = 100
r100 = reverse_hash(x0,l)
print(hex(x0))
a100 = [2**64]*99+[r100]
print(hex(hash(tuple(a100))))


r = ["69a20345a9b57143", "41366612f2cb848", "ff41cb1c380af30f27", "ffaa373a0d221ade2", "523cddcc9704f1ce"]
for i in r:
	print(recover_number(i))

token = '{"token":"xxxxxxxxxxxxxxxx"}'
token2 = token[:-1]+', "passphrase": '+str(a100)+'}'
x = json.loads(token2)
print(x["passphrase"])
