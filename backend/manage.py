# RVW: This structure feels very scattered. Originally thought it might
#       be analog to Django's MVT, but seems like there is a better organization
#       possible. Suggest refactoring to structure here:
#       http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
#       As that ^ seems to avoid the sprawl that's happening here.
import os
import unittest     # RVW: Consider moving tests to pytest. Need to research test fixtures more, but seems they could simplify testing.

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user
from app.main.model import role
from app.main.model import blacklist


# Allows use of environment variable to control environment
# TODO: look for alternative options.
# Seems like command line args would be cleaner argparse module
# RVW: Agree, not a fan of environment variables.
#      Flask-script Option module should be able to do what I'm thinking of.
#      That said - for a production machine, config file or env variable can enforce intentionality
app = create_app(os.getenv('FLASK_API_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

# RVW: Set up PEP8 formatter and linter - then use them!

@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    # RVW: hard-coded verbosity, command line args should be used for flexibility. Not a huge issue here, but on principle.
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()