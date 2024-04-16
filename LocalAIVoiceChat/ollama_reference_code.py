import json
import requests
import logging

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y%m%d %H%M%S')

model = 'zephyr-7b-beta.Q5_K_M'

def generate(prompt, context):
    r = requests.post('http://100.107.132.195:11434/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=True)
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        logging.debug(f"API Response: {response_part}")  
        print(response_part, end='', flush=True)

        if 'error' in body:
            error = body['error']
            print("\nError occurred:", error) 
            continue

        if body.get('done', False):
            context = body.get('context', [])  
            return context

def main():
    context = [] 
    while True:
        user_input = input("Enter a prompt: ").strip()
        if not user_input:
            exit()
        print()
        try:
            context = generate(user_input, context)
        except Exception as e:
            print("Error occurred:", str(e))
            continue
        print()

if __name__ == "__main__":
    main()