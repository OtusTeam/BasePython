import librosa
import numpy as np

f_name = "SineWaveMinus16.wav"
audio_native, _ = librosa.load(f_name, sr=44100, mono=False)
print(type(audio_native), len(audio_native), audio_native.dtype, audio_native.shape)

print(audio_native)
left, right = audio_native
print(left.max())
print(np.amax(left))
print(20 * np.log10(np.amax(left)))

percents = (1, 5, 10, 25, 50, 75, 95, 99)
left_stat = np.percentile(np.abs(left), percents)
print(dict(zip(percents, left_stat)))
