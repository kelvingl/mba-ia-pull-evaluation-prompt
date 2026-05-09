(mba-ia-pull-evaluation-prompt) PS C:\Users\kelvin\Desktop\repos\mba-ia-pull-evaluation-prompt> python .\src\evaluate.py

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: google
Modelo Principal: gemini-2.5-flash
Modelo de Avaliação: gemini-2.5-flash

Criando dataset de avaliação: prompt-optimization-challenge-resolved-eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset criado com 15 exemplos

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Iniciando experimento para: bug_to_user_story_v2
   Puxando prompt do LangSmith Hub: bug_to_user_story_v2
   ✓ Prompt carregado com sucesso
C:\Users\kelvin\Desktop\repos\mba-ia-pull-evaluation-prompt\.venv\Lib\site-packages\langchain_google_genai\chat_models.py:47: FutureWarning: 

All support for the `google.generativeai` package has ended. It will no longer be receiving 
updates or bug fixes. Please switch to the `google.genai` package as soon as possible.
See README for more details:

https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md

  from google.generativeai.caching import CachedContent  # type: ignore[import]
   Executando evaluate() contra dataset 'prompt-optimization-challenge-resolved-eval'...
   Os resultados serão publicados como Experiment no LangSmith.

View the evaluation results for experiment: 'bug_to_user_story_v2-0fba3539' at:
https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2/compare?selectedSessions=6a8bf551-a9ef-4f58-98a0-230a970b406a


15it [18:36, 74.44s/it]

==================================================
Prompt: bug_to_user_story_v2
==================================================

Métricas LangSmith:
  - Helpfulness: 0.97 ✓
  - Correctness: 0.93 ✓

Métricas Customizadas:
  - F1-Score: 0.90 ✓
  - Clarity: 0.97 ✓
  - Precision: 0.97 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.9467
--------------------------------------------------

✅ STATUS: APROVADO (média >= 0.9)

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 1
Reprovados: 0

✅ Todos os prompts atingiram média >= 0.9!

✓ Confira os resultados (tabela de métricas) em:
  https://smith.langchain.com/o/default/datasets/prompt-optimization-challenge-resolved-eval

✓ Ou acesse o projeto:
  https://smith.langchain.com/projects/prompt-optimization-challenge-resolved

Próximos passos:
1. Documente o processo no README.md
2. Capture screenshots das avaliações
3. Faça commit e push para o GitHub
(mba-ia-pull-evaluation-prompt) PS C:\Users\kelvin\Desktop\repos\mba-ia-pull-evaluation-prompt> ^C
(mba-ia-pull-evaluation-prompt) PS C:\Users\kelvin\Desktop\repos\mba-ia-pull-evaluation-prompt> python .\src\evaluate.py

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: google
Modelo Principal: gemini-2.5-flash
Modelo de Avaliação: gemini-2.5-flash

Criando dataset de avaliação: prompt-optimization-challenge-resolved-eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset 'prompt-optimization-challenge-resolved-eval' já existe, usando existente

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Iniciando experimento para: bug_to_user_story_v2
   Puxando prompt do LangSmith Hub: bug_to_user_story_v2
   ✓ Prompt carregado com sucesso
C:\Users\kelvin\Desktop\repos\mba-ia-pull-evaluation-prompt\.venv\Lib\site-packages\langchain_google_genai\chat_models.py:47: FutureWarning: 

All support for the `google.generativeai` package has ended. It will no longer be receiving 
updates or bug fixes. Please switch to the `google.genai` package as soon as possible.
See README for more details:

https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md

  from google.generativeai.caching import CachedContent  # type: ignore[import]
   Executando evaluate() contra dataset 'prompt-optimization-challenge-resolved-eval'...
   Os resultados serão publicados como Experiment no LangSmith.

View the evaluation results for experiment: 'bug_to_user_story_v2-eb020ba6' at:
https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2/compare?selectedSessions=9bda0d04-d07c-4445-9ae8-eadfb7297b3c


15it [17:24, 69.64s/it]

==================================================
Prompt: bug_to_user_story_v2
==================================================

Métricas LangSmith:
  - Helpfulness: 0.97 ✓
  - Correctness: 0.94 ✓

Métricas Customizadas:
  - F1-Score: 0.94 ✓
  - Clarity: 0.98 ✓
  - Precision: 0.96 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.9586
--------------------------------------------------

✅ STATUS: APROVADO (média >= 0.9)

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 1
Reprovados: 0

✅ Todos os prompts atingiram média >= 0.9!

✓ Confira os resultados (tabela de métricas) em:
  https://smith.langchain.com/o/default/datasets/prompt-optimization-challenge-resolved-eval

✓ Ou acesse o projeto:
  https://smith.langchain.com/projects/prompt-optimization-challenge-resolved

Próximos passos:
1. Documente o processo no README.md
2. Capture screenshots das avaliações
3. Faça commit e push para o GitHub
(mba-ia-pull-evaluation-prompt) PS C:\Users\kelvin\Desktop\repos\mba-ia-pull-evaluation-prompt> python .\src\evaluate.py

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: google
Modelo Principal: gemini-2.5-flash
Modelo de Avaliação: gemini-2.5-flash

Criando dataset de avaliação: prompt-optimization-challenge-resolved-eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset 'prompt-optimization-challenge-resolved-eval' já existe, usando existente

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Iniciando experimento para: bug_to_user_story_v2
   Puxando prompt do LangSmith Hub: bug_to_user_story_v2
   ✓ Prompt carregado com sucesso
C:\Users\kelvin\Desktop\repos\mba-ia-pull-evaluation-prompt\.venv\Lib\site-packages\langchain_google_genai\chat_models.py:47: FutureWarning: 

All support for the `google.generativeai` package has ended. It will no longer be receiving 
updates or bug fixes. Please switch to the `google.genai` package as soon as possible.
See README for more details:

https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md

  from google.generativeai.caching import CachedContent  # type: ignore[import]
   Executando evaluate() contra dataset 'prompt-optimization-challenge-resolved-eval'...
   Os resultados serão publicados como Experiment no LangSmith.

View the evaluation results for experiment: 'bug_to_user_story_v2-78bb07d9' at:
https://smith.langchain.com/o/d7e45f27-2f0f-4d97-900a-27bb81492af9/datasets/ae942558-c4ae-46f1-860f-dc698a9f37d2/compare?selectedSessions=6d1c4997-634f-4bf6-8ccd-6be629629a30


15it [18:30, 74.02s/it]

==================================================
Prompt: bug_to_user_story_v2
==================================================

Métricas LangSmith:
  - Helpfulness: 0.96 ✓
  - Correctness: 0.91 ✓

Métricas Customizadas:
  - F1-Score: 0.88 ✗
  - Clarity: 0.96 ✓
  - Precision: 0.95 ✓

--------------------------------------------------
📊 MÉDIA GERAL: 0.9316
--------------------------------------------------

✅ STATUS: APROVADO (média >= 0.9)

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 1
Reprovados: 0

✅ Todos os prompts atingiram média >= 0.9!

✓ Confira os resultados (tabela de métricas) em:
  https://smith.langchain.com/o/default/datasets/prompt-optimization-challenge-resolved-eval

✓ Ou acesse o projeto:
  https://smith.langchain.com/projects/prompt-optimization-challenge-resolved

Próximos passos:
1. Documente o processo no README.md
2. Capture screenshots das avaliações
3. Faça commit e push para o GitHub