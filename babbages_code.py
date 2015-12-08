def statistics(arr):

    import numpy as np



    mean = np.mean(arr)

    std = np.std(arr)

    high_score = max(arr)

    low_score = min(arr)



    return mean,std,high_score,low_score
