#!/usr/bin/python3.9

'''
#define _PyHASH_XXPRIME_1 ((Py_uhash_t)2654435761UL)
#define _PyHASH_XXPRIME_2 ((Py_uhash_t)2246822519UL)
#define _PyHASH_XXPRIME_5 ((Py_uhash_t)374761393UL)
#define _PyHASH_XXROTATE(x) ((x << 13) | (x >> 19))  /* Rotate left 13 bits */

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

_PyHASH_XXPRIME_1=2654435761
_PyHASH_XXPRIME_2=2246822519
_PyHASH_XXPRIME_5=374761393
def _PyHASH_XXROTATE(x):
	return (((x << 13) & 0xFFFFFFFF) | (x >> 19)) 

def _PyHASH_XXROTATE_R(x):
	return (((x << 19) & 0xFFFFFFFF) | (x >> 13)) 


def myhash(x):
	acc = _PyHASH_XXPRIME_5
	for i in range(len(x)):
		lane = x[i]
		acc += lane * _PyHASH_XXPRIME_2
		acc = _PyHASH_XXROTATE(acc)
		acc *= _PyHASH_XXPRIME_1

	acc += len(x) ^ (_PyHASH_XXPRIME_5 ^ 3527539)
	return acc

print(hash(tuple([1,2,3])))
print(myhash(tuple([1,2,3])))

