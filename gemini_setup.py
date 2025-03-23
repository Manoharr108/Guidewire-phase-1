import google.generativeai as genai

# Set your API key
genai.configure(api_key="your_api_key")

available_models = genai.list_models()

print("Available models:")
for model in available_models:
    print(model.name)
