# Classification-of-Major-Depressive-Disorder-from-EEG-Data

# Abstract

Electroencephalogram (EEG) is an electrophysiological monitoring method to record the electrical activity of the brain. EEG is most often used to diagnose epilepsy, which causes abnormalities in EEG readings. It is also used to diagnose sleep disorders, depth of anesthesia, coma, encephalopathy, brain death, and depression. Being one of the prevalent psychiatric disorders, depressive episodes of major depressive disorder (MDD) is often misdiagnosed or overlooked. Therefore, identifying MDD at earlier stages of treatment could help to facilitate efficient and specific treatment. The proposed method used Wavelet Transformation (WT) to decompose the EEG data into corresponding frequency bands, like delta, theta, alpha, beta and gamma. A total of 119 participants were recruited by the University of Arizona from introductory psychology classes based on survey scores of the Beck Depression Inventory (BDI).
Firefly algorithm along with SVM classifier has been used as a wrapper method for feature selection and further fuzzy rule based classification has been done using subtractive clustering.

# Feature selection
Feature selection is the process of reducing the number of input variables when developing a predictive model.
It is desirable to reduce the number of input variables to both reduce the computational cost of modeling and, in some cases, to improve the performance of the model.

# Firefly algorithm
In mathematical optimization, the firefly algorithm is a metaheuristic proposed by Xin-She Yang and inspired by the flashing behavior of fireflies.
In pseudocode the algorithm can be stated as: 
```
Begin
    1) Objective function: 
f ( x ) , x = ( x 1 , x 2 , . . . , x d ) {\displaystyle f(\mathbf {x} ),\quad \mathbf {x} =(x_{1},x_{2},...,x_{d})} 
;
    2) Generate an initial population of fireflies 
x i ( i = 1 , 2 , … , n ) {\displaystyle \mathbf {x} _{i}\quad (i=1,2,\dots ,n)} 
;.
    3) Formulate light intensity I so that it is associated with 
f ( x ) {\displaystyle f(\mathbf {x} )} 

       (for example, for maximization problems, 
I ∝ f ( x ) {\displaystyle I\propto f(\mathbf {x} )} 
 or simply 
I = f ( x ) {\displaystyle I=f(\mathbf {x} )} 
;)
    4) Define absorption coefficient γ

    While (t < MaxGeneration)
        for i = 1 : n (all n fireflies)
            for j = 1 : i (n fireflies)
                if (
I j > I i {\displaystyle I_{j}>I_{i}} 
),
                    Vary attractiveness with distance r via 
exp ⁡ ( − γ r ) {\displaystyle \exp(-\gamma \;r)} 
;
                    move firefly i towards j;                
                    Evaluate new solutions and update light intensity;
                end if 
            end for j
        end for i
        Rank fireflies and find the current best;
    end while

    Post-processing the results and visualization;

end
```
# Feature selection Methodology:
In this repository, a wrapper based method of firefly algorithm and SVM Classifier has been used for feature selection.

# Fuzzy Classification
In recent years, fuzzy models have been used widely because they are able to work with imprecise data, 
handle the complex nonlinear problems and acquired knowledge with these models is more interpretable 
than the black-box models. Fuzzy Rule-Based Classification System (FRBCS) is a special case of fuzzy 
modeling and focuses on finding a compact set of fuzzy if-then classification rules to model the input 
output behaviour of the system. In the design of FRBCS, construction of rule-base is the most challenging 
problem. It is desirable that the rule-base covers all the states of the system and at the same time, the 
number of rules should be kept low to increase the generalizing ability of the model, and to ensure a 
compact and transparent model. 
Many approaches have been proposed to construct the rule-base from numerical data. These include 
heuristic approaches , neuro-fuzzy techniques, genetic algorithms, clustering methods and data mining techniques . Clustering-based rule extraction methods help avoid combinatorial explosion of rules with increasing dimension of the input space, because the resultant rules 
are scattered in the input space rather than placed according to grid-like partitions in the input space. Each 
cluster can be considered as a fuzzy rule and essentially identifies a region in the data space that contains a 
sufficient mass of data to support the existence of a fuzzy input output relationship.

In this repository subtractive clustering has been used for rule base generation and classification.
# Dataset

119 participants were recruited by the University of Arizona from introductory psychology classes based on survey scores of the Beck Depression Inventory (BDI). All participants were between 18 and 25 years of age and had no history of head trauma or seizures and were not on any psychoactive medications. Controls had stable low BDI scores (<8) and had no self-reported history of MDD. Depressed participants had stable high BDI scores (>13) and met the criteria for MDD according to the Diagnostic and Statistical Manual of Mental Disorders, fourth standard EEG cap based on the extended 10-20 system of electrode positions using a NeuroScan EEG system (NeuroScan Lab, Charlotte, NC, USA) and were filtered and amplified using a bandpass filter 0.5-100Hz and sampling rate of 500Hz. Electrode impedances were maintained below 10kΩ throughout the experiment. Eye blink artifacts were removed using ICA. The data consists of 64 EEG micro-voltage rows, the 65th row contains HEOG and the 66th row contains VEOG values. VEOG and HEOG were recorded with two pairs of electrodes one placed above the right eye and the other 10mm from the lateral canthi. Some data may have a 67th column with EKG data as well. Voltages are referenced to a site anterior to the Fz section of the scalp. Out of 119 subjects 75 did not show characteristics of MDD while the rest 44 showed characteristics of MDD.
