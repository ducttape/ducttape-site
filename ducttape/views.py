from ducttape import app

@app.route("/")
def index():
    return "Oh hi there!"
