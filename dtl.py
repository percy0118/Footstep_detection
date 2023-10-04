# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:01:47 2023

@author: param
"""

import librosa
import numpy as np
import matplotlib.pyplot as plt


def extr(audio_file,genre):

    #print(audio_file)
    # Load the audio file.
    audio, sr = librosa.load(audio_file)
    """
    #chroma
    chroma=librosa.feature.chroma_stft( y=audio, sr=sr, n_fft=2048, hop_length=512,  n_chroma=12)
    chroma_mean=np.mean(chroma)
    chroma_var=np.var(chroma)

    """



    mfcc_13 = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)


    # Compute the energy of the audio file.
    energy = librosa.feature.rms(y=audio)



    #plt.subplot(2,2)
    sp_bw=librosa.feature.spectral_bandwidth(y=audio,sr=sr,hop_length=512)



    spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)

    #librosa.display.waveshow(y, kwargs)
    # Return a dictionary of features.


    #np.save("C:\Users\param\OneDrive\Documents\DTL\footstep audio\1-155858-A-25_features", features, allow_pickle=True, fix_imports=True)
    #mean_energy=np.correlate(energy)
    mfcc_mean=np.mean(mfcc_13)
    mfcc_var=np.var(mfcc_13)
    energy_mean=np.mean(energy)
    energy_var=np.var(energy)
    sp_mean=np.mean(sp_bw)
    sp_c_mean=np.mean(spectral_centroid)
    #print(mean_mfcc,mean_energy,mean_sp)

    mean=[mfcc_mean,mfcc_var,energy_mean,energy_var,sp_mean,sp_c_mean,genre]
    global mean_values
    mean_values.append(mean)
    #print(mean)
    


mean_values=[]
#mean_values=['mfcc_mean','mfcc_var','energy_mean','energy_var','spectral_bandwidth_mean','spectral_centroid mean']
features={}
# import required module
import os
# assign directory
directory = '/content/drive/MyDrive/1DTL'

# iterate over files in
# that directory
i=0
#extr(audio_file)
for root, dirs, files in os.walk(directory):
    for name in files:
        filename = os.path.join(root, name)
        genre=root.split('/')[-1]
        #print(filename)
        if genre=='footsteps':
         extr(filename,1)
        else :
          extr(filename,0)




#print(mfcc)
#print(mean_values)

import pandas as pd


DF = pd.DataFrame(mean_values,columns=['mfcc_mean','mfcc_var','energy_mean','energy_var','spectral_bandwidth_mean','spectral_centroid mean','type'])

# save the dataframe as a csv file
DF.to_csv("/content/drive/MyDrive/1DTL/footsteps_data.csv")




