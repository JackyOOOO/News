def label(open_price, m = 5, p = 0.03) :
    import numpy as np
    #Label y
    y = open_price
    m = m
    p = p
    y_list=[]
    for i in range(len(y)-m):
        y_value=np.array([y[i:i+m]])
        y_list.append(y_value)

    label=[]
    for b in range(len(y_list)):
        for j in range(m):
            value=[]
            value.append(np.log(y_list[b].reshape(m,1)[j]) - np.log(y_list[b].reshape(m,1)[0]))

        down_loc=np.where(np.array(value)< -p )[0]
        if (len(down_loc) >= 1):
            down_loc = down_loc.reshape(len(down_loc),1)[0]

        up_loc=np.where(np.array(value) > p)[0]
        if (len(up_loc) >= 1):
            up_loc = up_loc.reshape(len(up_loc),1)[0]

        if (len(down_loc) >= 1) & (len(up_loc) == 0):
            label.append(-1)

        if (len(down_loc) == 0) & (len(up_loc) >= 1):
            label.append(1)

        if (len(down_loc) >= 1) & (len(up_loc) >= 1):
            if down_loc[0]>up_loc[0]:
                label.append(1)
            if down_loc[0]<up_loc[0]:
                label.append(-1)

        if (len(up_loc) ==0) & (len(down_loc) ==0):
            label.append(0)


    Y = label
    return(label)