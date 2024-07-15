# api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    if request.method == "POST":
        # Handle POST request
        received_json_data = json.loads(request.body)
        message = received_json_data.get("name", "No message received.")

        data = {
            "message": f"This is a POST request. Received message: {message}"
        }
        return JsonResponse(data)
