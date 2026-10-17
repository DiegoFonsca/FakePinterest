# 📸 FakePinterest

> Uma aplicação web completa inspirada no Pinterest, desenvolvida em Python com o framework Flask. O sistema permite autenticação segura de usuários, criação de perfil individual, feed interativo da comunidade e upload de imagens.

🌐 **Acesse a aplicação no ar:** [https://fakepinterest-g1nc.onrender.com](https://fakepinterest-g1nc.onrender.com)

---

## 📌 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Demonstração & Recursos](#-demonstração--recursos)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Arquitetura & Estrutura de Pastas](#-arquitetura--estrutura-de-pastas)
- [Como Executar Localmente](#-como-executar-localmente)
- [Implantação em Nuvem (Deploy)](#-implantação-em-nuvem-deploy)
- [Autor & Contato](#-autor--contato)
- [Licença](#-licença)

---

## 🎯 Sobre o Projeto

O **FakePinterest** foi desenvolvido com o objetivo de praticar conceitos fundamentais de desenvolvimento web Full Stack utilizando a linguagem Python e o ecossistema Flask. 

A aplicação engloba desde a modelagem de banco de dados relacional até o gerenciamento de sessões de usuário, validação de formulários, controle de acessos por rotas protegidas e manipulação de arquivos de mídia (imagens).

---

## ✨ Demonstração & Recursos

- 🔐 **Autenticação & Segurança:**
  - Cadastro de novos usuários com verificação de e-mail e username únicos.
  - Login e logout seguros com armazenamento de senhas criptografadas via `Bcrypt`.
  - Controle de acesso a páginas restritas através de decorators do `Flask-Login`.

- 👤 **Gerenciamento de Perfil:**
  - Página de perfil personalizada para cada usuário.
  - Exibição de todas as fotos publicadas pelo próprio usuário.
  - Opção de upload de fotos de perfil e posts.

- 🖼️ **Feed & Interatividade:**
  - Feed principal da comunidade reunindo as postagens de todos os usuários cadastrados.
  - Exibição organizada de imagens com layout responsivo.

---

## 🛠️ Tecnologias Utilizadas

### **Backend**
- **[Python 3](https://www.python.org/):** Linguagem principal do projeto.
- **[Flask](https://flask.palletsprojects.com/):** Microframework web para construção das rotas e regras de negócio.
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/):** ORM para abstração e manipulação do banco de dados.
- **[Flask-Login](https://flask-login.readthedocs.io/):** Gerenciamento de sessões de usuários.
- **[Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/):** Criptografia avançada e hashing de senhas.
- **[Flask-WTF / WTForms](https://flask-wtf.readthedocs.io/):** Criação e validação de formulários web.
- **[Gunicorn](https://gunicorn.org/):** Servidor HTTP WSGI para ambiente de produção.

### **Frontend**
- **HTML5 & CSS3:** Estruturação e estilização visual das páginas.
- **Jinja2:** Motor de templates integrado ao Flask para renderização dinâmica de dados.

### **Banco de Dados & Ferramentas**
- **SQLite:** Banco de dados relacional para ambiente de desenvolvimento local.
- **Virtualenv (`.venv`):** Isolamento das dependências do ambiente Python.
- **Git & GitHub:** Versionamento de código e hospedagem de repositório.
- **Render:** Plataforma PaaS para hospedagem da aplicação online.

---

## 📂 Arquitetura & Estrutura de Pastas

```text
fakepinterest/
├── fakepinterest/          # Pacote principal da aplicação Flask
│   ├── static/             # Arquivos estáticos da aplicação
│   │   ├── css/            # Estilos CSS customizados
│   │   ├── fotos_posts/    # Uploads de imagens publicadas
│   │   └── fotos_sites/    # Elementos visuais e ícones da interface
│   ├── templates/          # Arquivos HTML renderizados via Jinja2
│   │   ├── criarconta.html
│   │   ├── feed.html
│   │   ├── homepage.html
│   │   ├── navbar.html
│   │   └── perfil.html
│   ├── __init__.py         # Inicialização do app, banco de dados e login manager
│   ├── forms.py            # Definição e validação dos formulários
│   ├── models.py           # Modelagem das entidades (User, Foto) no SQLAlchemy
│   └── routes.py           # Regras de negócio e definição de rotas
├── instance/               # Armazenamento local do banco de dados SQLite (comunidade.db)
├── .gitignore              # Regras de exclusão de arquivos no Git
├── criar_banco.py          # Script de criação inicial do banco de dados
├── main.py                 # Ponto de entrada (entry point) para execução do servidor
└── requirements.txt        # Lista de dependências e bibliotecas do projeto

