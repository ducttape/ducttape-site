from ducttape import *
from ducttape.models import *

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/blog/")
def blog():
    posts = BlogPost.query.order_by(BlogPost.posted.desc()).all()
    return render_template("blog.html", posts = posts)

@app.route("/blog/<int:id>/")
def blog_post(id):
    post = BlogPost.query.filter_by(id = id).first_or_404()
    return render_template("blog_post.html", post = post)

