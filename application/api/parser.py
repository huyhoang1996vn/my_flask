from flask_restful import reqparse

def email(email_str):
    """Return email_str if valid, raise an exception in other case."""
    if valid_email(email_str):
        return email_str
    else:
        raise ValueError('{} is not a valid email'.format(email_str))

integration_parser = reqparse.RequestParser(bundle_errors=True)
integration_parser.add_argument(
    'username', dest='username',
    location='form', required=True,
    help='The user\'s username',
)
integration_parser.add_argument(
    'email', dest='email',
    type=email, location='form',
    required=True, help='The user\'s email',
)
integration_parser.add_argument(
    'user_priority', dest='user_priority',
    type=int, location='form',
    default=1, choices=range(5), help='The user\'s priority',
)
