# ============================================================
# API CLIENT UTILITY
# ------------------------------------------------------------
# Responsible for executing HTTP requests dynamically
# ============================================================

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class APIClient:

    @staticmethod
    def send_request(test_case):

        # ----------------------------------------------------
        # Read test case data
        # ----------------------------------------------------
        method = test_case["method"]
        endpoint = test_case["endpoint"]

        headers = test_case.get("headers", {})
        query_params = test_case.get("query_params", {})
        body = test_case.get("body", {})

        # ----------------------------------------------------
        # Construct URL
        # ----------------------------------------------------
        url = f"{BASE_URL}{endpoint}"

        # ----------------------------------------------------
        # Execute Request
        # ----------------------------------------------------
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=query_params,
            json=body
        )

        return response
    