from flask import Flask,render_template, redirect, flash
from forms import LoginForm


app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index')
def index():
    user = {"name" : "Jesse"}
    return '''
        <html>
            <head></head>
            <body>
                <h1>
                    Hello, '''+ user['name'] +'''
                </h1>
            </body>
        </html>
    '''

@app.route('/blogTmplate')
def blogTpl():
    user = {"name" : "alvin"}
    lists = [{"value":"list1"},{"value":"list2"},{"value":"list3"}]
    return render_template("blog.html", title="home", user = user, lists=lists, show=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #获取表单对象
    form = LoginForm()
    #表单验证
    if form.validate_on_submit():
        #缓存数据 在重定向页面中获取
        flash('Login requested for name: ' + str(form.name.data))
        flash('password: ' + str(form.password.data))
        flash('remeber_me: ' + str(form.remember_me.data))
        #重定向
        return redirect('/blogTmplate')
    return render_template('login.html', title = 'Sign In', form=form)

if __name__ == '__main__':
    app.run(port="8088")
