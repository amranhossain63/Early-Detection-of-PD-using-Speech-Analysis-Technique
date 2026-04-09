# Early-Detection-of-PD-using-Speech-Analysis-Technique

## Machine Learning Approaches to Early Detection of  Parkinson’s Disease Using Speech Analysis Technique

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




##### Feature Extract contain funtion
- **split_into_chunks**  Split audio signal into small chunks based on : must be silent for at least half a second and consider it silent if quieter than -16 dBFS
- **extract_mfccfeatures_from_chunks** extract MFCC from smaller audio files.
- **extract_features_from_chunks**   Extract Audio features. 








***Keywords:** Parkinson’s disease (PD); machine learning (ML); voice; speech; speaker diarization; spontaneous dialogue 
