# Filtering-Scripts
Filter Design and Testing Tools

## Overview  
This repository contains scripts and data files for designing and testing filters for both front and rear wheel speeds. The workflow involves extracting raw CAN data, converting to .csv, analyzing signal in MATLAB, and design filters in Python iteratively.  

## File Structure  

### **Data Files**  
- `*.txt`, `*.csv` – Raw and processed data files.  
- CAN export `.txt` files are processed into `.csv` for MATLAB analysis.  

### **Data Extraction & Processing**  
- `CANDataToCSV.ipynb`, `CleanCANLoggerExportToCSV.ipynb`, `DataExportCleaned.ipynb`  
  - Extracts CAN data from `.txt` files and converts it into `.csv`.  

### **Filtering & Analysis**  
- `FilterDesignerScipy.py`  
  - Implements filtering using SciPy tools for both front and rear wheel speed signals.  
- `FrontTester_Front.mlx`, `FrontTester_Rear.mlx`  
  - MATLAB scripts for analyzing signals, filtering efficiency, spectral analysis, transient response, and Bode plots.  

### **Rear Wheel Speed Data**  
- `RWSinv1_03052025.txt`, `RWSinv2_03052025.txt`, `cleanedDataRWSLeft_03052025.csv`  

### **Front Wheel Speed Data**  
- `FWSInHouse03052025.txt`, `cleanedDataFWSBoth_03052025.csv`  

## Usage  
1. **Extract Data** – Run the Jupyter notebooks to convert CAN `.txt` exports into `.csv`.  
2. **Filter Signals** – Use `FilterDesignerScipy.py` for signal filtering.  
3. **Analyze in MATLAB** – Run `.mlx` scripts for visualization, spectral analysis, and transient response.
