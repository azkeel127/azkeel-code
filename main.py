from flask import Flask, render_template

app = Flask(__name__)

@app.route('/templates/')
def index():
    return render_template('index.html')

@app.route('/templates/about')
def about():
    return render_template('about.html')

@app.route("/templates/posts")
def posts():
    return render_template("posts.html")

if __name__ == '__main__':
    app.run(debug=True)
