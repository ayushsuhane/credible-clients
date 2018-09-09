# credible-clients

This repository contains a small pre-task for potential ML team
members for [UBC Launch Pad](https://www.ubclaunchpad.com).


## Overview

The dataset bundled in this repository contains information about credit card
bill payments, courtesy of the [UCI Machine Learning Repository][UCI]. Your task
is to train a model on this data to predict whether or not a customer will default
on their next bill payment.

Most of the work should be done in [**`model.py`**](model.py). It contains a
barebones model class; your job is to implement the `fit` and `predict` methods,
in whatever way you want (feel free to import any libraries you wish). You can
look at [**`main.py`**](main.py) to see how these methods will be called. Don't
worry about getting "good" results (this dataset is _very tough_ to predict on)
— treat this as an exploratory task!

To run this code, you'll need Python and three libraries: [NumPy], [SciPy],
and [`scikit-learn`]. After invoking **`python main.py`** from your shell of
choice, you should see the model accuracy printed: approximately 50% if you
haven't changed anything, since the provided model predicts completely randomly.

## Instructions

Here are the things you should do:

1. Fork this repo, so we can see your code!
2. Install the required libraries using `pip install -r requirements.txt` (if needed).
3. Ensure you see the model's accuracy/precision/recall scores printed when running `python main.py`.
4. Replace the placeholder code in [`model.py`](model.py) with your own model.
5. Fill in the "write-up" section below in your forked copy of the README.

_Good luck, and have fun with this_! :rocket:


## Write-up

It was a good exercise to test different algorithms on the given dataset. Since the problem at hand was a supervised machine learning problem,
I listed the major algorithms which are typically used to solve such problems. The success rate for different algorithms is
dependent on the distribution of dataset. A good approach is to identify few algorithms and pit them against each other. Various metric scores
such as accuracy, precision, recall among others can be used to judge the performance of the algorithm. I tried Linear Regression, Logistic Regression,
K-NearestNeighbours, ArtificialNeural Network, Naive Bayes and Random Forest to check theier performance. While every method can be optimized within itself,
the preliminary model using Random Forest turned out to be the best in terms of the selected metrics.

While scores associated with all the above mentioned methods can be found in ``TestModel.ipynb``, the scores with Random Forest are as follows:
Accuracy : 80.547 %
Precision : 59.333 %
Recall : 32.821 %


## Data Format

`X_train` and `X_test` contain data of the following form:

| Column(s) | Data |
| :-------: | ---- |
| 0         | Amount of credit given, in dollars |
| 1         | Gender (_1 = male, 2 = female_) |
| 2         | Education (_1 = graduate school; 2 = university; 3 = high school; 4 = others_) |
| 3         | Marital status (_1 = married; 2 = single; 3 = others_) |
| 4         | Age, in years |
| 5–10      | History of past payments over 6 months (_-1 = on-time; 1 = one month late; …_) |
| 11–16     | Amount of previous bill over 6 months, in dollars |
| 17–22     | Amount of previous payment over 6 months, in dollars |

`y_train` and `y_test` contain a `1` if the customer defaulted on their next
payment, and a `0` otherwise.


[UCI]: https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients
[NumPy]: http://www.numpy.org
[SciPy]: https://www.scipy.org
[`scikit-learn`]: http://scikit-learn.org
