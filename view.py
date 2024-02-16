#importando sqlite
import sqlite3 as lite

# criando conecção 
con = lite.connect('dados_livraria.db')


#CRUD


#  inserir dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventorio(nome_usuario,nome_do_livro,autor,data_do_emprestimo,data_de_entrega) VALUES(?,?,?,?,?)"
        cur.execute(query,i)



#  atualizar dados
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventorio SET nome_usuario=?,nome_do_livro=?,autor=?,data_do_emprestimo=?,data_de_entrega=? WHERE id=?"
        cur.execute(query,i)



#  deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventorio WHERE id=?"
        cur.execute(query,i)



#  ver dados
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventorio WHERE id=?"
        cur.execute(query,id)

        queue = cur.fetchall()
        for i in queue:
            ver_dados.append(i)
    return ver_dados



#ver item
def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventorio WHERE id=?"
        cur.execute(query,id)

        queue = cur.fetchall()
        for i in queue:
            ver_dados_individual.append(i)