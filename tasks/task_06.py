# numpy arrays to adjust pixels example

'''
# step 1
size(2, 2)
array = np.zeros((height, width, 3))
print(array)
'''

'''
# step 2
size(200, 200)
array = np.zeros((height, width, 3))
array[10:20, 30:60, 1] = 255
set_np_pixels(array, bands='RGB')
print(array)
'''

# step 3
size(200, 200)
array = np.zeros((height, width, 3))
array[10:20, 30:60, 1] = 255
array[:60, :, 0] = 255
array[:, -60:, 2] = 125
set_np_pixels(array, bands='RGB')
print(array)

