def encode(label):
    import numpy as np
    '''One hot labeling
    args:
        label: [list] 1D label array. -1: sell, 1: buy, 0: no action
    
    return:
        [list] one hot label. 0: sell, 1: buy, 2: no action( -1 -> [1, 0, 0], 1 -> [0, 1, 0], 0 -> [0, 0, 1])
    '''
    out = np.zeros((len(label), 3))

    for pos, i in enumerate(label):
        if i == 1:
            out[pos, 1] = 1
        elif i == -1:
            out[pos, 0] = 1
        else:
            out[pos, 2] = 1
    return out