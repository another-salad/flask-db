from decimal import Decimal

from flask.json import JSONEncoder


class DecimalJsonEncoder(JSONEncoder):
    """Corrects the default decimal encoding"""

    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)

        return super(DecimalJsonEncoder, self).default(obj)
