import h5py
import numpy as np
import sys
## key_name:true_phase_collection warp_phase_collection
def mat2np(mat_filename,np_filename,key_name='true_phase_collection'):
    my_mat = h5py.File(mat_filename)
    my_mat=my_mat[key_name]
    my_np = np.array(my_mat).T.astype(np.float32)
    print(np.max(my_np))
    print(np.min(my_np))
    np.save(np_filename,my_np,allow_pickle=True)


if __name__=='__main__':

    mat2np(
        mat_filename='../mat_data/test_true_phase_256_3000_bound20.mat',
        np_filename='../new_np_data/test/test_true_phase_256_3000_bound20.npy',
        key_name='true_phase_collection'
    )
    mat2np(
        mat_filename='../mat_data/test_warp_phase_256_3000_bound20.mat',
        np_filename='../new_np_data/test/test_warp_phase_256_3000_bound20.npy',
        key_name='warp_phase_collection'
    )

    # mat2np(
    #     mat_filename='../mat_data/test_true_phase_256_3000.mat',
    #     np_filename='../new_np_data/test/test_true_phase_256_3000.npy',
    #     key_name='true_phase_collection'
    # )
    # mat2np(
    #     mat_filename='../mat_data/test_warp_phase_256_3000.mat',
    #     np_filename='../new_np_data/test/test_warp_phase_256_3000.npy',
    #     key_name='warp_phase_collection'
    # )

    # mat2np(
    #     mat_filename='../mat_data/test_true_phase_256_bound50.mat',
    #     np_filename='../new_np_data/test/test_true_phase_256_bound50.npy',
    #     key_name='true_phase_collection'
    # )
    # mat2np(
    #     mat_filename='../mat_data/test_warp_phase_256_bound50.mat',
    #     np_filename='../new_np_data/test/test_warp_phase_256_bound50.npy',
    #     key_name='warp_phase_collection'
    # )
    # mat2np(
    #     mat_filename='../mat_data/test_true_phase_256_bound80.mat',
    #     np_filename='../new_np_data/test/test_true_phase_256_bound80.npy',
    #     key_name='true_phase_collection'
    # )
    # mat2np(
    #     mat_filename='../mat_data/test_warp_phase_256_bound80.mat',
    #     np_filename='../new_np_data/test/test_warp_phase_256_bound80.npy',
    #     key_name='warp_phase_collection'
    # )
