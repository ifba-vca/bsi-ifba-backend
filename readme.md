# BSI IFBA-VCA Backend

> Sistema dedicado ao curso de Sistemas de Informação do IFBA Campus Vitória da conquista.

# Pré Requesitos

-   Python v3.8
-   [Virtualenv](https://virtualenv.pypa.io/en/latest/)

# Instalação

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

> **Obs:** Para fazer a ativação do virtualenv no Windows substitua ~~source venv/bin/activate~~ por **virtualenv\venv\Scripts\activate**

# Variáveis de ambiente

-   Copie o arquivo _.env_example_ para a raiz do projeto renomeando para **.env**;

-   Preencha com as informações do banco de dados de desenvolvimento;

```
DB_HOST=127.0.0.1
DB_ENGINE=django.db.backends.postgresql
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_PORT=8000
```

## Gerar secret key

    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

-   Salve a saída na variáveil `SECRET_KEY` no arquivo .env

# Criação do BD

**Execução dos migrates**

    python manage.py migrate

**Criar um novo usuário**

    python manage.py createsuperuser

# Testes

    python manage.py test

# Executar a aplicação

    python manage.py runserve

> Acesse o admin em **/admin**

# Documentation

## Api requests

### Criado com [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/).

### Acesse na rota incial do projeto

![swagger_1](https://github.com/flaviofilipe/bsi-ifba-backend/blob/master/docs/images/swagger_1.png?raw=true)

![swagger_2](https://github.com/flaviofilipe/bsi-ifba-backend/blob/master/docs/images/swagger_2.png?raw=true)

![swagger_3](https://github.com/flaviofilipe/bsi-ifba-backend/blob/master/docs/images/swagger_3.png?raw=true)
![swagger_4](https://github.com/flaviofilipe/bsi-ifba-backend/blob/master/docs/images/swagger_4.png?raw=true)

> **Obs:** Para inserir novas informações é necessário acessar o painel de admin via browser.
