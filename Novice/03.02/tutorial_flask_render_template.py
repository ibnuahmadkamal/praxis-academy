from flask import Flask,render_template,url_for
app = Flask(__name__)

posts = [
    {
        'aothor': 'Andi',
        'title' : 'Buku Bacaan',
        'content' : 'First time',
        'date' : '13 agustus 2000'
    },
    {
        'aothor': 'Budi',
        'title' : 'Buku Dongeng',
        'content' : 'Second time',
        'date' : '13 April 2000'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home_page.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about_page.html",title = 'About')

if __name__ == '__main__':
    app.run(debug=True)
