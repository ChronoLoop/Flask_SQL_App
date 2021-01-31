# flask and sqlite tutorial https://medium.com/@aliciagilbert.itsimplified/a-slick-crud-application-built-using-python-with-flask-and-sqlite3-to-teach-simple-mysql-queries-bd75e1109582
from flask import Flask, request, redirect, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template('home.html')
@app.route('/sightings')
def sql_sighting_database():
    from sqlquery import sql_query
    tuples = sql_query("SELECT * FROM SIGHTINGS")
    return render_template('sightings.html', tuples=tuples)

@app.route('/flowers')
def sql_flowers_database():
    from sqlquery import sql_query
    tuples = sql_query("SELECT * FROM FLOWERS")
    return render_template('flowers.html', tuples=tuples)


@app.route('/features')
def sql_features_database():
    from sqlquery import sql_query
    tuples = sql_query("SELECT * FROM FEATURES")
    return render_template('features.html', tuples=tuples)

@app.route('/members')
def sql_members_database():
    from sqlquery import sql_query
    tuples = sql_query("SELECT * FROM MEMBERS")
    return render_template('members.html', tuples=tuples)

@app.route('/sql_update_flowers', methods=['POST', 'GET'])
def sql_updatelink():
    from sqlquery import get_flower_tuple
    if request.method == 'GET':
        oldGenus = request.args.get('oldGenus')
        oldSpecies = request.args.get('oldSpecies')
        oldComname = request.args.get('oldComname')
        oldTuple = get_flower_tuple(oldGenus, oldSpecies, oldComname)
    return render_template('flowers.html', oldTuple=oldTuple)

@app.route('/update_flower', methods=['POST', 'GET'])
def sql_update_flower():
    from sqlquery import update_flower, sql_query
    if request.method == 'POST':
        oldComname = request.form['oldComname']
        newComname = request.form['newComname']
        newGenus = request.form['newGenus']
        newSpecies = request.form['newSpecies']
        update_flower(oldComname, newComname, newGenus, newSpecies)
    tuples = sql_query("SELECT * FROM FLOWERS")
    return render_template('flowers.html', tuples=tuples)

@app.route('/insert_sighting', methods=['POST', 'GET'])
def sql_insert_sighting():
    from sqlquery import sql_query, insert_sighting
    if request.method == 'POST':
        name = request.form['name']
        person = request.form['person']
        location = request.form['location']
        sighted = request.form['sighted']
        insert_sighting(name, person, location, sighted)
    tuples = sql_query("SELECT * FROM SIGHTINGS")
    return render_template('sightings.html', tuples=tuples)

@app.route('/ten_recent_flowers')
def sql_get_ten_recent():
    from sqlquery import get_recent_sightings_by_flower_name
    eComname = request.args.get('eComname')
    tuples = get_recent_sightings_by_flower_name(eComname)
    return render_template('flowers.html', tuples=tuples)

if __name__ == "__main__":
    app.run(debug=True)