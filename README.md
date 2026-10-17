# 📸 FakePinterest

Uma aplicação web inspirada no Pinterest, desenvolvida em Python com o framework Flask. O sistema permite o cadastro e autenticação de usuários, personalização de perfil, além do upload e visualização de imagens em um feed dinâmico.

🌐 **Acesse a aplicação online:** [https://fakepinterest-g1nc.onrender.com](https://fakepinterest-g1nc.onrender.com)

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework Web:** Flask
- **Banco de Dados:** SQLite & Flask-SQLAlchemy (ORM)
- **Autenticação & Segurança:** Flask-Bcrypt & Flask-Login
- **Formulários:** Flask-WTF / WTForms
- **Front-end:** HTML5, CSS3, JavaScript
- **Gerenciamento de Ambientes:** Virtualenv (`.venv`)

---

## 🚀 Funcionalidades

- 🔐 **Autenticação Completa:** Cadastro de usuário e login com senhas criptografadas.
- 👤 **Perfil do Usuário:** Página personalizada contendo foto de perfil e publicações do usuário.
- 🖼️ **Upload de Fotos:** Envio de imagens para publicação no feed.
- 📰 **Feed de Posts:** Exibição de imagens publicadas pela comunidade.
- 🔒 **Rotas Protegidas:** Acesso restrito a páginas internas apenas para usuários autenticados.

---

## 📂 Estrutura do Projeto

```text
fakepinterest/
├── fakepinterest/          # Pacote principal da aplicação
│   ├── static/             # Arquivos estáticos (CSS, JS, fotos de perfil e posts)
│   ├── templates/          # Templates HTML (Jinja2)
│   ├── __init__.py         # Inicialização do app Flask e configurações
│   ├── forms.py            # Formulários de login, cadastro e postagem
│   ├── models.py           # Modelos de dados (User, Foto, etc.)
│   └── routes.py           # Definição das rotas e regras de negócio
├── instance/               # Banco de dados SQLite local
├── .gitignore              # Arquivos e pastas ignorados pelo Git
├── criar_banco.py          # Script de criação/inicialização do banco de dados
├── main.py                 # Arquivo principal para execução da aplicação
└── requirements.txt        # Dependências do projeto