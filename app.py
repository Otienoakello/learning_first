from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dictionary to store car data
car_database = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        country = request.form['country']

        # Store in dictionary
        car_database[make] = {
            'model': model,
            'year': year,
            'country': country
        }
        return redirect('/')  # Refresh the page

    return render_template('form.html', cars=car_database)


if __name__ == '__main__':
    app.run(debug=True)
