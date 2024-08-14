# Model Card - Salary Prediction

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Created by Rob Lau
Random Forest Classifier

## Intended Use
Predict if the individual makes under 50k a year or over 50k

## Training Data
used census.csv provided by udacity.  additional detail can be found at the following URL https://archive.ics.uci.edu/dataset/20/census+income

## Evaluation Data
The evaluation data consisted of 30% of the census data

## Metrics
the primary metrics are Precision, Recall and F1
Precision 0.7395
Recall 0.6198
F1 0.6744

## Ethical Considerations
The census data contains some features which could be somewhat biased, such as race and gender.  These should be avoided for ethical reasons if possible

## Caveats and Recommendations
Ensure the training data is of the highest quality, perform regular monitoring