"""First hug API (local, command-line, and HTTP access)"""
import hug


@hug.get(examples='name=Hug&age=1')
@hug.cli()
@hug.local()
def happy_birthday(name: hug.types.text, age: hug.types.number, timer: hug.directives.Timer=-1):
    """Says happy birthday to a user"""
    return {'message': 'Happy {0} Birthday {1}!'.format(age, name),
            'took': float(timer)}