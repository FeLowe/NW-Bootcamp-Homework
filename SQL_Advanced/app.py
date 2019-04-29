import numpy as np

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Home Route
#################################################

@app.route("/")

def home ():
	return (
		f"<h3>Welcome to the Surf Up API</h3>"
		f"<b><i>Available Routes:</i></b>"
        f"<p>/api/v1.0/precipitation</p>"
		f"<p>/api/v1.0/stations</p>"
		f"<p>/api/v1.0/tobs</p>"
        f"<p>/api/v1.0/start date ->format = yyyy-mm-dd </p>"
        f"<p>/api/v1.0/start date/end date ->format = yyyy-mm-dd </p>"
	)

#################################################
# Precipitation Route
#################################################

@app.route("/api/v1.0/precipitation")

def precipitation():
    '''Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.'''
    
    #Query date and prcp
    prcp_results = session.query(Measurement.date, Measurement.prcp).all()

    prcp_dates = []
    for date, prcp, in prcp_results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["precipitation"] = prcp
        prcp_dates.append(prcp_dict)

    return jsonify(prcp_dates)

#################################################
# Stations Route
#################################################

@app.route("/api/v1.0/stations")

def stations():
    '''Return a JSON list of stations from the dataset.'''

    # Query stations
    station_results = session.query(Measurement.station).\
        group_by(Measurement.station).all()
    
    all_stations = []
    for station in station_results:
        stations_dict = {}
        stations_dict["station"] = station
        all_stations.append(stations_dict)

    return jsonify(all_stations)

#################################################
# Tobs Route
#################################################

@app.route("/api/v1.0/tobs")

def tobs():
    ''' Query for the dates and temperature observations from a year from the last data point.
        Return a JSON list of Temperature Observations (tobs) for the previous year.'''
    
    # #last 12 months 
    last_12_months = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    tobs_12_months = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date > last_12_months).order_by(Measurement.date).all()

    year_tobs = []

    for tobs in tobs_12_months:
        tobs_dict = {}
        tobs_dict["tobs"] = tobs
        year_tobs.append(tobs_dict)

    return jsonify(year_tobs)

#################################################
# Start Date Route
#################################################

@app.route("/api/v1.0/<start_date>")

def tobs_start_date(start_date):

    start_dates = []

    start_date_results = session.query(Measurement.date, 
    func.avg(Measurement.tobs), func.max(Measurement.tobs), func.min(Measurement.tobs)).\
    filter(Measurement.date == start_date).all()
    
    for result in start_date_results:
        row = {}
        row['date'] = result[0]
        row['avg temperature'] = int(result[1])
        row['max temperature'] = result[2]
        row['mix temperature'] = result[3]
        start_dates.append(row)

    return jsonify(start_dates)

#################################################
# Start and End Date Route
#################################################

@app.route("/api/v1.0/<start_date>/<end_date>/")

def tobs_start_end_date(start_date, end_date):
	
    start_end_date_results = session.query(Measurement.date, 
    func.avg(Measurement.tobs), func.max(Measurement.tobs), func.min(Measurement.tobs)).\
    filter(Measurement.date >= start_date, Measurement.date <= end_date).all() 

    start_end_dates = []
    for result in start_end_date_results:
        row = {}
        row["start date"] = start_date
        row["end date"] = end_date
        row["avg temperature"] = int(result[1])
        row["max temperature"] = result[2]
        row["min temperature"] = result[3]
        start_end_dates.append(row)

    return jsonify(start_end_dates)

if __name__ == '__main__':
    app.run(debug=True)