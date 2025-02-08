from contextlib import contextmanager
import contextvars

url_context = contextvars.ContextVar("url_context", default="?")
product_context = contextvars.ContextVar("product", default="?")

@contextmanager
def context_set(context_variable: contextvars.ContextVar, value):
    token = context_variable.set(value)
    try:
        yield
    finally:
        context_variable.reset(token)

def info(s: str) -> None:
    url = url_context.get()
    product = product_context.get()
    print(f"[{product}] {s} {url}")
