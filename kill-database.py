#
# This is a short script to kill all tables and fill them with new test data.
# It should be run from a virtualenv.
#

from ducttape import db
from ducttape.models import *
from datetime import datetime, timedelta

def _info(s):
    print s + (60 - len(s))*" ",

def _done():
    print " DONE."


_info("Recreating the tables...")
db.drop_all()
db.create_all()
_done()
