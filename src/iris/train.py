
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import joblib
import os

PWD = os.path.dirname(os.path.abspath(__file__))


def main():

    # load iris dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # train model
    clf = LogisticRegression()
    clf.fit(X, y)

    # persistent model
    model_path = os.path.join(PWD, 'iris_model.pkl')
    joblib.dump(clf, model_path)


if __name__ == '__main__':
    main()
