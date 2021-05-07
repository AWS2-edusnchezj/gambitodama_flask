from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods = ["POST"])
def change_position():
	positions = [
		{
			'position': ['1','1'],
			'allowedPositions': [
				['1','8'], ['8','1']
			]

		},
		{
			'position': ['1','8'],
			'allowedPositions': [
				['1','1'], ['8','8']
			]

		},
		{
			'position': ['8','8'],
			'allowedPositions': [
				['1','8'], ['8','1']
			]

		},
		{
			'position': ['8','1'],
			'allowedPositions': [
				['1','1'], ['8','8']
			]

		},
	]
	positionSelected = [request.form['actualColumn'], request.form['actualRow']]
	nextPosition = [request.form['column'], request.form['row']]

	for position in positions:
		if position['position'] == positionSelected:
			if nextPosition in position['allowedPositions']:
				return render_template('index.html', actualColumn=nextPosition[0], actualRow=nextPosition[1])
	

	return render_template('index.html', alert='El moviment que vols realitzar no és possible.', actualColumn=positionSelected[0], actualRow=positionSelected[1])

app.run(debug=True)