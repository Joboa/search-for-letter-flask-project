from flask import Flask, render_template, request, escape, session
from DBcm import UseDatabase
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'EncryptedSecretKey'

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""

        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    title = 'Here are your results'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results
                from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase', 'Letters', 'Remote_addr',
              'User_agent', 'Results')
    """Rendering the data using the temaplate, viewlog"""
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are NOT logged in.'


if __name__ == '__main__':
    app.run(debug=True)
