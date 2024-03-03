Google OAuth 2.0 and OpenID Connect Example

Este é um exemplo simples de como usar OAuth 2.0 e OpenID Connect com a API do Google para autenticação e autorização de usuários.
Pré-requisitos

    Python 3.x instalado
    Módulo requests instalado (pode ser instalado usando pip install requests)

Configuração

    Crie um projeto no Google Cloud Console.
    Configure as credenciais do OAuth 2.0 no Console de Credenciais.
    Copie e cole as chaves do cliente (client_id e client_secret) no código.

Executando o Exemplo
1. Iniciando o Fluxo de Autorização

bash

python authorization.py

Este script imprimirá uma URL. Visite essa URL em seu navegador, faça login e autorize o acesso. Copie o código de autorização da URL.
2. Recebendo o Token de Acesso e Informações do Usuário

bash

python server.py

Este script inicia um servidor local na porta 8000 para receber o código de autorização. Cole o código de autorização quando solicitado. O servidor então trocará o código por um token de acesso e fornecerá as informações do usuário.
Notas

    Certifique-se de configurar corretamente as URLs de redirecionamento no Console de Credenciais.
    Este exemplo é para fins educacionais e pode precisar ser adaptado para ambientes de produção.

Lembre-se de que este README é uma base e pode ser expandido conforme necessário, dependendo das informações específicas que você deseja fornecer aos usuários do seu código.
