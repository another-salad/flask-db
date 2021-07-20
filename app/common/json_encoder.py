"""Json encoder for Decimal types"""

from decimal import Decimal

from flask.json import JSONEncoder


class DecimalJsonEncoder(JSONEncoder):
    """Corrects the default decimal encoding"""

    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)

        return super().default(o)
