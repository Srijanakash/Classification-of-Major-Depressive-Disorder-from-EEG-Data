# Classification-of-Major-Depressive-Disorder-from-EEG-Data

## Abstract

Electroencephalogram (EEG) is an electrophysiological monitoring method to record the electrical activity of the brain. EEG is most often used to diagnose epilepsy, which causes abnormalities in EEG readings. It is also used to diagnose sleep disorders, depth of anesthesia, coma, encephalopathy, brain death, and depression. Being one of the prevalent psychiatric disorders, depressive episodes of major depressive disorder (MDD) is often misdiagnosed or overlooked. Therefore, identifying MDD at earlier stages of treatment could help to facilitate efficient and specific treatment. In this article, Random Forest (RF) and Ant Colony Optimization (ACO) algorithm are used to reduce the number of features by removing irrelevant and redundant features. The selected features are then fed into k-nearest neighbors (KNN) and SVM classifiers, a mathematical tool for data classification, regression, function estimation, and modeling processes, in order to classify MDD and non-MDD subjects. The proposed method used Wavelet Transformation (WT) to decompose the EEG data into corresponding frequency bands, like delta, theta, alpha, beta and gamma. A total of 119 participants were recruited by the University of Arizona from introductory psychology classes based on survey scores of the Beck Depression Inventory (BDI). The performance of KNN and SVM classifiers is measured first with all the features and then with selected significant features given by RF and ACO.

## Dataset

119 participants were recruited by the University of Arizona from introductory psychology classes based on survey scores of the Beck Depression Inventory (BDI). All participants were between 18 and 25 years of age and had no history of head trauma or seizures and were not on any psychoactive medications. Controls had stable low BDI scores (<8) and had no self-reported history of MDD. Depressed participants had stable high BDI scores (>13) and met the criteria for MDD according to the Diagnostic and Statistical Manual of Mental Disorders, fourth standard EEG cap based on the extended 10-20 system of electrode positions using a NeuroScan EEG system (NeuroScan Lab, Charlotte, NC, USA) and were filtered and amplified using a bandpass filter 0.5-100Hz and sampling rate of 500Hz. Electrode impedances were maintained below 10kΩ throughout the experiment. Eye blink artifacts were removed using ICA. The data consists of 64 EEG micro-voltage rows, the 65th row contains HEOG and the 66th row contains VEOG values. VEOG and HEOG were recorded with two pairs of electrodes one placed above the right eye and the other 10mm from the lateral canthi. Some data may have a 67th column with EKG data as well. Voltages are referenced to a site anterior to the Fz section of the scalp. Out of 119 subjects 75 did not show characteristics of MDD while the rest 44 showed characteristics of MDD.

## Results and Discussion

The main objective of this article is to compare and find a good feature selection technique to remove non-relevant information thereby reducing the parameters of the classifier. Figure2 and Figure 3 show the feature importance of the electrodes and the frequency bands using random forest method respectively. From that feature importance, we then selected the top 15 electrodes out of 60 and top 3 frequency bands out of 5. We have also used ACO for selecting significant features. SVM and KNN classifiers are applied to those features selected by ACO and RF methods. It is easy to know the feature importance of the EEG electrodes and frequency bands using Random Forest rather than using any other techniques like ACO or PCA. Using these selected feature importance we are able to retrieve the original and information and improve the accuracy of the classifiers that predicts a subject being MDD or non-MDD. From Table 1, it is clear that the KNN classifier shows the best result when it is applied to the features selected by the random forest method using 3 frequency bands.

Different frequency bands depict different characteristics of an individual mental state which is shown in the following graph

### Figure 2
![Figure 2020-06-04 225049](https://user-images.githubusercontent.com/33724590/83796210-43d12b00-a6be-11ea-8ade-3bb5f00c3189.png)


So, all the 5 frequency bands are not required for analysis of an individual to identify MDD or non-MDD. The following graph shows the importance of the 5 Frequency Bands.


### Figure 3
![Figure 2020-06-04 225039](https://user-images.githubusercontent.com/33724590/83795964-e3da8480-a6bd-11ea-971c-037b179467bb.png)

It can be clearly seen that gamma, beta and delta have relatively more importance than alpha and theta frequency bands. Thus we select the top 3 frequency bands according to their importance and use those 3 bands in our proposed approach. 


The accuracy varies with the inclusion of the electrodes as follows: 

### Figure 4
![AccuracyNew](https://user-images.githubusercontent.com/33724590/83785149-84c14380-a6ae-11ea-904c-21ac139d508c.png)

These Electrodes are selected from the Importance Graph generated from Random Forest.  The above figure shows the performance of the classifier, one using 5 frequency bands and then using the top 3 significant frequency bands. The plot was made to illustrate the performance of the training and testing phase. It shows the performance of the classifier can be further improved using the top 3 frequency bands along with the top n electrodes. 

