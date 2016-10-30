from db import db_session, User

authors = [
    {
        'first_name': 'Василий',
        'last_name': 'Петров',
        'email': 'vasy@blabla.com'
    },
    {
        'first_name': 'Маща',
        'last_name': 'Смирнова',
        'email': 'masha@blabla.com'
    },
    {
        'first_name': 'Эдурд',
        'last_name': 'Фомин',
        'email': 'edick@blabla.com'
    }
]        

for a in authors:
    author = User(a['first_name'], a['last_name'], a['email'])
    db_session.add(author)

db_session.commit()