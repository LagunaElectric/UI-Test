from api import db

## pyright: reportGeneralTypeIssues=false
"""
Unfortunately, there seems to be a known issue with Pylance
(VSCode's type checker) where it is unable to correctly identify
SQLAlchemy's types; in this case, it gets angry about things surrounding
the 'db' object.

Since this file shouldn't be handling much logic or data anyway,
I'm disabling the "GeneralTypeIssues" reporting.
"""
class Test(db.Model):
    __tablename__: str = "MyTable"

    name = db.Column(db.String, primary_key=True, nullable=False)