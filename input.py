import fasttext

model = fasttext.load_model('model.bin')			# getting the model

x = raw_input()
label = model.predict_proba(x)					# getting input and predicting the labels upon modals

ham_prob = []							# storing ham probability of each label
spam_prob = []							# storing spam probability of each label
ham_count = []							# count of label on each iteration
total_ham = 0							# total count of ham iterations
spam_count = []
total_spam = 0

spam_calc = 0							# spam_calc is average of spam label probabilities
ham_calc = 0							# ham_calc is average of ham label probabilities

for i in range(0,len(label)):
	for j in range(0,len(label[i])):			# getting list out of dictionaries
		temp1 = label[i][j][0]				# temp1 specifies label_ham, label_spam
		temp2 = label[i][j][1]				# temp2 specifies probability of tag in temp1

		if(temp1 == 'label_ham'):			# if temp1 = label_ham, update values accordingly
			ham_prob.append(temp2)
			spam_prob.append(1-temp2)
			ham_count.append(1)
			spam_count.append(0)
			total_ham += 1

		if(temp1 == 'label_spam'):
			ham_prob.append(1-temp2)
			spam_prob.append(temp2)
			ham_count.append(0)
			spam_count.append(1)
			total_spam += 1		

		

for k in range(0, len(ham_count)):
	spam_calc += spam_prob[k]*spam_count[k]
	ham_calc += ham_prob[k]*ham_count[k]
	
spam_calc /= total_spam						# final average values
ham_calc /= total_ham

spam_possibility = (0.6*total_spam) + (0.4*spam_calc)		# calculating possibility on weightage
ham_possibility = (0.6*total_ham) + (0.4*ham_calc)

if(spam_possibility > ham_possibility):
	print("The message contains spam elements")
else:
	print("The message is clean")

# print(ham_possibility)
# print(spam_possibility)
# print(total_ham)
# print(total_spam)
# print(ham_prob)
# print(spam_prob)
# print(ham_count)
# print(spam_count)

