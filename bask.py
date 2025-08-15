from flask import Flask, render_template

app = Flask(__name__)

# Dados de exemplo para os times e jogadores
teams_data = {
    'lakers': {
        'name': 'Los Angeles Lakers',
        'logo': 'lakers.png',
        'players': [
            {'name': 'LeBron James', 'number': 23},
            {'name': 'Anthony Davis', 'number': 3},
            {'name': 'D\'Angelo Russell', 'number': 1}
        ]
    },
    'celtics': {
        'name': 'Boston Celtics',
        'logo': 'celtics.png',
        'players': [
            {'name': 'Jayson Tatum', 'number': 0},
            {'name': 'Jaylen Brown', 'number': 7},
            {'name': 'Kristaps Porzingis', 'number': 8}
        ]
    }
}

@app.route('/')
def home():
    # Renderiza a página inicial, passando os dados dos times
    return render_template('index.html', teams=teams_data)

@app.route('/team/<team_id>')
def team_page(team_id):
    # Encontra o time pelo ID na URL
    team = teams_data.get(team_id)
    if not team:
        # Retorna um erro 404 se o time não for encontrado
        return "Time não encontrado", 404
    # Renderiza a página do time, passando os dados do time
    return render_template('team.html', team=team)

if __name__ == '__main__':
    app.run(debug=True)