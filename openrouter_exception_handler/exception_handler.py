import os
import traceback
import requests
import inspect  # Importamos inspect para obtener el código fuente

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def send_exception_to_openrouter(prompt):
    """
    Envía el prompt (que incluye la excepción y el código fuente) a OpenRouter,
    usando la API Key definida en la variable de entorno APIKEY_OPENROUTER.
    Devuelve el mensaje de la IA o un mensaje de error si la solicitud falla.
    """
    api_key = os.getenv('APIKEY_OPENROUTER')
    llmodel = os.getenv('LLMODEL', 'openai/gpt-3.5-turbo')
    if not api_key or not llmodel:
        print("⚠️ [OpenRouter] APIKEY_OPENROUTER no definida en las variables de entorno.")
        return "No API key provided. Unable to retrieve AI response."

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": f"{llmodel}",
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
                ai_response = (
                    result.get('choices', [{}])[0]
                          .get('message', {})
                          .get('content', '')
                          .strip()
                )
                return ai_response if ai_response else "[OpenRouter] No se recibió una respuesta válida."
            except Exception as parse_err:
                return f"[OpenRouter] Error al procesar la respuesta: {parse_err}"
        return f"[OpenRouter] Error en la solicitud: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as req_err:
        return f"[OpenRouter] Error al conectarse a la API: {req_err}"


def exception_handler(func):
    """
    Decorador para funciones o métodos individuales.
    Captura cualquier excepción, imprime la información,
    obtiene el código fuente de la función y solicita a OpenRouter
    una explicación y posibles soluciones, incluyendo el código fuente.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Intentamos obtener el código fuente de la función
            try:
                source_code = inspect.getsource(func)
            except Exception as src_err:
                source_code = "No se pudo obtener el código fuente: " + str(src_err)
            exception_trace = traceback.format_exc()
            print(f"❌ Excepción capturada en '{func.__name__}': {e}")
            print("Código fuente del error:")
            print(source_code)
            # Combinamos la traza de error y el código fuente en un solo prompt
            combined_prompt = (
                "El siguiente código generó un error:\n\n"
                f"{source_code}\n\n"
                "Error:\n\n"
                f"{exception_trace}\n\n"
                "Proporciona una explicación clara y posible solución para este error."
            )
            ai_response = send_exception_to_openrouter(combined_prompt)
            if ai_response:
                print(f"\n🤖 [Respuesta de OpenRouter.ai]:\n{ai_response}\n")
            # Opcional: re-lanzar la excepción si se desea
            # raise e
    return wrapper


def class_exception_handler(cls):
    """
    Decorador de clase. Recorre los atributos de la clase y envuelve:
    - Los métodos de clase (classmethod) usando su función interna.
    - Los métodos de instancia y métodos normales.
    Se salvan los métodos "dunder" (como __init__, __str__, etc.)
    para no alterar el comportamiento interno.
    """
    for name, attr in list(vars(cls).items()):
        if isinstance(attr, classmethod):
            original_func = attr.__func__
            wrapped_func = exception_handler(original_func)
            setattr(cls, name, classmethod(wrapped_func))
        elif callable(attr) and not name.startswith("__"):
            setattr(cls, name, exception_handler(attr))
    return cls
