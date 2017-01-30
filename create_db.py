from views import db
from models import Task
from datetime import date


db.create_all()

# insert data
# db.session.add(Task("Finish this tutorial", date(2017, 2, 4), 10, 1))
# db.session.add(Task("Finish Real Python", date(2017, 6, 30), 10, 1))

# commit the changes
db.session.commit()
