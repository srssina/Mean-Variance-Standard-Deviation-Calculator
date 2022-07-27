import numpy as np
def calculate():
    try:
        a0,a1,a2,b0,b1,b2,c0,c1,c2=input("please input nine numbers to calculate:").split()
    except ValueError:
        print("List must contain nine numbers.") 

    arr=np.array([[[a0,a1,a2],[b0,b1,b2],[c0,c1,c2]]],float)
    flattened=arr.flatten()
    answer={
    'mean': [np.mean(arr,axis=1), np.mean(arr,axis=2), flattened.mean()],
    'variance': [np.var(arr,axis=1), np.var(arr,axis=2), flattened.var()],
    'standard deviation': [np.std(arr,axis=1),np.std(arr,axis=2), flattened.std()],
    'max': [np.max(arr,axis=1), np.max(arr,axis=2), flattened.max()],
    'min': [np.min(arr,axis=1), np.min(arr,axis=2), flattened.min()],
    'sum': [np.sum(arr,axis=1), np.sum(arr,axis=2), flattened.sum()]
    }
    return answer

print(calculate())    