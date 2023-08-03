# COVID-Analysis-2023
Motivation:
I wanted to analyze the relationship between vaccination rates with the number of infections, as well as the number of hospitalisation and ICU admission in Singapore. 
This led me to gather data from online sources such as data.gov.sg and the World Health Organization, where I filtered out and analyzed the data accordingly into Epiweeks, to better potray my results. I produced the graphs with the help of Python libraries, such as Pandas and Matplotlib. 
After analyzing the data, I infered that there is some correlation between vaccination rates and the number of infections. The data gathered for number of hospitalisation and ICU admission were limited to 2023, thus I cannot comment with confidence for the set of results shown. The results and code are attached in the repo.

Disclaimer:
Data does not belong to me and is captured near the end of July 2023. It is provided by courtesy from data.gov.sg as well as the World Health Organization (WHO). 
Data was analyzed to be as accurate as possible, I am not responsible for any losses of any kind if my data were to be used.

Prequisites:
1. Change relative path for each CSV file, if needed

Notes:
1. Added column "epi_date_start" and "epi_date_end" in file "NumberofCOVID19infections_by_Epiweek.csv"

2. Vaccination Rate defined as those considered under "Minimum Protection", which consists of 3 doses.

3. COVID Data from WHO (https://covid19.who.int/data). Kept only "Singapore" in csv, with data from 1 Jan 2021 to 12 Feb 2023. From 12 Feb 2023 onwards, data.gov supplements it (same as WHO).

4. Original data from WHO measures daily cases. I cleaned up the data and created additional columns to measure by "Epi-weeks", along with their dates.

5. Combined Hospitalisation and ICU into 1 type and added column "total_count" to sum up both types in "NumberofNEW_COVID19hospitalisationsICUadmissionsbyEpiweek.csv". CSV only contains data from 2023 onwards.

Last Updated: 03 August 2023
