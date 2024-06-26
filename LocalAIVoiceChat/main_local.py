if __name__ == '__main__':
    from RealtimeTTS import TextToAudioStream, SystemEngine
    from RealtimeSTT import AudioToTextRecorder
    import llama_cpp
    import json
    import os
    import logging
    
    logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%Y%m%d %H%M%S')

    output = ""
    Llama = llama_cpp.Llama
    history = []

    def replace_placeholders(params, char, user, scenario):
        for key in params:
            if isinstance(params[key], str):
                params[key] = params[key].replace("{char}", char)
                params[key] = params[key].replace("{user}", user)
                params[key] = params[key].replace("{scenario}", scenario)
        return params

    def write_file(filename, content):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

    def clear_console():
        os.system('clear' if os.name == 'posix' else 'cls')

    def encode(string):
        return model.tokenize(string.encode() if isinstance(string, str) else string)

    def count_tokens(string):
        return len(encode(string))

    def create_prompt():
        prompt = f'<|system|>\n{chat_params["system_prompt"]}</s>\n'
        if chat_params["initial_message"]:
            prompt += f"<|assistant|>\n{chat_params['initial_message']}</s>\n"
        return prompt + "".join(history) + "<|assistant|>"

    def generate():
        global output
        output = ""
        prompt = create_prompt()
        write_file('last_prompt.txt', prompt)
        completion_params['prompt'] = prompt
        first_chunk = True
        for completion_chunk in model.create_completion(**completion_params):
            text = completion_chunk['choices'][0]['text']
            if first_chunk and text.isspace():
                continue
            first_chunk = False
            output += text
            yield text

    with open('creation_params.json') as f:
        creation_params = json.load(f)
    with open('completion_params.json') as f:
        completion_params = json.load(f)
    with open('chat_params.json') as f:
        chat_params = json.load(f)
    
    chat_params = replace_placeholders(chat_params, chat_params["char"], chat_params["user"], chat_params["scenario"])

    if not completion_params['logits_processor']:
        completion_params['logits_processor'] = None


    print("Initializing LLM llama.cpp model ...")
    model = Llama(**creation_params)
    print("llama.cpp model initialized")

    print("Initializing TTS CoquiEngine ...")
    engine = SystemEngine(voice="Irina")

    print("Initializing STT AudioToTextRecorder ...")
    stream = TextToAudioStream(engine)
    recorder = AudioToTextRecorder(model="large", spinner=False)

    print(f'Scenario: {chat_params["scenario"]}\n\n')

    while True:
        print(f'>>> {chat_params["user"]}: ', end="", flush=True)
        print(f'{(user_text := recorder.text())}\n<<< {chat_params["char"]}: ', end="", flush=True)
        history.append(f"<|user|>\n{user_text}</s>\n")

        tokens_history = count_tokens(create_prompt())
        while tokens_history > 8192 - 500:
            history.pop(0)
            history.pop(0)
            tokens_history = count_tokens(create_prompt())

        generator = generate()
        stream.feed(generator)
        stream.play(fast_sentence_fragment=True, buffer_threshold_seconds=999, minimum_sentence_length=18, log_synthesized_text=True)
        history.append(f"<|assistant|>\n{output}</s>\n")
        write_file('last_prompt.txt', create_prompt())