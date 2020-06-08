# Classification-of-Major-Depressive-Disorder-from-EEG-Data

# Abstract

Electroencephalogram (EEG) is an electrophysiological monitoring method to record the electrical activity of the brain. EEG is most often used to diagnose epilepsy, which causes abnormalities in EEG readings. It is also used to diagnose sleep disorders, depth of anesthesia, coma, encephalopathy, brain death, and depression. Being one of the prevalent psychiatric disorders, depressive episodes of major depressive disorder (MDD) is often misdiagnosed or overlooked. Therefore, identifying MDD at earlier stages of treatment could help to facilitate efficient and specific treatment. In this branch, missing data imputation has been done.

# Missing Data

Missing data is a common problem and one of many factors comprising data quality. Data quality of a dataset depends on the intended use of the data, meaning a dataset may be of good quality for one use case, but not for another (Han, Pei, and Kamber 2011)
Missing data or missing values are values containing false data, or no value at all (Missing data 2017). A value in an object might be missing, or even the whole object. Sometimes, whole records are missing from a dataset. Having values that are missing in a dataset may affect the quality of the data, and therefore affect information to be gathered from the dataset. Missing data is a common problem within industrial and medical databases (Lakshminarayan et al. 1996), and is according to (Potthoff et al. 2006) "a source of serious problems in statistical analyses of clinical trials and of other medical studies". It is not uncommon to find datasets containing up to 50% missing values (Farhangfar, Kurgan, and Dy 2008). 

# Methodology
Usually if the missing data is within the bounds of 5-10% of the entire data, simple imputation methods such as replacing the NaN values with the mean, median and mode would suffice without majorly affecting the performance and accuracy of the models being developed. 
The results achieved by this simple method of imputation is as follows:
Random Forest Accuracy on Test Set: 62.50%
SVM Accuracy on Test Set: 66.67%
KNN Accuracy on Test Set: 66.67%

However, a better approach for imputing the missing values would be to estimate the maximum likelihood at that point of series data. 
Maximum Likelihood (ML) is a model-based technique for estimating parameters of a statistical model. In ML, observed values are used to impute missing values. ML dates back to 1912 when Ronald Fisher recommended, analyzed and popularized the technique (Maximum Likelihood Estimation 2017). When imputing, ML find the set of attributes that produces the highest log-likelihood. In other words, the method identifies the value that is most likely by looking at the observed data.  We’ve implemented maximum likelihood using K-Nearest Neighbour Regressor. K-nearest Neighbor can predict both discrete and continuous attributes. 

# Dataset

119 participants were recruited by the University of Arizona from introductory psychology classes based on survey scores of the Beck Depression Inventory (BDI). All participants were between 18 and 25 years of age and had no history of head trauma or seizures and were not on any psychoactive medications. Controls had stable low BDI scores (<8) and had no self-reported history of MDD. Depressed participants had stable high BDI scores (>13) and met the criteria for MDD according to the Diagnostic and Statistical Manual of Mental Disorders, fourth standard EEG cap based on the extended 10-20 system of electrode positions using a NeuroScan EEG system (NeuroScan Lab, Charlotte, NC, USA) and were filtered and amplified using a bandpass filter 0.5-100Hz and sampling rate of 500Hz. Electrode impedances were maintained below 10kΩ throughout the experiment. Eye blink artifacts were removed using ICA. The data consists of 64 EEG micro-voltage rows, the 65th row contains HEOG and the 66th row contains VEOG values. VEOG and HEOG were recorded with two pairs of electrodes one placed above the right eye and the other 10mm from the lateral canthi. Some data may have a 67th column with EKG data as well. Voltages are referenced to a site anterior to the Fz section of the scalp. Out of 119 subjects 75 did not show characteristics of MDD while the rest 44 showed characteristics of MDD.

# Results

We had a sample dataset of yeast genomes in which we had applied this method and found the mean RMSE to be 0.055, which seems to be quite satisfactory post which we had implemented the method on our dataset.  
The results found were as follows:
RMSE value for k= 2 is: 0.48947250518628044
Validation MAE for best value of max_leaf_nodes: 0.21

