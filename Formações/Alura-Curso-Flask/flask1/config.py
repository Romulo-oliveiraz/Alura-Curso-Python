SECRET_KEY = 'junin'

#cria uma URI na config do app para fazer a conexão com o banco de dados (MYSQL).
SQLALCHEMY_DATABASE_URI = '{SGDB}://{user}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',
        user = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'jogoteca'
    )