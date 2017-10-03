import numpy as np

def fileParse(file_name, label_index, encoding):
	d = np.loadtxt(file_name, delimiter="\t")
	
	""" format: xorSamples = [[[0, 0], [0]], [[0, 1], [1]], [[1, 1], [0]], [[1, 0], [1]]] """

	#76 columns
	#varying number of rows
	#77th column contains gesture

	result = []
	expectedOutput = []
	for i in range(len(d)):
		expectedOutput = d[i][label_index]
		print expectedOutput
		outputEncoding = oneHot(expectedOutput, encoding)
		givenInput = d[i][0:(label_index-1)]
		result += [[givenInput, outputEncoding]]
	print result

def oneHot(value, max):
	encoding = np.zeros(max)
	encoding[value-1] = 1
	return encoding

#sliding window implementation
def main2():
	return 5


fileParse("input.txt", 76, 15)