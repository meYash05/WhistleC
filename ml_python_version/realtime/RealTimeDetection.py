import sounddevice as sd
import numpy as np
import librosa
import joblib
import time

# ---- CONFIG ----
duration = 3  # Listening window in seconds
samplerate = 22050
model_path = r"C:\Users\Yash Singh\Desktop\WhistleML\Whistle_Detector_Model.pkl"

# ---- LOAD MODEL ----
model = joblib.load(model_path)

# ---- INIT COUNTER ----
whistle_count = 0

print("🎤 Listening for whistles... Press Ctrl+C to stop.")

try:
    while True:
        # Record audio for 'duration' seconds
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
        sd.wait()
        audio = np.squeeze(audio)

        # Calculate RMS energy (for noise filtering)
        rms_energy = np.sqrt(np.mean(audio**2))
        print(f"📈 RMS Energy: {rms_energy:.5f}")

        if rms_energy > 0.01:  # Threshold to ignore silence/background
            mfcc = librosa.feature.mfcc(y=audio, sr=samplerate, n_mfcc=13)
            mfcc_mean = np.mean(mfcc, axis=1).reshape(1, -1)

            prediction = model.predict(mfcc_mean)

            if prediction[0] == 1:
                whistle_count += 1
                print(f"🎯 Whistle detected! Total Count: {whistle_count}")
            else:
                print("😶 No whistle detected.")
        else:
            print("😶 Very low sound detected, skipping...")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n🛑 Stopped Listening.")
    print(f"🔔 Total Whistles Detected: {whistle_count}")