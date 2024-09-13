from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Matrix addition route
@app.route('/add_matrices', methods=['POST'])
def add_matrices():
    try:
        # Getting matrices from form
        matrix1 = [list(map(int, row.split())) for row in request.form['matrix1'].splitlines()]
        matrix2 = [list(map(int, row.split())) for row in request.form['matrix2'].splitlines()]

        # Ensure matrices have the same size
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            return "Matrices must have the same dimensions."

        # Add matrices
        result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

        return render_template('index.html', result=result_matrix)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
  
