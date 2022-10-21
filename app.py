#from flask import Flask

#app = Flask(__name__)

#@app.route("/")


#def index():
#    print ("Hello World")


#if __name__ == "__main__":
#    app.run()


from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__ , static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')
 
 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
 
 
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
 
 
if __name__ == '__main__':
    app.run(debug=True)