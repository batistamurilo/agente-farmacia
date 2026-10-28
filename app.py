
from groq import Groq

cliente = Groq(api_key='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')

pergunta= input('faça uma pergunta')


resposta = cliente.chat.completions.create(
model='openai/gpt-oss-120b',
messages=
[
{'role':'system', 'content':'você é um atendente de clinica de psicologia'},
{'role':'user', 'content':pergunta}
]
)


print(resposta.choices[0].message.content)