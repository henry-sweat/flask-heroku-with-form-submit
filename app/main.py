from flask import Flask, render_template, request, url_for, flash, redirect
import pandas as pd
import psycopg2
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
db_uri = os.environ['DB_URI']

@app.route('/')
def home():
   # create a new database connection by calling the connect() function
   con = psycopg2.connect(db_uri)
   # query
   query = 'SELECT * FROM amounts'
   # return results as df
   df = pd.read_sql(query, con)
   # convert df to html table
   table = df.to_html(index=False)
   #close connection
   if con is not None:
      con.close()

   return render_template('index.html',table=table)

@app.route('/submit/', methods=('GET', 'POST'))
def submit():
   if request.method == 'POST':
      date = request.form['reportdate']
      name = request.form['firstname']
      amount = request.form['dollaramount']

      if not date:
         flash('Date is required!')
      elif not name:
         flash('Name is required!')
      elif not amount:
         flash('Amount is required!')
      else:
         # create a new database connection by calling the connect() function
         con = psycopg2.connect(db_uri)
         # create a new cursor
         cur = con.cursor()
         # Create a new record
         sql = "INSERT INTO amounts VALUES (%s, %s, %s)"
         cur.execute(sql, (date, name, amount))
         # commit changes
         con.commit()
         # close connection
         if con is not None:
            cur.close()
            con.close()
         return redirect(url_for('home'), code=307)
   return  render_template('form.html')