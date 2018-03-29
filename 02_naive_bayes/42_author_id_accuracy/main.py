# coding: utf8
import sys
from sklearn.naive_bayes import GaussianNB
sys.path.append("../../tools")

from email_pre_processor import pre_process_email
from timer import Timer

# Get the email data.
features_train, features_test, labels_train, labels_test = pre_process_email()

# Create and train the classifier.
Timer.start()
classifier = GaussianNB()
classifier.fit(features_train, labels_train)
Timer.stop("⏱ Training time: ")

# Predict the test features.
Timer.start()
predicted_labels = classifier.predict(features_test)
Timer.stop("⏱ Predicting time: ")

# Calculate the accuracy.
accuracy = classifier.score(features_test, labels_test)
print("Accuracy: " + str(accuracy))
