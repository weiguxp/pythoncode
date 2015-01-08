def SaveRecord():
	with open('RecordSave.pk1', 'wb') as output:
		for record in myList:
			pickle.dump(record, output, -1)


def LoadRecords():
	with open('RecordSave.pk1', 'rb') as input:
		try:
			while True:
				recordS = pickle.load(input)
				myList.append(recordS)
		except EOFError:
			pass

		print myList[1]
		print myList[2]