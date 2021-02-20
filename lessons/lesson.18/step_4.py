import librosa
import numpy as np

f_name = "SineWaveMinus16.wav"
audio_native, _ = librosa.load(f_name, sr=44100, mono=False)
print(type(audio_native), len(audio_native), audio_native.dtype, audio_native.shape)
# print(dir(audio_native))
print(audio_native.ndim, audio_native.size, audio_native.itemsize)
# shape (2, 44100) -> (2, 2646000)
# RGB -> shape (3, 1920, 1080)

print(audio_native)
left, right = audio_native
print(left.shape, left.size, left)
print(right.shape, right.size, right)

frames = zip(left, right)
print(next(frames))
print(next(frames))

frame_1 = audio_native[:, 0]
print(frame_1)
print(audio_native[0, 0])  # [0][0]

left_avg = np.square(left).sum() / left.size
print(np.sqrt(left_avg))

# left_avg = sum(el ** 2 for el in left) / len(left)
