from pyramid.view import view_config
from aiwftest.resources import Root
from aiwftest.resources import AiwfQuotes
from random import randrange


@view_config(context=Root, renderer='templates/aiwfhome.pt')
def home_view(request):
    quotes_data = AiwfQuotes(request)
    quotes      = []
    quote_size  = 0

    # Hak that needs some more explination
    for q in quotes_data.get_quotes():
        quote_size = q.count()
        for r in range(0, quote_size):
            quotes.append(q[r])
    return { 'quotes': quotes[randrange(0, quote_size)] }


