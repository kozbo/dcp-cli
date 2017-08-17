"""This file is autogenerated according to HCA api spec. Don't modify."""
from ...added_command import AddedCommand

class GetSubscriptions(AddedCommand):
    """Class containing info to reach the get endpoint of files."""

    @classmethod
    def _get_base_url(cls):
        return "https://hca-dss.czi.technology/v1"

    @classmethod
    def _get_endpoint_info(cls):
        return {'seen': True, 'body_params': {}, 'positional': [{'argument': 'uuid', 'required': False, 'required_for': ['/subscriptions/{uuid}'], 'description': 'A RFC4122-compliant ID for the subscription.', 'type': 'string', 'format': None, 'pattern': '[A-Za-z0-9]{8}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{12}'}], 'options': {'replica': {'array': False, 'required': True, 'required_for': ['/subscriptions', '/subscriptions/{uuid}'], 'description': 'Replica to fetch from. Can be one of aws, gcp, or azure.', 'type': 'string', 'format': None, 'pattern': None, 'metavar': None, 'in': 'query', 'hierarchy': ['replica']}}, 'requires_auth': True, 'description': 'Return a list of associated subscriptions, which contains the uuid,\nreplica, query, creator_uid, and callback_url.\n'}
