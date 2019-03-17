from flask import Flask, render_template
from evrweb import app
from evrweb.models import Driver_Lap_Summary, session
from sqlalchemy import func

print('hello2')

@app.route('/')
def home():
    print('hello')
    return render_template('home.html', title='Dashboard')
    
    qry = session.query(
    Driver_Lap_Summary.lap_number,
    Driver_Lap_Summary.driver_number,
        func.min(
        Driver_Lap_Summary.elapsed_time
        ).label(
        'fastest_time')
    ).group_by(
        Driver_Lap_Summary.lap_number,
    ).order_by(
        Driver_Lap_Summary.lap_number,
        Driver_Lap_Summary.driver_number
    )

    for a,b,c in qry:
        print(a,b,c)
