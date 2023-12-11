import mysql.connector

conn = mysql.connector.connect(host = "localhost", password = "123456", user = "root")

mycursor = conn.cursor()

str = "SELECT COUNT(*) FROM `filmdata`.`movieinformation`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
movie_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`writers`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
writers_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`cast`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
cast_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`music`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
music_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`cinematography`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
cinematography_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`editing`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
editing_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`director`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
director_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`produced`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
produced_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`specialeffects`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
special_effect_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`genres`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
genres_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`taglines`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
taglines_id = count + 1

str = "SELECT COUNT(*) FROM `filmdata`.`did_you_know`;"
mycursor.execute(str)
count = mycursor.fetchone()[0]
did_you_know_id = count + 1

print("movie_id: ", movie_id)
print("writers_id: ", writers_id)
print("cast_id: ", cast_id)
print("music_id: ", music_id)
print("cinematography_id: ", cinematography_id)
print("editing_id: ", editing_id)
print("director_id: ", director_id)
print("produced_id: ", produced_id)
print("special_effect_id: ", special_effect_id)
print("genres_id: ", genres_id)
print("taglines_id: ", taglines_id)
print("did_you_know_id: ", did_you_know_id)

mycursor.close()
conn.close()