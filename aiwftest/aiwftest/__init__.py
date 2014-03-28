from pyramid.config import Configurator
#from .models import appmaker
from urllib.parse import urlparse
from .resources import Root 
import pymongo


# def root_factory(request):
#     conn = get_connection(request)
#     return appmaker(conn.root())


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    """ Mongo Connection Config.
    """
    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = pymongo.MongoClient(
        host=db_url.scheme,
    )

    def add_db(request):
        db = config.registry.db[db_url.path[1:]]
        return db

    """ if db_url.username and db_url.password:
        db.authenticate(db_url.username, db_url.password) 
    """

    config.add_request_method(add_db, 'db', reify=True)
    """ End Mongo Connection Config
    """

    config.scan()
    return config.make_wsgi_app()

