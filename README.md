## About the project
### Taxi Demand Modelling

This project investigates geospatial and temporal modelling of hourly NYC Yellow Taxi demand using 2024 data. Exploring how taxi demand interacts with subway ridership and weather conditions (particularly rainfall), focusing on spatial patterns in Manhattan.

Two predictive models were built:

- Poisson Regression (GLM) – interpretable but limited by overdispersion.

- Gradient Boosted Trees (GBT) – higher accuracy, capturing non-linear relationships.

### Findings
Findings show that subway usage anomalies and rainy periods amplify taxi demand in certain areas. 
Recommendations are provided for the NYC Taxi & Limousine Commission (TLC) to optimise fleet allocation, reduce wait times, and improve driver efficiency.
A summary of the methodology and findings can be found in report.pdf.



## Environment Setup

Prereqs: Install Conda or Miniconda. 

Clone and enter repository folder:
```bash
cd project-1-individual-jnakos01
```

Create environment :
```bash
conda env create -f environment.full.yml
```

Activate:
```bash
conda activate project1env
```

Register environment so it can be used on Jupyter:
```bash
python -m ipykernel install --user --name project1env --display-name "project1env"
```

Launch Jupyter:
```bash
jupyter notebook
```

Select the "project1env" kernel in the Notebook UI.

To update after you change environment.yml:
```bash
conda env update -f environment.full.yml --prune
```

To remove:
```bash
conda remove -n project1env --all
```


## Usage Instructions:
Step 1: Download prereq data (Subway + Lookups) from: 
https://drive.google.com/file/d/1uyMaVqJIwgWSFHeiuK-LRoZTY7OJELl9/view?usp=sharing
This data is free to redistribute for non-commercial use.

Step 2: Unzip 'data folder downloaded, drag unzipped folder downloaded into the '/project-1-individual-jnakos01' folder. This will fill the existing data folder with the required data for preparation.

If missing, download and insert the /processing_info folder from GitHub into the data folder.

Before running, data should contain 3 non empty subfolders: 'import_csvs', 'ny_boroughs', 'processing_info'.

Step 3: Click 'run all' in each notebook in order: import, taxi_preprocessing, subway_preprocessing, weather_preprocessing, analysis, then modelling. 
