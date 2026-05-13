from flask import Flask


app = Flask(__name__) 

@app.route('/') 
def ola_mundo():
    return '''  <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - [Seu Nome]</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; background-color: #f4f4f4; }
        .container { max-width: 800px; margin: auto; background: #fff; padding: 30px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        header { text-align: center; border-bottom: 2px solid #333; padding-bottom: 20px; }
        header h1 { margin: 0; }
        section { margin-top: 20px; }
        h2 { color: #333; border-bottom: 1px solid #ccc; padding-bottom: 5px; }
        .info-contato { font-style: normal; }
        .experiencia, .educacao { margin-bottom: 15px; }
        .cargo { font-weight: bold; }
        .empresa-data { color: #555; font-size: 0.9em; }
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>[Seu Nome Completo]</h1>
        <p class="info-contato">
            [Cidade/Estado] | [Seu Telefone] | [Seu E-mail] | [Link do LinkedIn]
        </p>
    </header>

    <section id="sobre">
        <h2>Resumo Profissional</h2>
        <p>[Escreva um breve parágrafo sobre sua experiência, objetivos e principais habilidades.]</p>
    </section>

    <section id="experiencia">
        <h2>Experiência Profissional</h2>
        <div class="experiencia">
            <p class="cargo">[Cargo] - [Nome da Empresa]</p>
            <p class="empresa-data">[Mês/Ano Início] – [Mês/Ano Fim ou Atual]</p>
            <ul>
                <li>[Responsabilidade ou conquista 1]</li>
                <li>[Responsabilidade ou conquista 2]</li>
            </ul>
        </div>
        <!-- Adicione mais blocos .experiencia conforme necessário -->
    </section>

    <section id="educacao">
        <h2>Educação</h2>
        <div class="educacao">
            <p class="cargo">[Nome do Curso/Grau] - [Nome da Instituição]</p>
            <p class="empresa-data">[Ano de Início] – [Ano de Conclusão]</p>
        </div>
    </section>

    <section id="habilidades">
        <h2>Habilidades</h2>
        <ul>
            <li>[Habilidade 1, ex: Python, Excel Avançado]</li>
            <li>[Habilidade 2, ex: Gestão de Projetos]</li>
        </ul>
    </section>
</div>

</body>
</html>'''

@app.route('/decorator') 
def hello():
    return 'Decorators são um padrão de projeto estrutural, comuns em linguagens como Python e TypeScript, que permitem adicionar novos comportamentos a objetos, métodos ou classes existentes de forma dinâmica, sem alterar o código-fonte original. Eles "embrulham" o código original, permitindo executar ações antes ou depois da sua execução.' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) 