import pandas as pd
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC

def main():

  dataset=pd.read_csv("LOTTOMAX.csv")
  dataset.dropna(how='all', inplace = True)
  X = dataset.drop(labels = ["PRODUCT","DRAW_NUMBER","SEQUENCE_NUMBER","DRAW_DATE","BONUS_NUMBER"], axis = 1)
  Y = dataset["DRAW_NUMBER"]
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4, random_state=1)
  clf = svm.SVC(C=1.0, cache_size=49, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=2, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.01, verbose=False)

  results =clf.fit(X_test[0:100], Y_test[0:100])
  results=clf.decision_function(X_test)
  #score=results.score(X_test)

  pred=results.predict(X_test)


 # print(score)
  print(pred)
if __name__ == '__main__':
    main()
