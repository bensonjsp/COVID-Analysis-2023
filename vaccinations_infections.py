import pandas as pd
from matplotlib import pyplot as plt

pd.options.mode.chained_assignment = None
# PLOT FOR COVID Vaccinations and Infection Count

# FOR NUMBER OF COVID INFECTIONS (data.gov)
infection_historical = pd.read_csv("COVID Analysis 2023\Datasets\\NumberofCOVID19infections_by_Epiweek.csv")
infection_data = infection_historical[['epi_date_end', 'est_count']]
infection_data['epi_date_end'] = pd.to_datetime(infection_data['epi_date_end']) # Convert column to datetime

infection_data_gov = plt.plot(infection_data['epi_date_end'], infection_data['est_count'], label='Line Graph 1', color='Green')

# FOR NUMBER OF COVID INFECTIONS (WHO)
infection_historical_who = pd.read_csv("COVID Analysis 2023\Datasets\WHO-COVID-19-Singapore-data.csv")
infection_data_who = infection_historical_who[['epi_date_end', 'New_cases_epiweek']]
infection_data_who['epi_date_end'] = pd.to_datetime(infection_data_who['epi_date_end']) # Convert column to datetime

infection_WHO = plt.plot(infection_data_who['epi_date_end'], infection_data_who['New_cases_epiweek'], label='Line Graph 2', color='Red')

# LABEL BEFORE INTRODUCING NEXT DATASET
plt.legend(["Infections (data.gov)", "Infections (WHO)"])
plt.xlabel('Date (Year - Month)', fontsize=12)
plt.ylabel('Number of COVID-19 Infections (by Epiweek*)', fontsize=12) # CHANGE ACCORDINGLY TO DATA
plt.tick_params(labelsize = 14)
# Add a footnote below and to the right side of the chart
plt.annotate('*Epiweek refers to a week and is commonly used by ministries of health',
            xy = (1.0, -0.1),
            xycoords='axes fraction',
            ha='right',
            va="center",
            fontsize=10)

plt.tight_layout()

plt.title("COVID Vaccinations / Infection Count")

# FOR VACCINATION RATES
vacc_alt = plt.twinx()
Vacc_Historical = pd.read_csv("COVID Analysis 2023\Datasets\ProgressofCOVID19vaccination.csv") # Get file
vacc_data = Vacc_Historical[['vacc_date','minimum_protection_pcttakeup']] # Identify columns to print
vacc_data['vacc_date'] = pd.to_datetime(vacc_data['vacc_date']) # Convert column to datetime

vacc_alt.plot(vacc_data['vacc_date'], vacc_data['minimum_protection_pcttakeup'], label='Line Graph 3', color='blue')

# PRINT LABEL
vacc_alt.legend(["Vaccination Rate (%)"], loc='upper left')
vacc_alt.set_ylabel('Vaccination Rate (%)', fontsize=12) # CHANGE ACCORDINGLY TO DATA
vacc_alt.set_ylim(None, 100)

plt.show()
