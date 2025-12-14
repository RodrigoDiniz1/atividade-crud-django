# 📋 Sistema CRUD de Funcionários - Django + MySQL

Sistema de gerenciamento de funcionários desenvolvido com Django e MySQL.

## 🚀 Funcionalidades

- ✅ **Create** - Cadastrar novos funcionários
- ✅ **Read** - Listar todos os funcionários
- ✅ **Update** - Editar dados de funcionários
- ✅ **Delete** - Remover funcionários
- ✅ **Detail** - Visualizar detalhes de um funcionário

## 🛠️ Tecnologias

- Python 3.12
- Django 6.0
- MySQL
- Bootstrap 5 (django-bootstrap5)
- Fonte Saira (Google Fonts)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/RodrigoDiniz1/atividade-crud-django.git
cd atividade-crud-django
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install django mysqlclient django-bootstrap5
```

4. Crie o banco de dados MySQL:
```sql
CREATE DATABASE funcionarios;
```

5. Configure o banco em `funcionario/settings.py` (se necessário)

6. Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Inicie o servidor:
```bash
python manage.py runserver
```

## 🔗 URLs

| Operação | URL |
|----------|-----|
| Listar | http://localhost:8000/app/lista_funcionarios |
| Cadastrar | http://localhost:8000/app/form_funcionario |
| Editar | http://localhost:8000/app/form_funcionario/{id} |
| Detalhes | http://localhost:8000/app/lista_funcionario/{id} |
| Remover | http://localhost:8000/app/remover_funcionario/{id} |

## 📁 Estrutura do Projeto

```
atividade-crud/
├── manage.py
├── funcionario/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── app/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
        ├── base.html
        ├── form_funcionario.html
        ├── lista_funcionarios.html
        ├── lista_funcionario.html
        └── remover_funcionario.html
```

## 👤 Autor

Rodrigo Diniz
