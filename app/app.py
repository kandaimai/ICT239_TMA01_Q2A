from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from books import all_books  # Import the all_books list from books.py

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

@app.route('/', methods = ['GET', 'POST'])
def list_books():
    if request.method == 'GET':
        return render_template('book_list.html', books=all_books)
    elif request.method == 'POST':
        cat = request.form['cat']
        filtered_books = [book for book in all_books if book['category'] ==  cat]
        #return cat
        return render_template('book_list.html', books=filtered_books)

'''
@app.route('/book_cat/', methods = ['GET', 'POST'])
def list_book_cat(cat):

    return render_template('book_list.html', books=all_books, cat = cat)

'''
