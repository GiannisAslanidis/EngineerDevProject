import sqlite3

#Create SQlite database function on disk memory
def create_Database():
    conn  = sqlite3.connect("sqlite/application_database.db")
    c= conn.cursor()
    c.execute("""CREATE TABLE users_info (
                 ID integer  PRIMARY KEY AUTOINCREMENT,
                 Username text,
                 Password text,
                 Email    text,
                 Phone_Number integer,
                 First_Name text,
                 Last_Name text,
                 Access_Level integer DEFAULT 1,
                 ID_Xwrwn_Prosvasis text DEFAULT null
                 )""")
    c.execute("""CREATE TABLE epoptes_info(
                 ID integer  PRIMARY KEY AUTOINCREMENT,
                 Username text,
                 Password text,
                 Email    text,
                 Phone_Number integer,
                 First_Name text,
                 Last_Name text,
                 ID_Xwrwn_Epopti text DEFAULT null
              )""")
    c.execute("""CREATE TABLE xwroi_idrymatos(
                 ID_xwrou integer  PRIMARY KEY AUTOINCREMENT,
                 xrisi_xwrou text,
                 onoma_xwrou text,
                 ID_epoptwn text 
                 )""")
    c.execute("""CREATE TABLE yliko_xwrwn(
                 typos text,
                 ID_ylikou integer  PRIMARY KEY AUTOINCREMENT,
                 posotita integer,
                 perigrafi_xrisis text,
                 katastasi text,
                 etairia text,
                 montelo text,
                 onomasia_organou text,
                 xronos_ktisis integer,
                 seiriakos_arithmos integer,
                 skopos_xrysis text,
                 varos integer,
                 diathesimotita text,
                 dinatotita_metakinisis text,
                 katastasi_daneismou text DEFAULT 'available',
                 lekseis_kleidia text,
                 katigoria text,
                 ypokatigoria text,
                 ID_Xwrou integer
                 )""")
    insert_Admin(conn, c)
    return conn


#Insert Admin Key to Database function
def insert_Admin(connection,cursor):
    with connection:
        cursor.execute("""INSERT INTO users_info('Username','Password','Email','Phone_Number','First_Name','Last_Name','Access_Level')
                         VALUES ('admin','2932019','admin@gmail.com',6975837283,'Dimitris','Zarogiannis',2)
                         """)


