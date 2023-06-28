# Import the dependencies.
import datetime as dt
import numpy as np
import sqlalchemy
import os
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Set up the database path
database_path = "Resources/hawaii.sqlite"

# Create the engine
engine = create_engine(f"sqlite:///{database_path}")

# Reflect the database tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Homepage - List all available routes
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    one_year_ago = dt.datetime.strptime(last_date[0], "%Y-%m-%d") - dt.timedelta(days=365)
    
    # Query the precipitation data for the last 12 months
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()
    
    # Convert the query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    
    return jsonify(precipitation_data)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Query the list of stations
    results = session.query(Station.station).all()
    
    # Convert the query results to a list
    station_list = list(np.ravel(results))
    
    return jsonify(station_list)

# Temperature Observations route
@app.route("/api/v1.0/tobs")
def tobs():
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    one_year_ago = dt.datetime.strptime(last_date[0], "%Y-%m-%d") - dt.timedelta(days=365)
    
    # Query the most active station ID
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()
    
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station[0]).\
        filter(Measurement.date >= one_year_ago).all()
    
    # Convert the query results to a list
    tobs_list = list(np.ravel(results))
    
    return jsonify(tobs_list)

# Temperature Statistics route
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start, end=None):
    try:
        # Convert start and end dates to datetime objects
        start_date = dt.datetime.strptime(start, "%Y-%m-%d").date()
        end_date = dt.datetime.strptime(end, "%Y-%m-%d").date() if end else None
    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD format."}), 400

    # Query the minimum, average, and maximum temperatures based on the given start and end dates
    if end_date:
        results = session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs)
        ).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    else:
        results = session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs)
        ).filter(Measurement.date >= start_date).all()

    # Convert the query results to a list of dictionaries
    temperature_stats_list = []
    for min_temp, avg_temp, max_temp in results:
        temperature_stats_list.append({
            "Minimum Temperature": min_temp,
            "Average Temperature": avg_temp,
            "Maximum Temperature": max_temp
        })

    return jsonify(temperature_stats_list)

if __name__ == "__main__":
    app.run(debug=True)
