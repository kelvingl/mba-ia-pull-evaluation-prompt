# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

### Stack utilizada
- Python 3.13
- LangSmith
- OpenAI (GPT-4o e GPT-4o-mini)

### Ajustes no script [./src/evaluate.py](./src/evaluate.py)

O script de avaliação foi configurado para gerar experiments no LangSmith, usando o "experiment_prefix" no evaluate() para organizar os resultados por prompt avaliado.


## Técnicas aplicadas

### 1. Role prompting
O que é: Role prompting é uma técnica onde o modelo é instruído a assumir um papel específico para fornecer respostas mais relevantes e contextuais. Por exemplo, pedir ao modelo para agir como um especialista em um determinado assunto pode melhorar a qualidade das respostas.

Por que escolhi: Um product manager especializado em análise de bugs tem uma perspectiva única sobre como transformar um bug em uma user story. Ao pedir ao modelo para assumir esse papel, podemos obter insights mais alinhados com as necessidades do produto e dos usuários.

Como apliquei: No início do prompt, instruí o modelo a agir como um product manager especializado em análise de bugs. Isso ajudou a direcionar as respostas para serem mais relevantes e focadas na transformação do bug em uma user story.

### 2. Few-shot learning
O que é: Few-shot learning é uma técnica onde o modelo é fornecido com alguns exemplos de entrada e saída para aprender a tarefa desejada. Isso ajuda o modelo a entender melhor o formato e o tipo de resposta esperada.

Por que escolhi: Fornecer exemplos específicos de como transformar um bug em uma user story pode ajudar o modelo a entender melhor a tarefa e a gerar respostas mais precisas e relevantes.

Como apliquei: Incluí exemplos de bugs e suas respectivas user stories no prompt. Isso ajudou o modelo a aprender a estrutura e o formato desejados para as respostas.

### 3. Chain of Thought
O que é: Chain of Thought é uma técnica onde o modelo é incentivado a pensar passo a passo para chegar a uma resposta. Isso pode ajudar a melhorar a qualidade das respostas, especialmente para tarefas complexas.

Por que escolhi: Transformar um bug em uma user story pode ser um processo complexo que envolve várias etapas. Ao incentivar o modelo a pensar passo a passo, podemos obter respostas mais detalhadas e bem estruturadas, além de ajudar a não perder detalhes importantes.

Como apliquei: No prompt, instrui um processo explícito com etapas para cada parte necessária.

### 4. Skeleton of Thought
O que é: Skeleton of Thought é uma técnica onde o modelo recebe um "esqueleto" ou template pré-definido da estrutura de resposta esperada. Em vez de gerar a resposta livremente, o modelo preenche seções pré-estabelecidas, garantindo completude e consistência na saída.

Por que escolhi: Bugs variam muito em complexidade, e uma user story para um bug simples não precisa das mesmas seções que uma para um conjunto de falhas críticas. Fornecer esqueletos distintos por nível de complexidade garante que o modelo produza exatamente as seções necessárias, sem omitir partes importantes nem gerar informações desnecessárias.

Como apliquei: Defini três esqueletos de resposta, um por nível de complexidade classificado internamente pelo modelo:
- **SIMPLES**: esqueleto com user story no formato "Como / eu quero / para que" + bloco de critérios de aceitação (Dado / Quando / Então / E).
- **MÉDIO**: esqueleto com user story + critérios de aceitação + seção extra nomeada conforme o contexto do bug (ex.: "Critérios Técnicos", "Critérios de Segurança", "Exemplo de Cálculo") + "Contexto do Bug / Técnico / de Segurança".
- **COMPLEXO**: esqueleto com seções delimitadas por `=== NOME DA SEÇÃO ===` cobrindo user story principal, critérios de aceitação por categoria (A., B., C…), critérios técnicos, contexto do bug e tasks técnicas sugeridas.

Cada esqueleto foi acompanhado de um ou mais exemplos concretos (few-shot) para que o modelo internalize tanto a estrutura quanto o nível de detalhe esperado para cada complexidade.


## Output

Mais detalhes no [output.md](output.md) | [Link para o experimento no LangSmith](https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2)

### Modelo escolhido

Foi  utilizado o gemini para respostas e avaliação. Ele se mostrou consistentemente melhor que o gpt-4o-mini, especialmente na métrica de Correctness, que é crucial para a qualidade das user stories geradas. O gpt-4o-mini apresentou uma média geral de 0.87, enquanto o gemini alcançou 0.95, garantindo que as user stories fossem não apenas úteis, mas também corretas e alinhadas com os relatos de bugs.

### Resultados da Avaliação

Prompt avaliado: `bug_to_user_story_v2` | Modelo: `gemini-2.5-flash` | Dataset: 15 exemplos

