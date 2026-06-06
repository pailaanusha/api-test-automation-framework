import os

# List of directories that need to be recognized as Python packages
package_dirs = [
    "tests",
    "utils",
    "data"
]

# Create an empty __init__.py in each package directory
for directory in package_dirs:
    init_file_path = os.path.join(directory, "__init__.py")
    if not os.path.exists(init_file_path):
        with open(init_file_path, "w") as f:
            f.write("")
        print(f"Created {init_file_path}")
    else:
        print(f"{init_file_path} already exists")

# Original content for api_client.py (kept for completeness as it was in the original cell)
api_client_content = '''
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
'''

# Write api_client.py as before
with open("utils/api_client.py", "w") as f:
    f.write(api_client_content)

print("api_client.py created")
