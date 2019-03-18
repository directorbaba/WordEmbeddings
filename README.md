# WordEmbeddings
Applied word embedding using fasttext

Included the Data-set from the given link :https://www.kaggle.com/uciml/sms-spam-collection-dataset

Initially preprocessed the data using the following command:
 
 cat spam.csv | sed -e "s/\([.\!?,'/()]\)/ \1 /g" | tr "[:upper:]" "[:lower:]" > spam.csv
  
Then, divide the data into two parts:
  
 Total Sample Data ( 5572) = Training Data (4072) + Test Data (1500)
 head -n 4072 spam.csv > Train.csv
 tail -n 1500 spam.csv > Test.csv

Classify the data using supervised learning through fasttext. 
  
 classifier= fasttext.supervised('Train.csv', 'model', label_prefix='label_', lr=1.0, dim=100, epoch=25)
  
Once the model was trained, it got 98% of precision onto the test data.


Now run input.py, take the input.

I have clasified on the basis of 60:40, 60% weightage to maximum iterations and 40% weightage to the probability calculation.



