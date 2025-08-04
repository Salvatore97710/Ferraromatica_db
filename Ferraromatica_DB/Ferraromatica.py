import mysql.connector

# Connessione al database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*****"
)
 
cursor = db.cursor()#creo il cursore
cursor.execute("CREATE DATABASE IF NOT EXISTS Ferraromatica")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*****",
    database="Ferraromatica"
)
cursor = db.cursor()
cursor.execute("CREATE TABLE DIPENDENTI(DIPENDENTE_id INT AUTO_INCREMENT PRIMARY KEY,NOME VARCHAR(255),RUOLO VARCHAR(255),ZONA_SERVIZIO VARCHAR(255))")
cursor.execute("""
CREATE TABLE CLIENTI (
   CLIENTE_id INT AUTO_INCREMENT PRIMARY KEY,
    DIPENDENTE_id INT,
    NOME VARCHAR(255),
    TIPO_ATTIVITA VARCHAR(255),
    CITTA VARCHAR(255),
    FOREIGN KEY (DIPENDENTE_id) REFERENCES DIPENDENTI(DIPENDENTE_id)
)
""")

cursor.execute("CREATE TABLE ORDINI(ORDINE_id INT AUTO_INCREMENT PRIMARY KEY,CLIENTE_id INT,DATA_ORDINE DATE,TOTALE_EURO INT,STATO VARCHAR(255),FOREIGN KEY (CLIENTE_id) REFERENCES CLIENTI(CLIENTE_id))")
cursor.execute("CREATE TABLE PAGAMENTI(PAGAMENTO_id INT AUTO_INCREMENT PRIMARY KEY,ORDINE_id INT,DATA_PAGAMENTO DATE,IMPORTO DECIMAL(10,2),METODO VARCHAR(255),FOREIGN KEY (ORDINE_id) REFERENCES ORDINI(ORDINE_id))")

sql= "INSERT INTO DIPENDENTI (nome,ruolo,zona_servizio) values(%s,%s,%s)"
values=[
    ("Massimiliano","Tecnico",None),       
    ("Alessio","Caricatore","Università Degli Studi Di Salerno"),   
    ("Marcello","Caricatore","Supermarket_Decò_AV"),       
   ("Raffaele","Caricatore","Aereoporto_di_Napoli"),
    ("Roberto","Caricatore","Supermarket_Decò_Salerno")          
]                                   
cursor.executemany(sql,values)
db.commit()

sql = "INSERT INTO CLIENTI (dipendente_id, nome, tipo_attivita, citta) VALUES (%s, %s, %s, %s)"
values=[      
    (2,"Università Degli Studi Di Salerno","Università","Salerno"),   
    (3,"Supermarket_Decò_AV","Supermercato","Avellino"),       
    (4,"Aereoporto_di_Napoli","Aereoporto","Napoli"),
    (5,"Supermarket_Decò_Salerno","Supermercato","Salerno")          
]                                   
cursor.executemany(sql,values)
db.commit()

sql = "INSERT INTO ORDINI (cliente_id, data_ordine, totale_euro, stato) VALUES (%s, %s, %s, %s)"
values = [
    (1, "2025-08-01", 200, "completato"),
    (2, "2025-08-02", 180, "in attesa"),
    (3, "2025-08-03", 220, "completato"),
    (4, "2025-08-04", 90, "completato")
]
cursor.executemany(sql, values)
db.commit()

sql = "INSERT INTO PAGAMENTI (ordine_id, data_pagamento, importo, metodo) VALUES (%s, %s, %s, %s)"
values = [
    (1, "2025-08-01", 200.00, "bonifico"),
    (3, "2025-08-04", 220.00, "contanti"),
    (4, "2025-08-05", 90.00, "POS")
]
cursor.executemany(sql, values)
db.commit()
