from persistent.mapping import PersistentMapping


class MyModel(PersistentMapping):
    __parent__ = __name__ = None


def appmaker(mongodb_root):
    if not 'app_root' in mongodb_root:
        app_root = MyModel()
        mongodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return mongodb_root['app_root']
