from app import db, app
from app.common.models import Base
from .activedirectory import ActiveDirectory


class User(Base):
    # The model uses LDAP as a backend for most of the User data

    __tablename__ = 'user'

    username = db.Column(db.String(128))
    # The GUID of the user in LDAP
    # guid = db.Column(db.String(32))

    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        super(User, self).__init__(**kwargs)
        
        if not self.is_authenticated():
            return

    def get_manager(self):
        pass

    def get_team(self):
        pass

    # The following 4 functions are implemented for the flask-login module
    def get_id(self):
        # This method must return a unicode that uniquely identifies this user, and can be used to
        # load the user from the user_loader callback. Note that this must be a unicode
        # - if the ID is natively an int or some other type, you will need to convert it to unicode.
        return str(self.id)

    def is_authenticated(self):
        # This property should return True if the user is authenticated, i.e. they have provided
        # valid credentials. (Only authenticated users will fulfil the criteria of login_required.)
        user, domain = self.username.split('@')
        username = domain+'\\'+user
        ad = ActiveDirectory(app.config['AD_HOST'], app.config['AD_PORT'], username, self.password)
        return ad.bind()

    def is_active(self):
        # This property should return True if this is an active user - in addition to being
        # authenticated,  they also have activated their account, not been suspended, or any
        # condition your application has for rejecting an account. Inactive accounts may not log in
        # (without being forced of course).
        return True

    def is_anonymous(self):
        # This property should return True if this is an anonymous user.
        # (Actual users should return False instead.)
        return False
