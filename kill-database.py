#
# This is a short script to kill all tables and fill them with new test data.
# It should be run from a virtualenv.
#

from ducttape import db
from ducttape.models import *
from datetime import datetime, timedelta

def _info(s):
    print s + "..." + (60 - len(s))*" ",

def _done():
    print " DONE."


_info("Recreating the tables")
db.drop_all()
db.create_all()
_done()


_info("Blogging a bit")
post1 = BlogPost("We have a website", "Today we set up this awesome website. It is still in the making, but you can already admire its awesomeness.")
db.session.add(post1)

post2 = BlogPost("New github organization founded", "Another great thing we did today: we founded the github organization [ducttape](https://github.com/ducttape) for all our projects related to the engine.")
db.session.add(post2)
_done()


_info("Saving")
db.session.commit()
_done()
