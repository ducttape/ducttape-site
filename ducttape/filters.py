from ducttape import *

@app.template_filter()
def time(s):
    return s.strftime("%B %d, %Y %I:%M %p")
