from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route("/")

def hello():
    return "hello"
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

#device
@app.route('/device/<name>')
def device(name=None):
    return render_template('device.html', name=name)
