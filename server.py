from flask import Flask, session, redirect, url_for, request
import os,json

users=[]
runid=os.urandom(32)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    global users, runid
    if 'runid' not in session or session['runid'] != runid:
        session.pop('username', None)
        session['runid'] = runid
    if 'username' not in session:
        if request.method == 'POST':
            session['username'] = request.form['username']
            users.append(session['username'])
            return redirect(url_for('wotchat'))
        else:
            return '''
            <form action="" method="post" >
                <p><input type=text name=username style="font-size: 50pt;">
                <p><input type=submit value=Login style="font-size: 50pt;">
            </form>
        '''
    else:
        return redirect(url_for('wotchat'))


@app.route('/wotchat')
def wotchat():
    if 'runid' not in session or session['runid'] != runid or 'username' not in session:
        return redirect(url_for('login'))
    else:
        return app.send_static_file('chat_view.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True, port=8000)



