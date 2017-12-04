import math
INPUTS = [1, 12, 23, 1024]

for value in INPUTS:
    # a) find the "girone"
    girone = math.ceil(math.sqrt(value))
    if girone % 2 == 0: girone += 1
    upper_boud = girone**2
    lower_bound = (girone - 2)**2
    max_coord = (girone - 1) // 2
    normalized_value = value - lower_bound
    side = math.ceil(normalized_value / (girone - 1))
    if side == 1:
        x = max_coord
        y = 
     print(value, girone, normalized_value)
