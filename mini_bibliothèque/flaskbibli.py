import os
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import mysql.connector

app = Flask(__name__)
app.secret_key = "mini-bibliotheque-secret-key"


def connection_bibli():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mini_bibliotheque",
        autocommit=True,
    )


@app.route("/")
def index():
    return redirect(url_for("login_user"))


@app.route("/login", methods=["GET", "POST"])
def login_user():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("pass_word", "").strip()

        if not username or not password:
            error = "Veuillez saisir un nom d'utilisateur et un mot de passe."
        else:
            try:
                conn = connection_bibli()
                cursor = conn.cursor(dictionary=True)
                cursor.execute(
                    "SELECT * FROM users WHERE username = %s AND pass_word = %s",
                    (username, password),
                )
                user = cursor.fetchone()
                conn.close()
            except mysql.connector.Error as exc:
                error = f"Erreur de connexion à la base de données : {exc}"
                user = None

            if user:
                session["user"] = {
                    "id": user["id_user"],
                    "username": user["username"],
                }
                return redirect(url_for("liste_livre"))

            error = "Nom d'utilisateur ou mot de passe incorrect."

    return render_template("login.html", error=error)


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("login_user"))


@app.route("/pdf/<path:filename>")
def serve_pdf(filename):
    return send_from_directory(os.path.join(app.static_folder, "livres"), filename)


def build_pdf_url(file_path):
    if not file_path:
        return "#"
    if file_path.startswith(("http://", "https://", "/")):
        return file_path
    return url_for("serve_pdf", filename=file_path.lstrip("/"))


@app.route("/mini_bibliotheque")
def liste_livre():
    if "user" not in session:
        return redirect(url_for("login_user"))

    try:
        conn_livre = connection_bibli()
        cursor_livre = conn_livre.cursor(dictionary=True)
        cursor_livre.execute("SELECT * FROM livres ORDER BY titre")
        livres = cursor_livre.fetchall()

        for livre in livres:
            livre["pdf_url"] = build_pdf_url(livre.get("chemin_pdf"))

        cursor_livre.execute("SELECT COUNT(*) AS total FROM livres")
        total_row = cursor_livre.fetchone()
        total = total_row["total"] if total_row else 0
        conn_livre.close()
    except mysql.connector.Error as exc:
        return render_template("mini_bibliotheque.html", livres=[], total=0, user=session["user"], error=f"Erreur de base de données : {exc}")

    return render_template("mini_bibliotheque.html", livres=livres, total=total, user=session["user"], error=None)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)