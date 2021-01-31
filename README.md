<h1>Flask SQL App</h1>
A web app to query and edit data for a SQLite flower database. The database is maintained by an imaginary wildflower club whose members are interested in observing wildflowers in the Sierra Nevada mountains of California.

<h2>Built with</h2>
<ul>
<li><b>Frontend:</b> HTML/CSS, Bootstrap</li>
<li><b>Backend:</b> Flask, SQLite, Python3</li>
</ul>

<h2>Installation</h2>

For macOS/Linux:
```bash
pip3 install flask
```

For Windows:
```bash
pip install flask
```

In the terminal: 
```bash
python3
>> import flask
>> exit()

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

<h2>Tables</h2>
<ul>
<li>SIGHTINGS (NAME, PERSON, LOCATION, SIGHTED)</li>
<li>FEATURES (LOCATION, CLASS, LATITUDE, LONGITUDE, MAP, ELEV)</li>
<li>FLOWERS (GENUS, SPECIES, COMNAME)</li>
</ul>

<h2>Features</h2>
<ul>
<li>Query - Allow the user to select from a list of flowers. Using the selected flower, the 10 most recent sightings of the selected flower can be displayed. Information include the date, location, and who sighted the flower. </li>
<li>Update - Allow a user to select and update flower information. </li>
<li>Insert - Allow a user to insert a new sighting of a flower. </li>
</ul>