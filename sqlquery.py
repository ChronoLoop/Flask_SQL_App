import sqlite3

conn = sqlite3.connect("flowers2019.db", check_same_thread=False)
conn.text_factory = str

c = conn.cursor()
def sql_query(query):
    with conn:
        c.execute(query)
        tuples = c.fetchall()
        return tuples

def get_recent_sightings_by_flower_name(comname):
    with conn:
        c.execute("SELECT * FROM SIGHTINGS WHERE name = :comname order by sighted desc limit 10", {'comname': comname})
        result = c.fetchall()
        print("The 10 most recent sightings of",comname, ":")
        for element in result:
            print ("\n",element)
        return result

def update_flower(comname, newName, newGenus, newSpecies):
    with conn:
        # get old
        c.execute("SELECT* FROM FLOWERS WHERE comname= :comname", {'comname': comname})
        old = c.fetchone()
        # update
        c.execute("""UPDATE FLOWERS SET comname = :newName, genus = :newGenus, species = :newSpecies 
                     WHERE comname = :comname""", {'comname': comname, 'newName': newName, 'newGenus': newGenus, "newSpecies": newSpecies})
        # # get new
        c.execute("SELECT* FROM FLOWERS WHERE comname= :newName", {'newName': newName})
        new = c.fetchone()
        print("\tOld flower:", old, "has been updated to: \n\tNew flower:", new)

def insert_sighting(name, person, location, sighted):
    with conn:
        c.execute("""INSERT INTO SIGHTINGS VALUES (:name, :person, :location, :sighted)""", 
                    {'name': name, 'person': person, 'location': location, 'sighted': sighted})
        c.execute("SELECT * FROM SIGHTINGS WHERE name = :name AND person = :person AND location = :location AND sighted = :sighted",
                    {'name': name, 'person': person, 'location': location, 'sighted': sighted})
        insert = c.fetchone()
        print("\t", insert, "has been inserted into the SIGHTING database")
def get_flower_tuple(genus, species, comname):
    with conn:
        c.execute("SELECT * FROM FLOWERS WHERE genus = :genus AND species = :species AND comname = :comname",
            {'genus': genus, 'species': species, 'comname': comname})
        result = c.fetchone()
        return result
