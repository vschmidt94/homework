from .. import db


class Role(db.Model):
    """
    The Role object controls the database structure for user roles,
    """
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rolename = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    created_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Role '{}'>".format(self.rolename)