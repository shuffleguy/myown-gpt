# myown-gpt

## Interação de Chat usando OpenAI GPT-3.5

Este é um script Python simples que demonstra como interagir com o modelo de linguagem GPT-3.5 da OpenAI para realizar uma conversa de chat. Ele permite que você faça perguntas ao modelo e receba respostas relevantes.

### Requisitos

Antes de executar este script, certifique-se de ter instalado o pacote `openai` e ter uma chave de API válida para acesso à API da OpenAI. Você pode obter sua chave de API registrando-se no site da OpenAI.

### Como Usar

1. Clone este repositório ou baixe o arquivo `chat_gpt.py`.
2. Substitua `'SUA_CHAVE_DE_API_AQUI'` pela sua chave de API OpenAI na linha `openai.api_key = ''`.
3. Execute o script Python em um ambiente compatível.

### Funcionamento do Código

O código consiste em duas funções principais:

- `entrada()`: Esta função permite que o usuário faça perguntas ao modelo de chat. Ele continuará aceitando perguntas até que o usuário insira uma entrada em branco para sair do programa.

- `saida(perguntas)`: Esta função envia as perguntas feitas pelo usuário para a API da OpenAI e retorna a resposta gerada pelo modelo.

### Observações

- Certifique-se de usar a chave de API fornecida pela OpenAI de acordo com suas políticas e termos de serviço.
- Este script utiliza o modelo `gpt-3.5-turbo` da OpenAI para geração de texto. Você pode experimentar com outros modelos, mas pode precisar ajustar os parâmetros de acordo.

