import numpy as np
import albumentations  as A

use_rorate=True
add_ground=True
warp_phase_filename = './np_data/test3000/gaussian_max/test_noisy_warp_phase_3000.npy'
ground_A_filename = './np_data/test3000/test_background_A_320.npy'
ground_V_filename = './np_data/test3000/test_background_V_320.npy'
shift_phase_filename = './np_data/test3000/gaussian_max/test_trans_phase_add_ground_rorate.npy'
# shift_pixel_low=-20
# shift_pixel_max=20
# angle_limit=(-10,10)
# rorate_pro=0.8
shift_pixel_low=0
shift_pixel_max=1
angle_limit=(0,0)
rorate_pro=1
final_phase_shape=256
warp_phases = np.load(warp_phase_filename,allow_pickle=True)
A_phases = np.load(ground_A_filename,allow_pickle=True)
V_phases = np.load(ground_V_filename,allow_pickle=True)
shift_phase_list =[]
for i in range(warp_phases.shape[0]):
    single_warp_phase = warp_phases[i]
    single_a_phase = A_phases[i]
    single_v_phase = V_phases[i]
    angle = [0,-np.pi/2,np.pi/2,np.pi]
    shift_phase = np.zeros((4,final_phase_shape,final_phase_shape),dtype=np.float32)
    trans = A.Rotate(limit=angle_limit,p=rorate_pro)
    for j in range(4):
        if add_ground:
            temp_phase= single_a_phase*(1+single_v_phase*np.cos(single_warp_phase+angle[j]))
        else:
            temp_phase = np.cos(single_warp_phase+angle[j])
        if use_rorate:
            if j!=0:
                temp_phase = trans(image=temp_phase)
                temp_phase = temp_phase['image']
                shift_pixel = np.random.randint(low=shift_pixel_low,high=shift_pixel_max)
                direction = np.random.randint(low=0,high=2)
                temp_phase = np.roll(temp_phase,shift_pixel,direction)
        shift_phase[j] = A.center_crop(img=temp_phase,crop_height=final_phase_shape,crop_width=final_phase_shape)
    shift_phase_list.append(shift_phase)
total_shift_phases = np.array(shift_phase_list)
print(total_shift_phases.dtype)
print(total_shift_phases.shape)
np.save(shift_phase_filename,total_shift_phases,allow_pickle=True)