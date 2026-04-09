# Early-Detection-of-PD-using-Speech-Analysis-Technique

## Machine Learning Approaches to Early Detection of  Parkinson’s Disease Using Speech Analysis Technique



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
