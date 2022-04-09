import numpy as np

sm_pict = [[[200, 100, 50],
            [100, 200, 0]],
           [[50, 150, 200],
            [0, 50, 100]],
           [[150, 150, 150],
            [255, 255, 255]]]
np_sm_pict = np.array(sm_pict, dtype='uint8')
# print(np_sm_pict)
# print(np_sm_pict.shape)
# red_ch = np_sm_pict[:, :, 0]  # (R), G, B
# green_ch = np_sm_pict[:, :, 1]  # R, (G), B
# print(red_ch)
# print(green_ch)

first_l = np_sm_pict[0]
# lines = np_sm_pict[0:2]
# lines = np_sm_pict[0:2, :, :]
lines = np_sm_pict[0:2, :, 0:2]
# print(first_l)
print(lines)
