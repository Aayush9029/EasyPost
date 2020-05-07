from flask import Flask, render_template, request
import os
app = Flask(__name__)
 
data_for_poll = {
   'question' : 'Which web framework do you use?',
   'fields'   : ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject']
}

poll_data_filename = './data/polldata.txt'
 

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/poll')
def poll():
    return render_template('poll/poll.html', data=data_for_poll)
 
@app.route('/poll-data')
def poll_data():
    vote = request.args.get('field')
    out = open(poll_data_filename, 'a')
    out.write(vote +"\n")
    out.close()
 
    return render_template('poll/thankyou.html', data=data_for_poll)
 
@app.route('/poll-results')
def poll_results():
    votes = {}
    total = 0
    for f in data_for_poll['fields']:
        votes[f] = 0
 
    f  = open(poll_data_filename, 'r')
    for line in f:
        vote = line.rstrip("\n")
        if vote in data_for_poll["fields"]:
            votes[vote] += 1
            total += 1
    
    return render_template('poll/results.html', data=data_for_poll, votes=votes, total=total)

@app.route('/form')
def form():
    return render_template('form/form_template.html')


@app.route('/login')
def login():
    return render_template('login/login.html')

@app.route('/signup')
def signup():
    return render_template('login/signup.html')

 
if __name__ == "__main__":
    app.run(debug=True)
