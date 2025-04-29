# 🤖 Python ML-Based Whistle Detection

This version of the project uses **machine learning** and **audio feature extraction** to detect cooker whistles.

## 🔍 Features Used
- MFCC (Mel Frequency Cepstral Coefficients)
- ZCR (Zero Crossing Rate)
- RMS (Root Mean Square Energy)
- MLP Classifier (from scikit-learn)

## 🗂 Project Structure
ml_python_version/ ├── data/ │ ├── whistle/ # Whistle audio segments (not pushed to GitHub) │ ├── non_whistle/ # Non-whistle segments (not pushed to GitHub) │ └── Whistle_Features.csv ├── models/ │ └── Whistle_Detector_Model.pkl ├── scripts/ │ ├── extract_and_prepare.py │ └── train_and_evaluate.py ├── realtime/ │ └── RealTimeDetection.py ├── requirements.txt └── README.md

## 🎧 Dataset Note

The `data/whistle/` and `data/non_whistle/` folders are large and excluded from this repo.

📁 You can download them here:  
[Google Drive Link – Whistle and Non-Whistle Audio Segments](https://drive.google.com/drive/folders/1g0p8dNe2xTWcaKZDtPi1t3BY7Fgyd0JJ?usp=sharing )


## 🚀 How to Use
1. Run `scripts/extract_and_prepare.py` to extract features and generate dataset
2. Run `scripts/train_and_evaluate.py` to train and save the model
3. Run `realtime/RealTimeDetection.py` to test live whistle detection using microphone

## 📦 Dependencies
See `requirements.txt`

## ✍️ Author
Yash Singh
