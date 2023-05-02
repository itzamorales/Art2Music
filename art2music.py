#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CSC 1570 Project ot convert Art to Music
# Author: imorales
# Date: 4-20-2023
# Version: 0.1a
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#Import our libraries

import streamlit as st
import pandas as pd
import numpy as np
import cv2
import random
from pedalboard import Pedalboard, Chorus, Reverb, Gain, LadderFilter,Phaser, Delay, PitchShift, Distortion
from pedalboard.io import AudioFile
from PIL import Image
from scipy.io import wavfile
import librosa
import glob

#Keep track of settings
#Handle user user input

#See if they want to use own image or sample
#See if we have an image

#Save Image into a temp file
#Ask the computer to view the image
#grab Hue from HSV
#seperate the Hues and convert to Frequency
#generic song save
#Make an effected version
#save the final song and make a midi