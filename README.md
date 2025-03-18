# OpenRouter Exception Handler

A Python module distributed via pip that automatically handles exceptions using intelligent responses generated by [OpenRouter.ai](https://openrouter.ai/). It also sends the source code of the function where the exception occurred, which can help you debug issues more effectively.

## 🚀 Installation

```bash
pip install openrouter-exception-handler
```

## 📌 Features

- Automatically captures Python exceptions during execution.
- Sends exception details to OpenRouter.ai.
- **Sends the source code** of the function that triggered the exception.
- Displays intelligent responses from OpenRouter.ai directly in your stdout.
- Facilitates AI-assisted debugging, reducing the time needed for error diagnosis.
- **Optionally** decorates entire classes so all their methods automatically benefit from exception handling.

## 🔧 Quick Usage (Function-Level)

Simply decorate your functions with `@exception_handler`:

```python
from openrouter_exception_handler.exception_handler import exception_handler

@exception_handler
def divide(a, b):
    return a / b

divide(10, 0)  # Will trigger ZeroDivisionError and send the function's source code along with the error.
```

### Example Output

```
❌ Exception captured in 'divide': division by zero
Source code of the function:
def divide(a, b):
    return a / b

AI Response:
This exception occurs because you're trying to divide by zero.
Validate your inputs before performing division to prevent this error.
```

## 💡 Class-Level Usage

To automatically capture exceptions in **all methods** of a class (including `staticmethod` and `classmethod`), use `@class_exception_handler`:

```python
from openrouter_exception_handler.exception_handler import class_exception_handler

@class_exception_handler
class MyClass:
    def instance_method(self, x):
        return 10 / x  # Will raise ZeroDivisionError if x == 0

    @staticmethod
    def static_method(x):
        return 10 / x  # Same behavior

    @classmethod
    def class_method(cls, x):
        return 10 / x  # Same behavior

obj = MyClass()
obj.instance_method(0)   # Exception will be caught and the function's source code will be sent.
MyClass.static_method(0) # Same behavior
MyClass.class_method(0)  # Same behavior
```

> By default, dunder methods (like `__init__`, `__str__`, etc.) are not wrapped. If you want to handle those as well, adjust the class decorator code accordingly.

## 🔑 Configuration

Define your OpenRouter.ai API key in the environment variable `APIKEY_OPENROUTER`:

```bash
export APIKEY_OPENROUTER="your_api_key_here"
```

## 📦 Installation

Install easily using pip:

```bash
pip install openrouter-exception-handler
```

## 📌 Requirements

- Python >= 3.6
- requests

## 📄 License

MIT

---

### Here's a simple guide to create an API key on OpenRouter

1. **Sign Up or Log In**
   Go to [openrouter.ai](https://openrouter.ai/) and create an account, or log in if you already have one.

2. **Go to Your User/Developer Settings**
   Look for a section like *Developer Settings*, *API Keys*, or *Settings* in your account dashboard.

3. **Generate a New Key**
   - Click **Generate New Key** (or a similar button) to create your new API key.
   - Copy the generated API key. Note that for security reasons, you usually only get to see the key once.

4. **Save Your API Key**
   - Store it in a safe place (e.g., an environment variable or a password manager).
   - Avoid committing it directly to a public repository or version control.

> **Tip:** Once you have your API key, set it in your environment (e.g., `OPENROUTER_API_KEY`), so your application can access it securely without exposing it in the source code.