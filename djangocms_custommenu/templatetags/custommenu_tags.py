from django.core.serializers import serialize
from django.db.models.query import QuerySet
import json
from django.template import Library

register = Library()


def jsonify(obj):
    try:
        if isinstance(obj, QuerySet):
            return serialize('json', obj)
        if isinstance(obj, str) or isinstance(obj, unicode):
            obj = json.loads(obj)
    except:
        obj = {"error": "could not perform jsonify"}
    return json.dumps(obj)

register.filter('jsonify', jsonify)
