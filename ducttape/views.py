from ducttape import *
from ducttape.models import *

@app.errorhandler(500)
@app.errorhandler(404)
@app.errorhandler(403)
def error(error):
    return render_template("error.html", error = error)

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

@app.route("/engine/")
def engine():
    return render_template("engine.html")

@app.route("/editor/")
def editor():
    return render_template("editor.html")

@app.route("/contribute/")
def contribute():
    return render_template("contribute.html")

@app.route("/download/")
def download():
    return render_template("download.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/donate/")
def donate():
    return render_template("donate.html")

@app.route("/thanks/", methods=["GET", "POST"])
def thanks():
    return render_template("thanks.html")
