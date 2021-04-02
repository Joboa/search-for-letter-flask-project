from flask import Flask, render_template, request, escape

app = Flask(__name__)


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form,
              req.remote_addr,
              req.user_agent,
              res, file=log, sep='|')


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
def view_the_log() -> 'html':
    """Reading data from the log file and saving it in
    a container called contents"""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr',
              'User_agent', 'Results')
    """Rendering the data using the temaplate, viewlog"""
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
