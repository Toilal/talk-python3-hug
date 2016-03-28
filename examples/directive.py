import hug


@hug.directive()
def basic(default='hi', **kwargs):
    return default + ' there!'


@hug.local()
def english(greeting: basic='hello'):
    return greeting


@hug.local()
def american(greeting: basic):
    return greeting


assert english() == 'hello there!'
assert american() == 'hi there!'
assert english('OMG!') == 'OMG!'
