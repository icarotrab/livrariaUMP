#importanto sqllite
import sqlite3 as lite

# criando conecção 
con = lite.connect('dados_livraria.db')

# criando tabela
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventorio(id INTEGER PRIMARY KEY AUTOINCREMENT, nome_usuario TEXT, nome_do_livro TEXT, autor TEXT, data_do_emprestimo DATE, data_de_entrega DATE,)")
