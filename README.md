# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

### Stack utilizada
- Python 3.13
- LangSmith
- OpenAI (GPT-4o e GPT-4o-mini)

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

### Resultados da Avaliação

Prompt avaliado: `bug_to_user_story_v2` | Modelo: `gemini-2.5-flash` | Dataset: 15 exemplos

| Experimento | Helpfulness | Correctness | F1-Score | Clarity | Precision | Média Geral | Status |
|---|---|---|---|---|---|---|---|
| [0fba3539](https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2/compare?selectedSessions=6a8bf551-a9ef-4f58-98a0-230a970b406a) | 0.97 ✓ | 0.93 ✓ | 0.90 ✓ | 0.97 ✓ | 0.97 ✓ | **0.9467** | ✅ APROVADO |
| [eb020ba6](https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2/compare?selectedSessions=9bda0d04-d07c-4445-9ae8-eadfb7297b3c) | 0.97 ✓ | 0.94 ✓ | 0.94 ✓ | 0.98 ✓ | 0.96 ✓ | **0.9586** | ✅ APROVADO |
| [78bb07d9](https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2/compare?selectedSessions=6d1c4997-634f-4bf6-8ccd-6be629629a30) | 0.96 ✓ | 0.91 ✓ | 0.88 ✗ | 0.96 ✓ | 0.95 ✓ | **0.9316** | ✅ APROVADO |


