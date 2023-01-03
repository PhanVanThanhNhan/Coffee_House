from apps import db, app

class Khachhang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable=False)
    taikhoan = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(150), unique=True, nullable=False)
    matkhau = db.Column(db.String(180), unique=False, nullable=False)
    def __repr__(self):
        return '<Khachhang %r>' % self.taikhoan



# class addtt(db.Model):
#     name = db.Column(db.String(40), unique=False, nullable=False)
#     phone = db.Column(db.String(10), unique=True, nullable=False)
#     address = db.Column(db.String(150), unique=True, nullable=False)
#     matkhau = db.Column(db.String(180), unique=False, nullable=False)
#     def __repr__(self):
#         return '<addtt %r>' % self.title

with app.app_context():
    db.create_all()