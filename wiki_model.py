from google.appengine.ext import db

class Todo(db.Model):
    title = db.StringProperty(required=True)
    body = db.TextProperty(required=True)