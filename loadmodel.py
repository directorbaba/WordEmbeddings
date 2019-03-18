import fasttext

classifier = fasttext.supervised('Train.csv', 'model', label_prefix='label_', lr=1.0, dim=100, epoch=25)

result= classifier.test('Test.csv')

print(result.precision)
print(result.recall)
print(result.nexamples)
