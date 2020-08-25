import psycopg2
import covid


conn = psycopg2.connect(database="covid_data", 
                        user="postgres", password="Bobobones31$", host="127.0.0.1")
conn.set_session(autocommit=True)

cur = conn.cursor()
sql = "Insert into covid_data  (hash, date, states, positive, hostpitalizedCumulative, recovered, death,lastModified, total, deathIncrease) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 

# YOU NEED TO LOOK UP HOW TO INSERT these records PROPERLY 

cur.execute(sql)

cur.close(sql)

conn.close(sql)

