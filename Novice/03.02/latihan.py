from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home/<name>')
def hello_world (name):
    return render_template("hello.html",user=name)


if __name__ == '__main__':
    app.run(debug=True)

