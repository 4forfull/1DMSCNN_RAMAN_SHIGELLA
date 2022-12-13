# **1DMSCNN_RAMAN_SHIGELLA**
This repository provides the implementation for our paper Multiscale deep learning model for rapid differentiation between SERS spectra of four Shigella species. Our experiments show that SRDS can be used as a practical and efficient tool for Shigella Raman spectroscopy analysis. SRDS provides two functions for input spectral data: peak search, and identify the unknown samples automatically and efficiently. In SRDS, all the above functions can be easily implemented with the assistance of the graphical user interface (GUI).
# **Installation**
The current install version of EasyCID only supports Windows 64-bit version.  
**Download Link:** [**Baidu SkyDrive**](https://pan.baidu.com/s/10gI09jCN2L5xXC-Xzdp-Ug?pwd=l04q)  
**Note:** Once downloaded, unzip it and do not change the default folder name.  
# **Requirements**  
keras 2.4.3  
matplotlib 3.1.1  
numpy 1.18.5  
pandas 0.25.1  
python 3.7  
pyqt5 5.15.4  
scikit-learn 0.21.3  
# **Function**  
[**main**](https://github.com/4forfull/1DMSCNN_RAMAN_SHIGELLA/blob/main/main.py): This is the main interface of the software, all the functions are integrated in it.  
[**model**](https://github.com/4forfull/1DMSCNN_RAMAN_SHIGELLA/blob/main/model.py): Load the pre-trained model, the spectral data of shigella spp were predicted.  
[**curve**](https://github.com/4forfull/1DMSCNN_RAMAN_SHIGELLA/blob/main/curve.py): Visualize the raw spectral data and fit the characteristic peaks.  
# **Usage**  
Run the [main.py](https://github.com/4forfull/1DMSCNN_RAMAN_SHIGELLA/blob/main/main.py) file.  
Click "OPEN" and select the data you want to analyze. The demo data is given in the [demo](https://github.com/4forfull/1DMSCNN_RAMAN_SHIGELLA/tree/main/demo) folder.  
![image](https://github.com/4forfull/1DMSCNN_RAMAN_SHIGELLA/blob/main/Figure/read_file%26curve.png)  
Click "RUN" to execute the model file, and the software will automatically analyze the types of shigella.  
![image](https://github.com/4forfull/1DMSCNN_RAMAN_SHIGELLA/blob/main/Figure/model_predict.png)  
# **Contact**  
name  
**E-mail**: 




