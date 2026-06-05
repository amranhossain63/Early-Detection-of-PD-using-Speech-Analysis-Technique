# Early-Detection-of-PD-using-Speech-Analysis-Technique

## Machine Learning Approaches to Early Detection of  Parkinson’s Disease Using Speech Analysis Technique

### Abstract

**Background**: Parkinson’s disease (PD) is a progressive neurodegenerative disorder that affects millions globally, particularly those in the elderly population. Several occupational exposures typical of maritime environments are recognized or suspected risk factors for PD, warranting attention within occupational health frameworks. The disease is characterized by motor symptoms such as tremor, rigidity, and bradykinesia, as well as non-motor impairments including speech abnormalities. Objective: Early diagnosis is crucial for effective disease management but remains challenging due to symptoms overlapping with normal aging and other neurological conditions. This study presents a machine learning (ML)-based approach for the early diagnosis of PD using speech signal analysis. Methods: We employed six supervised ML classifiers to differentiate between PD patients and healthy controls based on vocal features. The experimental dataset, MDVR-KCL, consists of speech recordings from both reading tasks and spontaneous dialogs, collected via mobile devices. From these recordings, we extracted Mel-Frequency Cepstral Coefficients (MFCCs), Gammatone Frequency Cepstral Coefficients (GTCCs), and acoustic features such as jitter, shimmer, and harmonic-to-noise ratio. These features capture a broad range of prosodic, spectral, and articulatory characteristics associated with PD-related speech impairments. Speaker diarization was applied in spontaneous dialog recordings to separate participant speech. Hyperparameter tuning was performed using GridSearchCV with 10-fold cross-validation, while final model evaluation was conducted using Leave-One-Subject-Out Cross-Validation (LOSOCV) to ensure subject-independent performance assessment. Results: In the read-text task, the SVM model performed exceptionally, yielding 95.45% accuracy, 94.62% sensitivity, 95.97% specificity, an F1-score of 94.12%, and an AUC of 0.98 with an MCC value of 0.90, for GTCCs with the acoustic features. In the spontaneous dialog task, the XGB model demonstrated the highest overall performance across all metrics, with a test accuracy of 83.7%, a sensitivity of 76.3.9%, a specificity of 88.9%, an F1-score of 79.5%, an AUC value of 0.88, and an MCC value of 0.66. Conclusions: Comparable results were obtained on both spontaneous dialog and reading speech subsets, demonstrating the robustness of the approach across different speaking contexts. These results demonstrate the effectiveness of integrating cepstral and acoustic features with machine learning models for non-invasive PD classification. The findings support the use of speech-based digital biomarkers in early PD detection and highlight the potential for developing scalable tools. This work highlights the potential of speech-based digital diagnostics to support clinical decision-making and improve patient outcomes.


###  Dataset
- Publicly accessible Mobile Device Voice Recordings at King's College London (MDVR-KCL)
- Total of 37 participants, 21 healthy controls and 16 PD Patients
-  Speech recordings from healthy controls and PD patients; including early and advanced stages.
- The recordings were acquired using “Toggle Recording App” installed on a Moto G4 smartphone, resulting in high-quality audio files with a sampling rate of 44.1 kHz and a bit depth of 16 bits.
- Participants perform two speech tasks.
- First task, everyone read aloud the standardized paragraph “The North Wind and the Sun.” 
- some participants were also asked to read an additional technical excerpt titled “Tech. Engin. Computer Applications in Geograph”.
- The second task involved a spontaneous dialog between the participant and the examiner, during which open-ended questions were posed regarding topics such as local traffic, places of interest, and personal preferences. This format was designed to capture both structured and natural speech patterns.
- Each audio file is labeled with metadata including the participant ID, Hoehn and Yahr (H&Y) stage, and Unified Parkinson’s Disease Rating Scale (UPDRS) scores for sections II-5 and III-18. For example, the file name “ID02_pd_1_2_1.wav” refers to participant 02, diagnosed with PD at H&Y stage 1 (indicative of early-stage PD), with a UPDRS II-5 score of 2 and a UPDRS III-18 score of 1.




#### Feature extraction class containing the methods to extract features from voice sample
- MFCC : Mel-Frequency Cepstral Coefficients.
- GTCC : Gammatone Frequency Cepstral Coefficients.
- Pitch: 'meanF0Hz', Mean of the fundamental frequency	Numerical
- Pitch: 'stdevF0Hz', SD	Standard deviation of the fundamental frequency	Numerical
- 'HNR', Mean harmonics-to-noise ratio	Numerical
- Jitter: 'localJitter', 	Local variation in pitch	Numerical
- Jitter: 'localabsoluteJitter', absolute	Absolute jitter	Numerical
- Jitter: 'rapJitter', RAP	Relative average perturbation	Numerical
- Jitter: 'ppq5Jitter', Five-point period perturbation quotient	Numerical
- Shimmer: 'localShimmer', Local variation in amplitude	Numerical
- Shimmer:  'localdbShimmer', Shimmer in decibels	Numerical
- Shimmer: 'apq3Shimmer', Three-point amplitude perturbation quotient	Numerical
- Shimmer:  'apq5Shimmer' Five-point amplitude perturbation quotient	Numerical




##### Feature Extract funtion
- **split_into_chunks**  Split audio signal into small chunks based on : must be silent for at least half a second and consider it silent if quieter than -16 dBFS
- **extract_mfccfeatures_from_chunks** extract MFCC from smaller audio files. (13 Coefficients )
- **extract_features_from_chunks**   Extract Audio features. 


#### GTCC Feature Extraction
- Used a separate python file to extract GTCC features
- 13 Coefficients 







***Keywords:** Parkinson’s disease (PD); machine learning (ML); voice; speech; speaker diarization; spontaneous dialogue 
