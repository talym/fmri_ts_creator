from scipy.io import loadmat
import pandas as pd
import os
import math

T_R = 2.5
mat_file = r'E:\ketamine\pain\Results_Schaefer2018\PAIN_KET\clusterAssignments\k6.mat'
events_folder = r'E:\ketamine\pain\events'
fo_file = r'E:\ketamine\pain\Results_Schaefer2018\PAIN_KET\analyses\fo_results.xlsx'
fo_enreached = r'E:\ketamine\pain\Results_Schaefer2018\PAIN_KET\analyses\fo_results_enreached.xlsx'
list_of_events = ['negative', 'neutral', 'vas8', 'vas2', 'fix', 'feedback', 'washout']
k = 6

def add_fo_for_events(fo, index_fo, partition, events, k, ses):

    for event in list_of_events:
        total_tr = 0
        flt_events = events[events['trial_type'].str.contains(event, case=False, na=False)]
        for index_ev, row in flt_events.iterrows():
            start = int(math.ceil(row['onset'] / T_R))+1
            end = int((row['onset'] + row['duration'])//T_R)
            for tr in range(start, end + 1):
                fo.loc[index_fo, str(ses) + '_' + event + '_' + str(partition[tr-1][0])] +=1
                total_tr+=1
        for part in range(k):
            fo.loc[index_fo, str(ses) + '_' + event + '_' + str(part + 1)] = \
                float(fo.loc[index_fo, str(ses) + '_' + event + '_' + str(part + 1)])/total_tr
    """for event in list_of_events:
        for part in range(k):
            fo.loc[index_fo, str(ses) + '_' + event + '_' + str(part+1)] /= total_tr"""
    return fo


if __name__ == '__main__':
    partition = loadmat(mat_file)['clusterAssignments']['k6'][0][0]['partition'][0][0]
    scan_len = loadmat(mat_file)['clusterAssignments']['k6'][0][0]['SCAN_LEN'][0][0]
    fo = pd.read_excel(fo_file).iloc[:28]
    ses_1_start = 0
    ses_2_start = int(sum(scan_len[:scan_len.shape[0]//2]))
    for ses in range(1, 3):
        for event in list_of_events:
            for part in range(k):
                fo[str(ses) + '_' + event + '_' + str(part+1)] = 0
    for index_fo, row in fo.iterrows():
        scan = row['TP1']
        try:
            id = scan[:scan.find('_ses-')]
        except:
            print(f'Missing id: {id}')
            continue
        try:
            scan_1_events = \
                pd.read_table(os.path.join(events_folder, id+'_ses-1_task-fmrimentalandphysicalpainphysiosmstr_events.tsv'))
        except:
            print(f'Missing events file {id} ses-1')
        else:
            fo = add_fo_for_events(fo, index_fo, partition[ses_1_start: ses_1_start+scan_len[index_fo][0]], scan_1_events, k, 1)
        finally:
            ses_1_start += scan_len[index_fo][0]
        try:
            scan_2_events = \
                pd.read_table(os.path.join(events_folder, id+'_ses-2_task-fmrimentalandphysicalpainphysiosmstr_events.tsv'))
        except:
            print(f'Missing events file {id} ses-2')
        else:
            fo = add_fo_for_events(fo, index_fo,
                                   partition[ses_2_start: ses_2_start+scan_len[scan_len.shape[0] // 2 + index_fo][0]],
                                   scan_2_events, k, 2)
            #print(ses_2_start, ses_2_start+scan_len[scan_len.shape[0] // 2 + index_fo][0])
        finally:
            ses_2_start += scan_len[scan_len.shape[0] // 2 + index_fo][0]
    fo.to_excel(fo_enreached)



