from flask import Flask, render_template , request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/home.html')
@app.route('/blog')
def blog():
    return render_template('pages/blog.html')
@app.route('/about')
def about():
    return render_template('pages/about.html')
@app.route('/mission')
def mission():
    return render_template('pages/mission.html')

@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        person_name = request.form ['name']
        return f'hello {person_name}!'    
    return render_template('pages/register.html')

if __name__ == '__main__':
    app.run(debug = True)