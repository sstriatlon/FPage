from flask.ext.testing import TestCase
from app import db, app
from app.models import User

TEST_SQLALCHEMY_DATABASE_URI = "sqlite:///app/test.sqlite"

class MyTest(TestCase):


    def setUp(self):
        db.create_all()
        ## create users:
        user = User('joe', 'joe@soap.com')
        user2 = User('jane', 'jane@soap.com')
        db.session.add(user)
        db.session.add(user2)
        db.session.commit()


    def test_get_all_users(self):
        users = User.query.all()
        assert len(users) == 2, 'Expect all users to be returned'

    def test_get_user(self):
        user = User.query.filter_by(username='joe').first()
        assert user.email == 'joe@soap.com', 'Expect the correct user to be returned'