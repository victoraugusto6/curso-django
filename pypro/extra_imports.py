from django.db import connection, reset_queries

from pypro.settings import DEBUG

if DEBUG:
    def num_queries(reset=True):
        print(len(connection.queries))
        if reset:
            reset_queries()
