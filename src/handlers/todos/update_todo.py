

from src.core.decorator.api_endpoint import api_endpoint
from src.core.decorator.api_params import api_params
from src.main import init

# Initialize context
init()


@api_endpoint()
@api_params(required=['idTodo'], optional=[])
def update_todo(event, context, resource, idTodo):
    return None, "Success"
