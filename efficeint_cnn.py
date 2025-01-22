import pandas as pd
import os

#Create Files_Name
image_data='/kaggle/input/solar-panel-images/Faulty_solar_panel'
pd.DataFrame(os.listdir(image_data),columns=['Files_Name'])