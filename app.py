from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Constants
HOURS_PER_WEEK = 40
WEEKS_PER_YEAR = 52  # Assuming 52 weeks in a year
DAYS_PER_WEEK = 5  # Assuming 5 working days in a week
MONTHS_PER_YEAR = 12  # Assuming 12 months in a year

@app.route('/', methods=['GET', 'POST'])
def salary_calculator():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_salary():
    try:
        hourly_rate = None
        monthly_salary = None
        weekly_salary = None
        daily_salary = None
        yearly_salary = None

        # Check which input field was updated and calculate the corresponding values
        if 'yearly_salary' in request.form:
            yearly_salary = float(request.form.get('yearly_salary'))
            hourly_rate = yearly_salary / (HOURS_PER_WEEK * WEEKS_PER_YEAR)
            monthly_salary = yearly_salary / MONTHS_PER_YEAR
            weekly_salary = yearly_salary / WEEKS_PER_YEAR
            daily_salary = weekly_salary / DAYS_PER_WEEK
        elif 'hourly_rate' in request.form:
            hourly_rate = float(request.form.get('hourly_rate'))
            yearly_salary = hourly_rate * HOURS_PER_WEEK * WEEKS_PER_YEAR
            monthly_salary = yearly_salary / MONTHS_PER_YEAR
            weekly_salary = yearly_salary / WEEKS_PER_YEAR
            daily_salary = weekly_salary / DAYS_PER_WEEK
        elif 'monthly_salary' in request.form:
            monthly_salary = float(request.form.get('monthly_salary'))
            yearly_salary = monthly_salary * MONTHS_PER_YEAR
            hourly_rate = yearly_salary / (HOURS_PER_WEEK * WEEKS_PER_YEAR)
            weekly_salary = yearly_salary / WEEKS_PER_YEAR
            daily_salary = weekly_salary / DAYS_PER_WEEK
        elif 'weekly_salary' in request.form:
            weekly_salary = float(request.form.get('weekly_salary'))
            yearly_salary = weekly_salary * WEEKS_PER_YEAR
            hourly_rate = yearly_salary / (HOURS_PER_WEEK * WEEKS_PER_YEAR)
            monthly_salary = yearly_salary / MONTHS_PER_YEAR
            daily_salary = weekly_salary / DAYS_PER_WEEK
        elif 'daily_salary' in request.form:
            daily_salary = float(request.form.get('daily_salary'))
            weekly_salary = daily_salary * DAYS_PER_WEEK
            yearly_salary = weekly_salary * WEEKS_PER_YEAR
            hourly_rate = yearly_salary / (HOURS_PER_WEEK * WEEKS_PER_YEAR)
            monthly_salary = yearly_salary / MONTHS_PER_YEAR

        return render_template('index.html', 
                               yearly_salary=yearly_salary,
                               hourly_rate=hourly_rate,
                               monthly_salary=monthly_salary,
                               weekly_salary=weekly_salary,
                               daily_salary=daily_salary)
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter valid values.'})

if __name__ == '__main__':
    app.run(debug=True)
