import numpy as np
import skimage.util as utils
from torch import mm
import albumentations as A

if __name__=='__main__':
    ### hyper parameter
    warp_phase_filename = '../new_np_data/test/test_warp_phase_256_3000_bound20.npy'
    noisy_warp_phase_filename ='../new_np_data/test/test_noisy_warp_phase_256_3000_bound20.npy'
    # gaussian_noise_var_min=0.01**2      
    gaussian_noise_var_min=0.01**2     
    gaussian_noise_var_max=0.2**2
    mult_noise_var_min = 0.01**2
    mult_noise_var_max = 0.2**2
    salt_noise_density_min=0.01
    salt_noise_density_max=0.2
    isClip=False ### if true,the value will round to [-1,1]
    ### read warp phase
    warp_phases = np.load(warp_phase_filename,mmap_mode='r',allow_pickle=True)
    ### add noise 
    noise_type_vector = np.random.randint(low=1,high=3,size=(warp_phases.shape[0],))
    noisy_phases = np.zeros(shape=warp_phases.shape,dtype=np.float32)
    for i in range(warp_phases.shape[0]):
        single_warp_phase = warp_phases[i]
        norm_warp_phase = single_warp_phase/np.pi
        # noise_type = 1
        noise_type = noise_type_vector[i]
        if noise_type==1:
            ### gaussian noise
            random_var_value = np.random.uniform(low=gaussian_noise_var_min,high=gaussian_noise_var_max)
            noisy_norm_warp_phase = utils.random_noise(norm_warp_phase,mode='gaussian',clip=isClip,var=random_var_value)
        elif noise_type==3:
            ### multive noise
            random_var_value = np.random.uniform(low=mult_noise_var_min,high=mult_noise_var_max)
            noisy_norm_warp_phase = utils.random_noise(norm_warp_phase,mode='speckle',clip=isClip,var=random_var_value)
        elif noise_type==2:
            ### salt pepper noise
            noise_amount = np.random.uniform(low=salt_noise_density_min,high=salt_noise_density_max)
            noisy_norm_warp_phase = utils.random_noise(norm_warp_phase,mode='s&p',clip=isClip,amount = noise_amount)
        else:
            raise ValueError()
        single_noisy_warp_phase = noisy_norm_warp_phase*np.pi
        noisy_phases[i]= single_noisy_warp_phase
    np.save(noisy_warp_phase_filename,noisy_phases,allow_pickle=True)
    print(np.max(noisy_phases))
    
        