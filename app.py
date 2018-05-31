from flask import Flask, request, jsonify

app = Flask(__name__)

database = []

@app.route('/movies', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		name = request.form['name']
		year = request.form['year']
		director = request.form['director']
		movie = {'name': name, 'year': year, 'director': director}
		database.append(movie)
		return jsonify(movie)
	return jsonify(database)



if __name__ == "__main__":
	app.run(debug = True)