# sqlalchemy-challenge

## Surf's Up! Climate Analysis

### Background:
To help plan my ***4*** day trip to Honolulu, Hawaii, I will do some climate analysis on the area. 

## Part 1 - Climate Analysis and Exploration

### Task:
To use Python and SQLAlchemy to do climate analysis and data exploration of the [climate database](https://github.com/catherinesloan/sqlalchemy-challenge/tree/main/Resources), using SQLAlchemy ORM queries, Pandas, and Matplotlib.

Using _SQLAlchemy create_engine_ to connect to the sqlite database and using _SQLAlchemy automap_base()_ to reflect the tables into classes and save a reference to those classes called _Station_ and _Measurement_. 


### Output:
[Jupyter Notebook](https://github.com/catherinesloan/sqlalchemy-challenge/blob/main/climate_analysis.ipynb)

1. **Precipitation Analysis**
   - Designed a query to retrieve the last 12 months of precipitation data and selected only the date and prcp values
   - Loaded the query results into a Pandas DataFrame and set the index to the date column
   - Sort the DataFrame values by date
   - Plotted the results using the DataFrame plot method
   - Printed the summary statistics for the precipitation data 

<img width="878" alt="Screen Shot 2021-05-29 at 6 05 32 pm" src="https://user-images.githubusercontent.com/73929301/120063026-80a0e980-c0a8-11eb-8e16-a2fe2b9fd3c0.png">


2. **Station Analysis** 
   - Designed a query to calculate the total number of stations
   - Designed a query to find the most active stations
   - Listed the stations and observation counts in descending order
   - Designed a query to calculate that 'the most active station is WAIHEE 837.5, HI US' 
   - Designed a query to retrieve the last 12 months of temperature observation data (TOBS)
   - Filter by the station with the highest number of observations, WAIHEE 837.5, HI US
   - Plotted the results as a histogram with bins=12

<img width="888" alt="Screen Shot 2021-05-29 at 6 08 39 pm" src="https://user-images.githubusercontent.com/73929301/120063115-ef7e4280-c0a8-11eb-96be-5c915b3a051e.png">

## Part 2 - Climate App

### Task:
Design a Flask API based on the queries developed in part I.

### Output:
Created **6 different routes** in a [Flask App](https://github.com/catherinesloan/sqlalchemy-challenge/blob/main/app.py)
1. **Home page**
2. **/api/v1.0/precipitation**
Converted the query results to a dictionary using date as the key and prcp as the value.
Returning the JSON representation of the dictionary.
3. **/api/v1.0/stations**
Returned a JSON list of stations from the dataset
4. **/api/v1.0/tobs**
Querying the dates and temperature observations of the most active station, WAIHEE 837.5, HI US
Returning a JSON list of temperature observations (TOBS) for the previous year
5. **/api/v1.0/**<**start>**
When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date
Returning a JSON list of the minimum temperature, the average temperature, and the max temperature for the given start date
6. **/api/v1.0/<**start>/<**end>**
When given the start **and** the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
Returning a JSON list of the minimum temperature, the average temperature, and the max temperature for the given start-end range

<img width="542" alt="Screen Shot 2021-05-29 at 6 19 09 pm" src="https://user-images.githubusercontent.com/73929301/120063681-b98e8d80-c0ab-11eb-9739-afa5fefe10c6.png">

### To use:
1. Clone this repository
2. Open new terminal within root of the directory
3. Enable python envirnonment _'conda activate PythonData'_
4. Run _'python app.py'_
5. Open local host in web browser
6. Investigate routes by following links
7. For routes 5 and 6, remember to enter dates into the url bar in the correct format 

### Considerations: 
- [] Complete bonus part of the task

### Bonus: 

1. **Temperature Analysis I**
   - Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
   - Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
   - Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

2. **Temperature Analysis II**
   - The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.
   - Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").
   - Plot the min, avg, and max temperature from your previous query as a bar chart.
   - Use the average temperature as the bar height.
   - Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

3. **Daily Rainfall Average** 
   - Calculate the rainfall per weather station using the previous year's matching dates.
   - Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.
   - You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic TOBS that match that date string.
   - Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list. 
   - Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
   - Use Pandas to plot an area plot (stacked=False) for the daily normals.