| Experimento | Helpfulness | Correctness | F1-Score | Clarity | Precision | Média Geral | Status |
|---|---|---|---|---|---|---|---|
| [0fba3539](https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2/compare?selectedSessions=6a8bf551-a9ef-4f58-98a0-230a970b406a) | 0.97 ✓ | 0.93 ✓ | 0.90 ✓ | 0.97 ✓ | 0.97 ✓ | **0.9467** | ✅ APROVADO |
| [eb020ba6](https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2/compare?selectedSessions=9bda0d04-d07c-4445-9ae8-eadfb7297b3c) | 0.97 ✓ | 0.94 ✓ | 0.94 ✓ | 0.98 ✓ | 0.96 ✓ | **0.9586** | ✅ APROVADO |
| [78bb07d9](https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2/compare?selectedSessions=6d1c4997-634f-4bf6-8ccd-6be629629a30) | 0.96 ✓ | 0.91 ✓ | 0.88 ✗ | 0.96 ✓ | 0.95 ✓ | **0.9316** | ✅ APROVADO |

### Melhorias feitas no prompt

O prompt v1 era intencionalmente deficiente. A tabela abaixo resume os problemas identificados e como cada um foi corrigido no v2:

| Problema no v1 | Solução no v2 |
|---|---|
| Persona genérica: "Você é um assistente" | Role prompting: "Product Manager sênior com experiência em QA" |
| `{bug_report}` duplicado no `system_prompt` e no `user_prompt` | `{bug_report}` presente apenas no `user_prompt`, eliminando repetição e contexto desnecessário no system |
| Instrução vaga: "crie uma user story" sem restrição de formato | Três esqueletos de saída distintos (SIMPLES / MÉDIO / COMPLEXO) com estrutura pré-definida |
| Zero exemplos — modelo sem referência de saída esperada | 8 exemplos few-shot cobrindo todos os níveis de complexidade e variações de persona |
| Sem critérios de aceitação — saída livre e inconsistente | Critérios obrigatórios no formato `Dado que / Quando / Então / E` |
| Sem regra de persona — modelo misturava "usuário" e "sistema" arbitrariamente | Regra explícita: "Como o sistema" apenas para atores internos; "Como um [usuário]" nos demais casos |
| Sem instrução de preservação de detalhes técnicos | Regra 3: preservar endpoints, z-index, queries, logs, valores, SLAs etc. |
| Sem regra de idioma ou formato de saída | Regra 1: responder somente em português, usando Markdown |
| Sem controle de alucinação — modelo podia inventar dados ausentes | Regra 2: usar colchetes `[dado]` para informações que precisam ser investigadas |
| Sem controle do início da resposta — modelo adicionava preâmbulos | Regra crítica: resposta DEVE começar diretamente com a palavra "Como" |


## Como executar

### Pré-requisitos

- Python 3.13+
- Conta no [LangSmith](https://smith.langchain.com) com API key
- Chave de API do Google Gemini **ou** OpenAI

### 1. Instalar dependências

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Configurar variáveis de ambiente

```bash
cp .env.example .env
```

Edite o `.env` com suas credenciais:

| Variável | Descrição |
|---|---|
| `LANGSMITH_API_KEY` | Chave de API do LangSmith |
| `USERNAME_LANGSMITH_HUB` | Seu username no LangSmith Hub |
| `LANGSMITH_PROJECT` | Nome do projeto no LangSmith |
| `GOOGLE_API_KEY` | Chave da API do Google Gemini (se `LLM_PROVIDER=google`) |
| `OPENAI_API_KEY` | Chave da API da OpenAI (se `LLM_PROVIDER=openai`) |
| `LLM_PROVIDER` | `google` ou `openai` |
| `LLM_MODEL` | Modelo principal (ex: `gemini-2.5-flash` ou `gpt-4o-mini`) |
| `EVAL_MODEL` | Modelo de avaliação (ex: `gemini-2.5-flash` ou `gpt-4o`) |

> **Dica:** para descobrir seu `USERNAME_LANGSMITH_HUB`, publique qualquer prompt no LangSmith Hub, abra-o e clique no ícone de cadeado (🔒).

### 3. Executar o fluxo completo

```bash
# Passo 1 — baixar o prompt v1 do LangSmith Hub
python src/pull_prompts.py

# Passo 2 — editar o prompt otimizado
# Edite o arquivo prompts/bug_to_user_story_v2.yml com suas melhorias

# Passo 3 — publicar o prompt v2 no LangSmith Hub
python src/push_prompts.py

# Passo 4 — avaliar o prompt (requer push prévio)
python src/evaluate.py
```

### 4. Executar os testes

```bash
pytest tests/test_prompts.py
pytest tests/test_prompts.py -v --tb=short  # saída detalhada
```

