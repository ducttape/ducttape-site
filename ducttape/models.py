from ducttape import *

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(256))
    posted = db.Column(db.DateTime)
    text = db.Column(db.Text)

    def __init__(self, title, text):
        self.title = title
        self.posted = datetime.utcnow()
        self.text = text

    def __repr__(self):
        return "<BlogEntry %s>" % self.title

    def url(self):
        return url_for("blog_post", id = self.id)
