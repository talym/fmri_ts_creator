import os
import glob
import numpy as np
import pandas as pd
import nibabel as nib
import matplotlib.pyplot as plt
from nilearn.plotting import plot_event
from nilearn.glm.first_level import FirstLevelModel
from nilearn.plotting import plot_design_matrix
from nilearn.glm.second_level import SecondLevelModel

from preprocessing_tools import PrepTools


class GLMAnalyzer(object):
    def __init__(self, glm_res_path, prep_params = None):
        if prep_params is not None:
            self.T_R = prep_params.T_R
            self.DEBUG = prep_params.DEBUG
            self.prep_params = prep_params
        self.glm_res_path = glm_res_path
        self.glm2_name = None
    def glm1(self, set_of_files):
        try:
            events = pd.read_table(set_of_files['EVENTS'])
        except:
            print('No event file: ', set_of_files['EVENTS'])
            return
        if 'shift' in self.glm_res_path:
            for i in range(events.shape[0]):
                events.loc[i, 'onset'] = events.loc[i, 'onset'] + 2.5
        conf_, _ = PrepTools.handleConf(set_of_files, self.prep_params)
        first_level_model = FirstLevelModel(
            self.T_R,
            noise_model="ar1",
            standardize=False,
            hrf_model="spm",
            drift_model="cosine",
            high_pass=0.01,
            smoothing_fwhm=6)
        first_level_model = first_level_model.fit(set_of_files['NIFTI'], events=events, confounds = conf_)
        design_matrix = first_level_model.design_matrices_[0]

        contrast = np.zeros(len(design_matrix.columns))
        contrast[design_matrix.columns.to_list().index('vas2_')] = 1
        contrast[design_matrix.columns.to_list().index('vas8_')] = -1
        z_map = first_level_model.compute_contrast(contrast, output_type="z_score")
        if  self.DEBUG:
            plot_event(events, figsize=(15, 5))
            plt.show()

            # design_matrix.drop('music', axis=1, inplace=True) # remove dummy event
            plot_design_matrix(design_matrix)
            plt.show()
        nifti_name = set_of_files['NIFTI'].split('\\')[-1]
        start_index = nifti_name.find('_task')
        nib.save(z_map, os.path.join(self.glm_res_path, nifti_name[:start_index] + '_result.nii.gz'))

    def glm2(self, run):
        self.glm2_name = 'glm2_' + run + '_result.nii.gz'
        glm1_fies = glob.glob(self.glm_res_path + "\*" + run +"*_result.nii.gz")
        n_subjects = len(glm1_fies)
        design_matrix = pd.DataFrame([1] * n_subjects, columns=["intercept"])
        second_level_model = SecondLevelModel(n_jobs=2).fit(glm1_fies, design_matrix=design_matrix)
        z_map = second_level_model.compute_contrast(output_type="z_score")
        nib.save(z_map, os.path.join(self.glm_res_path, self.glm2_name))
    def glm2ROIAv(self, roi):
        roi_img = nib.load(roi)
        roi_data = roi_img.get_fdata()
        glm2_img = nib.load(os.path.join(self.glm_res_path, self.glm2_name))
        glm2_data = glm2_img.get_fdata()

        print(roi.split('.')[0], glm2_data[roi_data==1].mean())





