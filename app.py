from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from books import all_books  # Import the all_books list from books.py

app = Flask(__name__)

@app.route('/books')
def list_books():
    return render_template('base.html', books=all_books)

