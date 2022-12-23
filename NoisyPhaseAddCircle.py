import numpy as np
import matplotlib.pyplot as plt
import random
import os

def get_circle_mask(H,W,center,radius):
    Y,X = np.ogrid[:H,:W]
    dist = np.sqrt((X-center[0])**2+(Y-center[1])**2)
    mask = dist<=radius
    return mask

def get_rectangle_mask(H,W,center,height,width):
    mask = np.zeros(shape=(H,W))
    mask[center[0]-height//2:center[0]+height//2,center[1]-width//2:center[1]+width//2]=1
    # mask[]=1
    mask=mask>0
    return mask


if __name__=='__main__':
    # bound=80
    noisy_phase =  np.load(f'../new_np_data/test/test_noisy_warp_phase_256_3000_bound20.npy',allow_pickle=True)
    true_phase = np.load(f'../new_np_data/test/test_true_phase_256_3000_bound20.npy',allow_pickle=True)
    file2save_noisy='../new_np_data/test/test_noisy_warp_phase_256_3000_bound20_remove_geo.npy'
    file2save_true='../new_np_data/test/test_true_phase_256_3000_bound20_remove_geo.npy'
    H,W=noisy_phase.shape[1],noisy_phase.shape[2]
    center_border_low = 96
    center_border_high=160
    radius_low=10
    radius_high=80
    # H = noisy_phase.shape[1]
    # W = noisy_phase.shape[2]
    for index in range(noisy_phase.shape[0]):
        p = np.random.randint(0,100)
        if p<35:
            mask_type = np.random.randint(0,2)
            if mask_type==0:
                center = (np.random.randint(center_border_low,center_border_high),np.random.randint(center_border_low,center_border_high))
                radius = np.random.randint(radius_low,radius_high)
                mask = get_circle_mask(H,W,center=center,radius=radius)
            if mask_type==1:
                center = (np.random.randint(center_border_low,center_border_high),np.random.randint(center_border_low,center_border_high))
                height= np.random.randint(radius_low*2,radius_high*2)
                width = np.random.randint(radius_low*2,radius_high*2)
                mask = get_rectangle_mask(H,W,center,height,width)
            noisy_phase[index][mask]=0
            true_phase[index][mask]=0
    np.save(file2save_noisy,noisy_phase,allow_pickle=True)
    np.save(file2save_true,true_phase,allow_pickle=True)