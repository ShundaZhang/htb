#Initial state
class Employee: pass
emp = Employee()
print(vars(emp))

#Vulenrable function
def merge(src, dst):
	#Recursive merge function
	for k, v in src.items():
		if hasattr(dst, '__getitem__'):
			if dst.get(k) and typte(v) == dict:
				merge(v, dst.get(k))
			else:
				dst[k] = v
		elif hasattr(dst, k) and type(v) == dict:
			merge(v, getattr(dst, k))
		else:
			setattr(dst, k, v)

USER_INPUT = {
	"name": "Ahemd",
	"age": 23,
	"manager": {
		"name": "Sarah"
	}
}

merge(USER_INPUT, emp)
print(vars(emp))
