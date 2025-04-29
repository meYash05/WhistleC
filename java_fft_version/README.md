# 🔧 Java FFT-Based Whistle Detection

This version of the project implements whistle detection using **Fast Fourier Transform (FFT)** in Java.

## 📌 Features
- Analyzes audio frequency to detect pressure cooker whistles
- Pure Java implementation
- Based on static signal processing logic (non-ML)

## 🗂 Project Structure
java_fft_version/ ├── src/ │ └── main/ │ └── java/ │ └── │ └── WhistleC.java # Main detection logic using FFT ├── pom.xml # Maven build config └── README.md


## 💡 How It Works
1. Audio signal is converted into frequency domain using FFT
2. Frequency bands are scanned for whistle signature
3. Detected whistles are counted based on thresholding

## 🚀 How to Run
- Import the project into any Java IDE (like IntelliJ or Eclipse)
- Make sure dependencies (if any) in `pom.xml` are resolved
- Compile and run `WhistleC.java`

## ✍️ Author
Yash Singh
