from google.appengine.ext import db

class Burndown(db.Model):
    owner = db.UserProperty()

# Burndown
# Name
# Type (Burnup / Burndown)
# start date, end date
# owner