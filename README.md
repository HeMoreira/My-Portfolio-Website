# My-Portfolio-Website

🇺🇸 An overview about my Developer skills and career information. Created with Django and basic HTML/CSS/JS. 

🇧🇷 Uma visão geral sobre minhas habilidades como desenvolvedor e informações da minha carreira. Criado com Django e HTML/CSS/JS básico.

[English](#about-the-project) 
• 
[Português](#sobre-o-projeto)

## 🇺🇸 English

### About the Project
A personal portfolio website designed to showcase my developer skills, projects, and career journey. Built with **Django** backend and a clean, responsive frontend using vanilla **HTML, CSS, and JavaScript**.

### Technologies & Tools
* **Backend:** Django (Python)
* **Frontend:** HTML5, CSS3, JavaScript

### Setting Up

#### 1. Clone the repository and navigate to the project folder
```bash
git clone https://github.com/HeMoreira/My-Portfolio-Website.git
cd My-Portfolio-Website
```
> Remember to define a virtual environment if you want

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Configure environment variables
```bash
touch .env
# Define in a .env file SECRET_KEY, DEBUG and ALLOWED_HOSTS
```
> Example (recommended):
> ```bash
> # in the .env file
> SECRET_KEY='your_secret_key'
> DEBUG=True
> ALLOWED_HOSTS=127.0.0.1,localhost
> ```

#### 4. Run the server
```bash
python manage.py runserver
```

Access: http://127.0.0.1:8000 or http://localhost:8000

## 🇧🇷 Português

### Sobre o Projeto
Um projeto pessoal para apresentar minhas habilidades como desenvolvedor, projetos e jornada na carreira. Criado com **Django** como backend e um frontend limpo e responsivo usando **HTML, CSS e JavaScript**.

### Tecnologias e Ferramentas
* **Backend:** Django (Python)
* **Frontend:** HTML5, CSS3, JavaScript

### Configuração

#### 1. Clone o repositório e acesse o diretório principal
```bash
git clone https://github.com/HeMoreira/My-Portfolio-Website.git
cd My-Portfolio-Website
```
> Lembre-se de definir um ambiente virtual caso queira

#### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

#### 3. Configurar variáveis de ambiente
```bash
touch .env
# Defina em um arquivo .env SECRET_KEY, DEBUG e ALLOWED_HOSTS
```
> Exemplo (recomendado):
> ```bash
> # no arquivo .env
> SECRET_KEY='sua_chave_secreta'
> DEBUG=True
> ALLOWED_HOSTS=127.0.0.1,localhost
> ```

#### 4. Rodar o servidor
```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000 ou http://localhost:8000