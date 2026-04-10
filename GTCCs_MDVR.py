import librosa
import numpy as np
import pandas as pd
import os


def compute_gtcc(audio, sr, n_coeffs=13, n_fft=512, hop_length=256):
    """Compute GTCCs for a given audio signal"""
    try:
        # Compute short-time Fourier transform (STFT)
        stft = np.abs(librosa.stft(audio, n_fft=n_fft, hop_length=hop_length)) ** 2

        # Convert to Mel scale and apply log
        gtccs = librosa.feature.mfcc(S=librosa.power_to_db(stft), sr=sr, n_mfcc=n_coeffs)

        # Compute mean and standard deviation of GTCCs over time
        gtcc_mean = np.mean(gtccs, axis=1)
        gtcc_std = np.std(gtccs, axis=1)

        return np.concatenate((gtcc_mean, gtcc_std))  # Combine mean & std features
        #return gtcc_std
    except Exception as e:
        print(f"Error processing GTCC: {e}")
        return None


def process_audio_files(root_folder, label):
    """Recursively process all .wav files in the given root_folder"""
    data = []

    # Walk through all subdirectories
    for dirpath, _, filenames in os.walk(root_folder):
        for file_name in filenames:
            if file_name.endswith(".wav"):  # Process only .wav files
                file_path = os.path.join(dirpath, file_name)
                print(f"Processing {label}: {file_path}")

                # Load the audio file
                audio, sr = librosa.load(file_path, sr=16000)
                print(f"Loaded {file_name}: {len(audio)} samples at {sr} Hz")

                # Compute GTCCs
                gtcc_features = compute_gtcc(audio, sr)

                if gtcc_features is not None:
                    patient_id = file_path  # Get patient folder name
                    data.append([patient_id] + list(gtcc_features) + [label])


                else:
                    print(f"Skipping {file_name} due to GTCC extraction failure.")

    return data



# Define main folders for HC (Healthy Control) and PD (Parkinson’s Disease)
#hc_folder = "MDVR_KCL/ReadText/HC"
#pd_folder = "MDVR_KCL/ReadText/PD"

hc_folder = "Dataset_MDVR_KCL/MDVR/ReadText/chunks/HC"
pd_folder = "Dataset_MDVR_KCL/MDVR/ReadText/chunks/PD"


#r"Dataset_MDVR_KCL/MDVR/ReadText/HC", r"Dataset_MDVR_KCL/MDVR/ReadText/PD"

# Ensure paths exist
if not os.path.exists(hc_folder) or not os.path.exists(pd_folder):
    print("Error: One or both folders do not exist!")
    exit()

# Process all files in HC and PD folders
hc_data = process_audio_files(hc_folder, 0)
pd_data = process_audio_files(pd_folder, 1)

# Combine data
data = hc_data + pd_data

# Convert to Pandas DataFrame
if data:
    columns = ["voiceID"] + [f"GTCC_Mean_{i + 1}" for i in range(13)] + [f"GTCC_Std_{i + 1}" for i in
                                                                                    range(13)] + ["label"]
    #columns = ["voiceID"] + [f"GTCC_MeanFeature{i + 1}" for i in range(13)] + ["label"]
    #columns = ["voiceID"] + [f"GTCC_STDfeature{i + 1}" for i in range(13)] + ["label"]
    df = pd.DataFrame(data, columns=columns)

    # Save to CSV
    output_csv = "Dataset_MDVR_KCL/MDVR/ReadText/chunks/MDVRReadText_GTCC_feature_chunks.csv"
    #output_csv = "Dataset_MDVR_KCL/MDVR/ReadText/chunks/GTCC_Mean_feature_chunks.csv"
    #output_csv = "Dataset_MDVR_KCL/MDVR/ReadText/chunks/GTCC_Std_feature_chunks.csv"
    df.to_csv(output_csv, index=False)
    print(f"Saved GTCC features to {output_csv}")
else:
    print("No valid data extracted. Check file paths and audio content.")
