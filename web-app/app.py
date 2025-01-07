from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/project_1')
def profile():
    return render_template('project1.html')

@app.route('/projects')
def project_home():
    return render_template('project_home.html')

# ... tambahkan route untuk halaman lain ...

if __name__ == '__main__':
    app.run(debug=True)