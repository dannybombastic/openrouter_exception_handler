import os
import traceback
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def send_exception_to_openrouter(exception_trace):
    api_key = os.getenv('APIKEY_OPENROUTER')

    if not api_key:
        print("⚠️ [OpenRouter] APIKEY_OPENROUTER no definida en las variables de entorno.")
        return "No API key provided. Unable to retrieve AI response."

    prompt = f"""
    Capturé esta excepción en mi aplicación Python:

    {exception_trace}

    Proporciona una explicación clara y posible solución para este error.
    """

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Eres un asistente que ayuda a resolver excepciones Python."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, json=data, headers=headers, timeout=10)

        if response.status_code == 200:
            try:
                result = response.json()
                ai_response = result.get('choices', [{}])[0].get('message', {}).get('content', '').strip()
                return ai_response if ai_response else "[OpenRouter] No se recibió una respuesta válida."
            except Exception as parse_err:
                return f"[OpenRouter] Error al procesar la respuesta: {parse_err}"

        return f"[OpenRouter] Error en la solicitud: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as req_err:
        return f"[OpenRouter] Error al conectarse a la API: {req_err}"


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            exception_trace = traceback.format_exc()
            print(f"❌ Excepción capturada:")
            ai_response = send_exception_to_openrouter(exception_trace)
            if ai_response:
                print(f"\n🤖 [Respuesta de OpenRouter.ai]:\n{ai_response}\n")
            raise  # Re-lanza la excepción original para no ocultar errores críticos
    return wrapper
