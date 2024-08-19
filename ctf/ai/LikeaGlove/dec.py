import gensim.downloader as api

# Load the GloVe model
glove_model = api.load("glove-twitter-25")

# Read and process each line in the file
with open('chal.txt', 'r', encoding='utf-8') as file:
	lines = file.readlines()

results = []

for line in lines:
	# Parse the analogy structure: "Like X is to Y, Z is to?"
	parts = line.split(", ")
	if len(parts) == 2:
		X_Y_part = parts[0].strip().split(" is to ")
		Z_part = parts[1].strip().replace(" is to?", "").strip()

		if len(X_Y_part) == 2:
			X = X_Y_part[0].replace("Like ", "").strip()
			Y = X_Y_part[1].strip()
			Z = Z_part

			vec1 = glove_model[X]
			vec2 = glove_model[Y]
			target = glove_model[Z]

			analogy_vector = target + (vec2 - vec1)
			result = glove_model.similar_by_vector(analogy_vector, topn = 1)
			results.append(results[0][0])

# Print the results
print(''.join(results))


#htb{h４rm０n１ou５_hymn_０f_h１ghd１m３ns１０n４l_subl１me_５ymph０ny_０f_num３r１cal_nuanc３_１n_tr３mend０u５_t４p３stry_０f_t３xtu４l_７r４n５f０rma７ion}
#htb{h4rm0n1ou5_hymn_0f_h1ghd1m3ns10n4l_subl1me_5ymph0ny_0f_num3r1cal_nuanc3_1n_tr3mend0u5_t4p3stry_0f_t3xtu4l_7r4n5f0rma7ion}
