from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
# MYSQL CONNECTION
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Elias20042005"
app.config["MYSQL_DB"] = "base_tienda"

mysql = MySQL(app)

# SETTING
app.secret_key = "mysecretkey"

#PAGINA PRINCIPAL COMPRAS
@app.route("/")
def form_page():
    return render_template("index.html")

#METODO PARA AGG PRENDAS
@app.route("/add_contact", methods=["POST"])
def add_contact():
    if request.method == "POST":
        fullname = request.form["fullname"]
        phone = request.form["phone"]
        email = request.form["email"]
        prenda = request.form["prenda"]
        cantidad = request.form["cantidad"]
        if prenda == "Chaqueta de Cuero":
            precio = 40.00
        elif prenda == "Buso de algodon":
            precio = 15.00
        elif prenda == "Body Rojo":
            precio = 20.00
        elif prenda == "Buso Jordan":
            precio = 50.00
        elif prenda == "Camisa casual":
            precio = 20.00
        elif prenda == "chaqueta+falda":
            precio = 60.00
        elif prenda == "Conjunto Casual":
            precio = 40.00
        elif prenda == "Conjunto Black":
            precio = 70.00
        elif prenda == "Conjunto Otoño":
            precio = 80.00
        elif prenda == "Conjuto Primera":
            precio = 85.00
        elif prenda == "Conjunto Univer.":
            precio = 75.00
        elif prenda == "Conjunto Gabardina":
            precio = 70.00
        elif prenda == "Pantalon Deportivo":
            precio = 20.00
        elif prenda == "Vestido Turqueza":
            precio = 40.00
        elif prenda == "Vestido H&M NEGRO":
            precio = 40.00
        elif prenda == "Vestido Zara Rojo":
            precio = 50.00
        elif prenda == "Conjunto Jeans":
            precio = 45.00
        
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO proyecto_table (fullname, phone, email, prenda, cantidad, precio) VALUE(%s,%s,%s,%s,%s,%s)",
            (fullname, phone, email, prenda, cantidad,precio),
        )
        mysql.connection.commit()
        flash("Registro Exitoso!")
        flash("Contact Added successfully")
        return redirect("/")
@app.route("/list")
def list_page():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM proyecto_table")
    data = cur.fetchall()
    return render_template("table_template.html", contacts=data)

#METODO DEVUELVE LOS DATOS DEL CLIENTE SELECCIONADO Y LOS PUEDE CAMBIAR
@app.route("/edit/<id>")
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM proyecto_table WHERE id = %s", (id,))
    data = cur.fetchall()
    return render_template("edit_contact.html", contact=data[0])


#METODO PARA ACTUALIZAR LA BASE DE DATOS UNA VEZ EDITADO LOS DATOS
@app.route("/update/<id>" , methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form["fullname"]
        phone = request.form["phone"]
        email = request.form["email"]
        prenda = request.form["prenda"]
        cantidad = request.form["cantidad"]
        if prenda == "Chaqueta de Cuero":
            precio = 40.00
        elif prenda == "Buso de algodon":
            precio = 15.00
        elif prenda == "Body Rojo":
            precio = 20.00
        elif prenda == "Buso Jordan":
            precio = 50.00
        elif prenda == "Camisa casual":
            precio = 20.00
        elif prenda == "chaqueta+falda":
            precio = 60.00
        elif prenda == "Conjunto Casual":
            precio = 40.00
        elif prenda == "Conjunto Black":
            precio = 70.00
        elif prenda == "Conjunto Otoño":
            precio = 80.00
        elif prenda == "Conjuto Primera":
            precio = 85.00
        elif prenda == "Conjunto Univer.":
            precio = 75.00
        elif prenda == "Conjunto Gabardina":
            precio = 70.00
        elif prenda == "Pantalon Deportivo":
            precio = 20.00
        elif prenda == "Vestido Turqueza":
            precio = 40.00
        elif prenda == "Vestido H&M NEGRO":
            precio = 40.00
        elif prenda == "Vestido Zara Rojo":
            precio = 50.00
        elif prenda == "Conjunto Jeans":
            precio = 45.00
        cur = mysql.connection.cursor()
        cur.execute("UPDATE proyecto_table SET fullname = %s, phone = %s, email = %s, prenda = %s,cantidad = %s,precio=%s WHERE id = %s ", (fullname,phone,email,prenda,cantidad,precio,id))
        mysql.connection.commit()
        flash('Actualizado con exito!')
        flash('Contact Update Successfully')
        return redirect(url_for('list_page'))
#METODO ELIMINA LA COMPRA
@app.route("/delete/<string:id>")
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM proyecto_table WHERE id = {0}".format(id))
    mysql.connection.commit()
    flash("Eliminado correctamente!")
    flash("Contact Removed Successfully")
    return redirect(url_for("list_page"))
@app.route("/search", methods=["POST"])
def search_contact():
    if request.method == "POST":
        fullname = request.form["fullname"]
        # Realiza una consulta SQL para buscar los datos de la compra por el nombre (fullname)
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM proyecto_table WHERE fullname LIKE %s", ('%' + fullname + '%',))
        data = cur.fetchall()

        print(data)  # Agrega esta línea para depuración

        return render_template("search_results.html", contacts=data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
