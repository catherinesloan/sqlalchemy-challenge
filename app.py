#  Importing libraries - from jupyter notebook
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper - from jupyter notebook
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

# Import Flask
from flask import Flask, jsonify

# Set up database - from jupyter notebook
# Had to add connect_args so I could do multiple queries in browser
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Setting up routes:

# /
@app.route("/")
def homepage():
    return(
        f"<h1>Surfs up! Climate API for Hawaii</h1> <br/>"
        f"List of all available routes: <br/>"
        f"Click here for <a href='/api/v1.0/precipitation'>precipitation data for the last year</a> <br/>"
        f"Click here for <a href='/api/v1.0/stations'>a list of the weather stations</a> <br/>"
        f"Click here for <a href='/api/v1.0/tobs'>temperature data for the last year at station USC00519281, WAIHEE 837.5, HI US</a> <br/>"
        f"Click here for <a href='/api/v1.0/<start>'>min, av and max temps for all dates greater than and equal to start date - enter in format 'yyyy-mm-dd'</a> </br>"
        f"Click here for <a href='/api/v1.0/<start>/<end>'>min, av and max temps for dates in the range - enter in format 'yyyy-mm-dd'</a>"
    ) 

# api/v1.0/precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    """
    Perform a query to retrieve the date and precipitation scores for last 12 months
    Return the JSON representation of your dictionary
    """
    # Calculate the date 1 year ago from the last data point in the database
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Perform a query to retrieve the date and precipitation scores for last 12 months
    prcp_dates = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).all()

    # Short cut way of writing a for loop - go through each row of prcp_dates, save as a dictionary where date is the key
    results = {date: prcp for date, prcp in prcp_dates}
    
    return jsonify(results)

# /api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations():
    # Return a JSON list of stations from the dataset
    station_result = session.query(Station.name).all()
    # []
    station_list = list(np.ravel(station_result))
    return jsonify(station_list)

# /api/v1.0/tobs
@app.route("/api/v1.0/tobs")
def tobs():
    # Query the dates and temperature observations of the most active station for the last year of data
    # the most active station = USC00519281

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Return a JSON list of temperature observations (TOBS) for the previous year
    yearly_tobs = session.query(Measurement.tobs).filter(Measurement.date >= query_date).filter(Measurement.station == 'USC00519281').all()

    tobs_list = list(np.ravel(yearly_tobs))
    return jsonify(tobs_list)

# /api/v1.0/<start> 
@app.route("/api/v1.0/<start>")
def start_date(start):
    # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

    start_temps = session.query(func.min(Measurement.tobs), func.round(func.avg(Measurement.tobs),2), func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).all()

    start_list = list(np.ravel(start_temps))
    return jsonify(start_list)

# /api/v1.0/<start>/<end>
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start,end):

# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

    start_end_temps = session.query(func.min(Measurement.tobs), func.round(func.avg(Measurement.tobs),2), func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    start_end_list = list(np.ravel(start_end_temps))
    return jsonify(start_end_list)

## glue code
if __name__ == "__main__":
    app.run(debug=True)
