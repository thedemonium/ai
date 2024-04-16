import json
import os
import logging
import requests
from RealtimeTTS import TextToAudioStream, SystemEngine
from RealtimeSTT import AudioToTextRecorder

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y%m%d %H%M%S')

history = []
model = 'zephyr-7b-beta.Q5_K_M'  
context = []  

OLLAMA_API_URL = "http://100.107.132.195:11434/api/generate"
CREATION_PARAMS_FILE = 'creation_params.json'
COMPLETION_PARAMS_FILE = 'completion_params.json'
CHAT_PARAMS_FILE = 'chat_params.json'

def call_ollama_api(prompt, context):
    payload = {
        'model': model,
        'prompt': prompt,
        'context': context,
        'stream': True  
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
        response.raise_for_status()
        logging.debug(f"API Response: {response.text}")
        for line in response.iter_lines():
            if line:  
                yield json.loads(line)
    except requests.exceptions.RequestException as e:
        logging.error(f"RequestException occurred: {e}")
        raise

def replace_placeholders(params, char, user, scenario):
    new_params = {}
    for key, value in params.items():
        if isinstance(value, str):
            new_params[key] = value.format(char=char, user=user, scenario=scenario)
        else:
            new_params[key] = value
    return new_params

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def create_prompt(chat_params):
    prompt = f'<|system|>\n{chat_params["system_prompt"]}</s>\n'
    if chat_params["initial_message"]:
        prompt += f"<|assistant|>\n{chat_params['initial_message']}</s>\n"
    return prompt + "".join(history) + "<|assistant|>"


def generate(user_input, context, chat_params):
    prompt = create_prompt(chat_params) + user_input
    write_file('last_prompt.txt', prompt)
    for completion in call_ollama_api(prompt, context):
        response_part = completion.get('response', '')
        print(response_part, end='', flush=True)
        yield response_part

def load_params():
    with open(CREATION_PARAMS_FILE) as f:
        creation_params = json.load(f)
    with open(COMPLETION_PARAMS_FILE) as f:
        completion_params = json.load(f)
    with open(CHAT_PARAMS_FILE) as f:
        chat_params = json.load(f)
    return creation_params, completion_params, chat_params

def initialize_tts_stt(chat_params):
    print("Initializing TTS CoquiEngine ...")
    engine = SystemEngine(voice="xtts_v2")
    print("Initializing STT AudioToTextRecorder ...")
    stream = TextToAudioStream(engine)
    recorder = AudioToTextRecorder(model="large", spinner=False)
    print(f'Scenario: {chat_params["scenario"]}\n\n')
    return engine, stream, recorder

def main():
    creation_params, completion_params, chat_params = load_params()
    chat_params = replace_placeholders(chat_params, chat_params["char"], chat_params["user"], chat_params["scenario"])
    if not completion_params.get('logits_processor'):
        completion_params['logits_processor'] = None

    engine, stream, recorder = initialize_tts_stt(chat_params)

    while True:
        print(f'>>> {chat_params["user"]}: ', end="", flush=True)
        user_text = recorder.text()
        print(f'{user_text}\n<<< {chat_params["char"]}: ', end="", flush=True)
        history.append(f"<|user|>\n{user_text}</s>\n")
        for text_chunk in generate(user_input=user_text, context=context, chat_params=chat_params):
            stream.feed(text_chunk)  
            context.append(f"<|assistant|>\n{text_chunk}</s>\n")
        stream.play()        
        context.append(f"<|user|>\n{user_text}</s>\n")

if __name__ == '__main__':
    main()