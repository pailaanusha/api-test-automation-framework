# ============================================================
# LLM-BASED TEST GENERATOR
# ------------------------------------------------------------
# Reads Swagger/OpenAPI specification
# Uses Gemini LLM to generate intelligent API test scenarios
# ============================================================

import google.generativeai as genai # Reverted import to google.generativeai
import json
import os


# ------------------------------------------------------------
# Configure Gemini API Key
# Using genai.configure() with google.generativeai
# ------------------------------------------------------------
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ------------------------------------------------------------
# Initialize Gemini Model
# ------------------------------------------------------------
model = genai.GenerativeModel("gemini-flash-latest") # API key set via configure()

# ------------------------------------------------------------
# Generate API Test Cases Dynamically
# ------------------------------------------------------------
def generate_test_cases(api_specification):

    prompt = f"""
    You are an expert API Automation Engineer.

    Generate realistic API test cases in JSON array format.

    Cover:

    1. Positive scenarios
    2. Negative scenarios
    3. Boundary validations
    4. Missing mandatory fields
    5. Invalid datatypes
    6. Invalid headers
    7. Performance scenarios
    8. Response schema validations
    9. Business rule validations

    Include:
    - test_name
    - method
    - endpoint
    - headers
    - query_params
    - body
    - expected_status_code

    API Specification:
    {json.dumps(api_specification, indent=2)}

    Output ONLY JSON array.
    """

    response = model.generate_content(prompt)

    generated_text = response.text.strip()

    # --------------------------------------------------------
    # Remove markdown formatting if generated
    # --------------------------------------------------------
    generated_text = generated_text.replace("```json", "")
    generated_text = generated_text.replace("```", "")

    return json.loads(generated_text)






