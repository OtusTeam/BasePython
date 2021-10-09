import librosa
import numpy as np

#
f_name = "SineWaveMinus16.wav"
audio_native, _ = librosa.load(f_name, sr=44100, mono=False)
#

print(type(audio_native), len(audio_native), audio_native.ndim,
      audio_native.dtype, audio_native.shape)
# (3, 1920, 1080)

# print(dir(audio_native))
# print(audio_native.ndim, audio_native.size, audio_native.itemsize)
# shape (2, 44100) -> (2, 2646000)
# RGB -> shape (3, 1920, 1080)
#
# # print(audio_native)
# r, g, b = some_img
# r = some_img[0, :, :]
left, right = audio_native
# left = audio_native[0]
# right = audio_native[1]

# print(left.shape, left.size, left)
# print(right.shape, right.size, right)

# frames = zip(left, right)
# print(next(frames))
# print(next(frames))

# frame_0 = audio_native[:, 0]
# left_0 = audio_native[0, 0]
# left_all = audio_native[0, :]
# right_0 = audio_native[1, 0]
# print(frame_0, left_0, right_0)
# print(left_all)

# pict[2, :, :]

# frame_1 = audio_native[:, 0]
# print(frame_1)
# print(audio_native[0, 0])  # [0][0]

# print(right)
print(np.square(right))
left_avg = np.square(left).sum() / left.size
print(left_avg)
print(np.sqrt(left_avg))

# # left_avg = sum(el ** 2 for el in left) / len(left)
