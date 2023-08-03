import pandas as pd
from matplotlib import pyplot as plt

pd.options.mode.chained_assignment = None
# PLOT FOR COVID Vaccinations and Hospitalisation and ICU

# FOR NUMBER OF HOSPITALISATION AND ICU ADMISSIONS (data.gov)
sick_historical = pd.read_csv("COVID Analysis 2023\Datasets\\NumberofNEW_COVID19hospitalisationsICUadmissionsbyEpiweek.csv")
sick_data = sick_historical[['epi_date_end', 'total_count']]
sick_data['epi_date_end'] = pd.to_datetime(sick_data['epi_date_end']) # Convert column to datetime

sick_data_gov = plt.plot(sick_data['epi_date_end'], sick_data['total_count'], label='Line Graph 1', color='Red')

# LABEL BEFORE INTRODUCING NEXT DATASET
plt.legend(["Hospitalisation and ICU"])
plt.xlabel('Date (Year - Month)', fontsize=12)
plt.ylabel('Number of New COVID-19 Hospitalisation and ICU Admissions (by Epiweek*)', fontsize=12) # CHANGE ACCORDINGLY TO DATA
plt.tick_params(labelsize = 14)
# Add a footnote below and to the right side of the chart
plt.annotate('*Epiweek refers to a week and is commonly used by ministries of health',
            xy = (1.0, -0.1),
            xycoords='axes fraction',
            ha='right',
            va="center",
            fontsize=10)

plt.tight_layout()

plt.title("COVID Vaccinations / Hospitalisation and ICU")

# FOR VACCINATION RATES
vacc_alt = plt.twinx()
Vacc_Historical = pd.read_csv("COVID Analysis 2023\Datasets\ProgressofCOVID19vaccination.csv") # Get file
vacc_data = Vacc_Historical[['vacc_date','minimum_protection_pcttakeup']] # Identify columns to print
vacc_data['vacc_date'] = pd.to_datetime(vacc_data['vacc_date']) # Convert column to datetime

vacc_alt.plot(vacc_data['vacc_date'], vacc_data['minimum_protection_pcttakeup'], label='Line Graph 2', color='Blue')

# PRINT OUTPUT
vacc_alt.legend(["Vaccination Rate (%)"], loc='upper right')
vacc_alt.set_ylabel('Vaccination Rate (%)', fontsize=12) # CHANGE ACCORDINGLY TO DATA
vacc_alt.set_ylim(None, 100)

plt.show()
