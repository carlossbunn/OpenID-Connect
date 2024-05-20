README
Descrição

Este projeto consiste em duas aplicações Flask que implementam um fluxo de autenticação utilizando Keycloak e OAuth do Google. A aplicação aplicaao.py gerencia a autenticação com Keycloak e redireciona para o serviço de login OAuth do Google. A aplicação serveroidc gerencia o processo de autenticação OAuth do Google e redireciona de volta para a aplicação aplicaao.py.
Pré-requisitos

    Python 3.x
    Flask
    Requests
    Um servidor Keycloak em execução na porta 8080
    Configuração OAuth do Google

Instalação

    Clone o repositório:

    sh

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Crie e ative um ambiente virtual:

sh

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

Instale as dependências:

sh

    pip install Flask requests

    Configure o servidor Keycloak e Google OAuth conforme necessário.

Configuração
Keycloak

    O servidor Keycloak deve estar em execução na URL http://localhost:8080.
    Atualize as variáveis username e password em aplicaao.py com as credenciais do Keycloak.

Google OAuth

    Registre seu aplicativo no Console de APIs do Google para obter o client_id e client_secret.
    Atualize as variáveis client_id e client_secret em serveroidc.

Execução

    Inicie a aplicação serveroidc:

    sh

python serveroidc.py

Inicie a aplicação aplicaao.py em outro terminal:

sh

    python aplicaao.py

    Acesse a URL http://127.0.0.1:8001/ no seu navegador.

Fluxo de Autenticação

    O usuário acessa http://127.0.0.1:8001/.
    A aplicação aplicaao.py tenta fazer login no Keycloak.
    Se o login no Keycloak for bem-sucedido, o usuário é redirecionado para o serviço de login OAuth do Google.
    O usuário faz login no Google.
    Após o login, o Google redireciona para o callback do serveroidc.
    O serveroidc obtém o token de acesso e redireciona de volta para o aplicaao.py com o token.
    O aplicaao.py armazena o token na sessão e permite o acesso ao recurso protegido.

Arquivos

    aplicaao.py: Gerencia a autenticação com Keycloak e redireciona para o serviço de login OAuth do Google.
    serveroidc.py: Gerencia o processo de autenticação OAuth do Google e redireciona de volta para a aplicação aplicaao.py.

Contribuição

    Faça um fork do repositório.
    Crie uma nova branch: git checkout -b minha-nova-feature.
    Faça commit das suas alterações: git commit -am 'Adiciona nova feature'.
    Envie para o branch: git push origin minha-nova-feature.
    Envie um Pull Request.

Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
