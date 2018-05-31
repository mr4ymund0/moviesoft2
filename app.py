from flask import Flask, request, jsonify

app = Flask(__name__)

database = []

@app.route('/movies', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		id = len(database) + 1
		name = request.form['name']
		year = request.form['year']
		director = request.form['director']
		movie = {'id':id,'name': name, 'year': year, 'director': director}
		database.append(movie)
		return jsonify(movie)
	return jsonify(database)

@app.route('/movies/<int:id>', methods = ['GET'])
def search(id):
	mov_filter = list(filter(lambda n: n['id'] == id, database))
	return jsonify(mov_filter)

@app.route('/movies/<int:id>', methods = ['DELETE'])
def delete(id):
	mov_delete = list(filter(lambda n: n['id'] == id, database))
	database.remove(mov_delete[0])
	return jsonify(database)



if __name__ == "__main__":
	app.run(debug = True)