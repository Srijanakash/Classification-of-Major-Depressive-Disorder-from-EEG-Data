# Classification-of-Major-Depressive-Disorder-from-EEG-Data


The main objective of this article is to compare and find a good feature selection technique to remove non-relevant information thereby reducing the parameters of the classifier. According to the Random Forest feature importance, we have selected top 15 electrodes out of 60 and top 3 frequency bands out of 5. We have also used ACO for selecting significant features and comapred with the same. SVM and KNN classifiers are applied to those features selected by ACO and RF methods. It is easy to know the feature importance of the EEG electrodes and frequency bands using Random Forest rather than using any other techniques like ACO or PCA. Using these selected feature importance we are able to retrieve the original and information and improve the accuracy of the classifiers that predicts a subject being MDD or non-MDD.
Further details are given in the below link,

https://dl.acm.org/doi/10.1145/3396474.3396480
