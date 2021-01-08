class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("username", db.String(30))

    def __init__(self, name):
        self.name = name