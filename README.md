# sqlalchemy-challenge

## Surf's Up! Climate Analysis

### Background:
To help plan my trip to Honolulu, Hawaii, I will do some climate analysis on the area. 

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

### To use:
1. Clone this repository
2. Open new terminal within root of the directory
3. Enable python envirnonment _'conda activate PythonData'_
4. Run _'python app.py'_
5. Open local host in web browser
6. Investigate routes by following links
7. For routes 5 and 6, remember to enter dates into the url bar in the correct format 

<img width="542" alt="Screen Shot 2021-05-29 at 6 19 09 pm" src="https://user-images.githubusercontent.com/73929301/120063681-b98e8d80-c0ab-11eb-9739-afa5fefe10c6.png">

### Bonus: 

Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

1. **Temperature Analysis I**
   - Identified the average temperature in June and December at all stations across all available years in the dataset
   - Used an unpaired t-test to determine whether the difference in the means, if any, is statistically significant

2. **Temperature Analysis II**
   - Used function called calc_temps to calculate the min, avg, and max temperatures for my trip 
   - Plotted the min, avg, and max temperature from previous query as a bar chart

<img width="294" alt="Screen Shot 2021-06-03 at 4 09 12 pm" src="https://user-images.githubusercontent.com/73929301/120596064-a05c5700-c486-11eb-98a3-0b8df69e2a4c.png">


3. **Daily Rainfall Average** 
   - Calculated the rainfall per weather station using the previous year's matching dates
   - Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.
   - Used the function called daily_normals that calculates the daily normals for a specific date. 
   - Created a list of dates for my trip in the format %m-%d
   - Used the daily_normals function to calculate the normals for each date string and appended the results to a list
   - Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date
   - Used Pandas to plot an area plot for the daily normals

<img width="432" alt="Screen Shot 2021-06-03 at 4 09 22 pm" src="https://user-images.githubusercontent.com/73929301/120596083-a6523800-c486-11eb-89ba-67323d2a21ce.png">
