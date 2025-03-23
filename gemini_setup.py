import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyCezzX-vgWa0ZQ8_gr5HrbVpP_CERW9hNQ")

available_models = genai.list_models()

print("Available models:")
for model in available_models:
    print(model.name)