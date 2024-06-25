#import kaggle
#kaggle datasets download -d 'asaniczka/1-3m-linkedin-jobs-and-skills-2024'
"""
This is an app that uses web scraped data available from Kaggle to show the most 
"""

import os
fileAvailable:bool

if os.path.isfile("~/Developer/WhatSkills/asaniczka/1-3m-linkedin-jobs-and-skills-2024"):
    exit
else:
    import subprocess
    command = "kaggle datasets download -d asaniczka/1-3m-linkedin-jobs-and-skills-2024"
    subprocess.run(command, shell=True, capture_output=True, text=True)