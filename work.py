import pathlib
import yaml
from langchain.memory import ConversationBufferWindowMemory
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate

base_path = pathlib.Path.cwd()

template = """
# introduction
- You are my exclusive professional advisor.
- Please output the best results based on the following constrains

# Constrains
- Your answer must be in Japanese.
- About 200 characters.
- No important keywords are left out.
- Keep the text concise.
- If you cannot provide the best information, let us know.

{history}
Human: {input}
Assistant:
"""

conf_file = base_path / 'config' / 'config.yaml'

def run():
    with open(conf_file, 'r') as inf:
        config = yaml.safe_load(inf)
    api_key = config['openai_api']['api_key']

    # メモリの初期化(kは、直近のやり取りを保存する数)
    memory = ConversationBufferWindowMemory(k=2)

    # LLM の初期化
    llm = OpenAI(
        temperature=0.2,
        openai_api_key=api_key,
        model_name='gpt-3.5-turbo',
        max_tokens=200
    )

    prompt = PromptTemplate(
        input_variables=['history', 'input'],
        template=template
    )

    # `ConversationChain` の初期化
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt
    )

    # 会話を開始
    user_input=input("You: ")

    while True:
        response = conversation.predict(input=user_input)
        print(f"AI: {response}")
        user_input = input("You: ")
        if user_input == "exit":
            break


if __name__ == '__main__':
    run()