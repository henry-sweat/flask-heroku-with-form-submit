# flask-heroku-with-form-submit
this is the template for a python flask app hosted on heroku that takes html form submissions, then adds them to a 
postgres database

### Notes
sqlalchemy is the library for connecting pandas and an sql database, whereas psycopg2 is for connecting python in 
general and an sqldatabase.</br>
the environment variable are established in the heroku dashboard. the uri for the database changes intermittently, 
and this program does not account for that.</br>
</br>
https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
