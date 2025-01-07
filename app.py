import google.generativeai as genai
import os
from flask import Flask, render_template, request
from database import get_user, list_users
from functions import oferecer_plano_anual, motivar_envio_fotos, atualizar_envio_fotos, oferecer_desconto_primeira_aula
app = Flask(__name__)

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

magical_if = genai.GenerativeModel("gemini-1.5-flash",
                                   generation_config={"temperature": 0.5},
                                   tools = [oferecer_plano_anual, motivar_envio_fotos, atualizar_envio_fotos, oferecer_desconto_primeira_aula])

app = Flask(__name__)
# Página inicial que lista todos os usuários
@app.route('/')
def index():
    users = list_users()
    return render_template('index.html', users=users)
# Página de detalhes do usuário e interação com a IA
@app.route('/user/<user_id>', methods=['GET', 'POST'])
def user_details(user_id):
    user = get_user(user_id)
    if not user:
        return "Usuário não encontrado", 404
    if request.method == 'POST':
        # Aqui a IA tomaria a decisão com base nos dados do usuário
        pass
    return render_template('user.html', user=user, user_id=user_id)
if __name__ == '__main__':
    app.run(debug=True)