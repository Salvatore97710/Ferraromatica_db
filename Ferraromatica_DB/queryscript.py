import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Salvio977",
    database="Ferraromatica"
)
cursor = db.cursor()
#Vogliamo stampare il nome dei dipendenti che iniziano con la lettera R e l'id del cliente ad essi associato
sql=("""select clienti.CLIENTE_id,dipendenti.NOME
from clienti,dipendenti
where clienti.DIPENDENTE_id=dipendenti.DIPENDENTE_id and dipendenti.NOME like 'R%'
order by dipendenti.DIPENDENTE_id;""")

cursor.execute(sql)

for x in cursor:
    print(x)
#Vogliamo il numero di dipendenti che hanno il ruolo di Caricatore
sql="select RUOLO, sum(1) AS NUM_CARICATORI from dipendenti group by RUOLO order by  NUM_CARICATORI desc;"   
cursor.execute(sql)
result=cursor.fetchall()

for x in result:  
    print(x)
#Vogliamo stampare il nome del cliente e la data per cui gli è stato fatto l'ordine, dei soli clienti per cui l'ordine è stato completato e l'importo è maggiore o uguale a 200 euro    
sql=("""select dipendenti.ZONA_SERVIZIO,ordini.DATA_ORDINE
from dipendenti,ordini,clienti,pagamenti
where dipendenti.DIPENDENTE_id=clienti.DIPENDENTE_id and clienti.CLIENTE_id=ordini.CLIENTE_id and (ordini.STATO='completato' and pagamenti.IMPORTO>= 200)
order by dipendenti.ZONA_SERVIZIO;""")
cursor.execute(sql)

result=cursor.fetchall()

for x in result:  
    print(x)
    