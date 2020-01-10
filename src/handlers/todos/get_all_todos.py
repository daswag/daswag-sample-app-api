

from src.core.decorator.api_endpoint import api_endpoint
from src.core.decorator.api_params import api_params
from src.main import init

# Initialize context
init()


@api_endpoint()
@api_params()
def get_all_todos(event, context, resource):
    return None, "Success"
