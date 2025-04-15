import requests


class Auth:
    """Classe para autenticação."""

    def __init__(self, base_url):
        """
        Inicializa a classe Auth com a URL base.

        Args:
            base_url (str): URL base para autenticação.
        """
        self._base_url = base_url
