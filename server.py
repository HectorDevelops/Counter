from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "La Republica Dominicana 🇩🇴"

#  Main route when rendering our page
@app.route('/')
def counter():
    #  Checks the current counter of session and increments the amount of times we have visited the site
    if 'num_visits' in session:
        session['num_visits'] += 1
    #  If session has not been refreshed/revisited then counter remains at 1
    else:
        session['num_visits'] = 1
    #  Setting a variable in order to pass data to our rendered page via Jinja syntax
    visits = session.get('num_visits')
    return render_template('counter.html', visits = visits)

#  Creating a new route for the times the user clicks the add button 
@app.route('/buttonIncrement', methods=['POST'])
def buttonIncrement():
    # check if user has visited the site, and if so, the counter will be incremeented by +2
    if 'num_visits' in session:
        session['num_visits'] += 2

    return redirect('/')

# This route is meant for the reset, 
@app.route('/reset', methods=['POST'])
def reset():
    #  If user has clicked this reset button, the couner will be reset to 1 
    if 'num_visits' in session:
        session.clear()

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
