import os
import traceback
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def send_exception_to_openrouter(exception_trace):
    api_key = os.getenv('APIKEY_OPENROUTER')

    if not api_key:
        print("⚠️ [OpenRouter] APIKEY_OPENROUTER no definida en las variables de entorno.")
        return None

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

    response = requests.post(API_URL, json=data, headers=headers)

    if response.status_code == 200:
        try:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        except Exception as parse_err:
            return f"[OpenRouter] Error al procesar la respuesta: {parse_err}"
    else:
        return f"[OpenRouter] Error en la solicitud: {response.status_code} - {response.text}"

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            exception_trace = traceback.format_exc()
            print(f"❌ Excepción capturada:\n{exception_trace}")
            ai_response = send_exception_to_openrouter(exception_trace)
            if ai_response:
                print(f"\n🤖 [Respuesta de OpenRouter.ai]:\n{ai_response}\n")
            raise  # Re-lanza la excepción original para no ocultar errores críticos
    return wrapper
