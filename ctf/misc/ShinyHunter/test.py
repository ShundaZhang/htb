import random

#i = 0
i = 2**32 - 1
natures = ["Adamant", "Bashful", "Bold", "Brave", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty", "Impish", "Jolly", "Lax", "Lonely", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid"]

#while i < 2**22:
while i > 0:
	random.seed(i)
	tid = random.randint(0,65535)
	sid = random.randint(0,65535)
	for seedi in range(3):
		random.seed(i+seedi)
		for _ in range(6):
			random.randint(20,31)
		random.choice(natures)
		pid = random.randint(0,2**32-1)
		if ((tid ^ sid) ^ (pid & 0xFFFF) ^ (pid >> 16)) < 8:
			print('Found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
			print(f'seed: {i} + choice: {seedi}')
	#i += 1
	i -= 1
	#print(f'{i} Not Found...')
