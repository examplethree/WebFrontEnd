from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def start():
    return render_template('test.html')

@app.route("/render/<user>")
def hello_html(user):
    # 渲染一个HTML网页模板
    return render_template('test.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
