# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## The challenge

Read [the challenge](./challenge.md) to understand the target output.

## Project Overview
This is an MBA course challenge project for learning prompt engineering. The goal is to:
1. Pull a low-quality prompt from LangSmith Hub
2. Optimize it using advanced prompt engineering techniques
3. Push the optimized prompt back to LangSmith
4. Evaluate the prompt and achieve >= 0.9 on all 5 metrics (Helpfulness, Correctness, F1-Score, Clarity, Precision)

## Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Then fill in your API keys
```

Required `.env` variables:
- `LANGSMITH_API_KEY` and `USERNAME_LANGSMITH_HUB` — always required
- `OPENAI_API_KEY` (if `LLM_PROVIDER=openai`) or `GOOGLE_API_KEY` (if `LLM_PROVIDER=google`)
- `LLM_MODEL`, `EVAL_MODEL`, `LANGSMITH_PROJECT`

## Commands

```bash
# Pull base prompt from LangSmith Hub
python src/pull_prompts.py

# Push optimized prompt to LangSmith Hub
python src/push_prompts.py

# Run evaluation (requires prior push)
python src/evaluate.py

# Run tests
pytest tests/test_prompts.py
pytest tests/test_prompts.py -v --tb=short  # verbose
```

## Architecture

All scripts run from the project root. `src/` is not a package with installed paths — scripts in `src/` import each other directly (e.g., `from utils import ...`), so run them with `python src/<script>.py` from the project root, not from inside `src/`.

### Data flow

```
LangSmith Hub
    ↓ pull_prompts.py
prompts/bug_to_user_story_v1.yml  (low-quality, do not edit)
    ↓ (manual optimization)
prompts/bug_to_user_story_v2.yml  (your optimized version)
    ↓ push_prompts.py
LangSmith Hub ({username}/bug_to_user_story_v2)
    ↓ evaluate.py
datasets/bug_to_user_story.jsonl → LangSmith dataset → metrics
```

### Key modules

- **`src/utils.py`** — shared helpers: `get_llm()` (responder LLM), `get_eval_llm()` (evaluator LLM), `load_yaml()`, `save_yaml()`, `validate_prompt_structure()`. LLM provider is selected by `LLM_PROVIDER` env var (`openai` or `google`).
- **`src/metrics.py`** — LLM-as-Judge evaluators: `evaluate_f1_score()`, `evaluate_clarity()`, `evaluate_precision()`. All call `get_eval_llm()` using `EVAL_MODEL`.
- **`src/evaluate.py`** — orchestrates: creates LangSmith dataset from JSONL, pulls prompt from Hub, runs each of the 15 examples through the prompt, scores with metrics. **Do not modify.**
- **`src/pull_prompts.py`** / **`src/push_prompts.py`** — skeleton functions to implement.

### Metric derivation

`evaluate.py` computes only 3 base metrics per example (F1, Clarity, Precision), then derives:
- `Helpfulness = (Clarity + Precision) / 2`
- `Correctness = (F1 + Precision) / 2`

Approval requires all 5 >= 0.9.

## Prompt YAML structure

`prompts/bug_to_user_story_v2.yml` must have:
```yaml
bug_to_user_story_v2:
  description: "..."
  system_prompt: |
    ...
  user_prompt: "{bug_report}"
  version: "v2"
  techniques_applied: ["Few-shot Learning", "Chain of Thought"]  # min 2
  tags: [...]
```

The `{bug_report}` variable is the only input variable — it maps to `inputs.question` or `inputs.bug_report` in the dataset. The evaluator tests for: non-empty `system_prompt`, role definition (persona), format mention (Markdown/User Story), few-shot examples, no `[TODO]` strings, and `techniques_applied` with >= 2 entries.

## What to implement

- `src/pull_prompts.py` — implement `pull_prompts_from_langsmith()` and `main()`: use `hub.pull("leonanluppi/bug_to_user_story_v1")` and save to `prompts/bug_to_user_story_v1.yml`
- `src/push_prompts.py` — implement `push_prompt_to_langsmith()`, `validate_prompt()`, and `main()`: load v2 YAML, build `ChatPromptTemplate`, call `hub.push("{username}/bug_to_user_story_v2", prompt, new_repo_is_public=True)`
- `tests/test_prompts.py` — implement 6 tests in `TestPrompts` loading `prompts/bug_to_user_story_v2.yml`
- `prompts/bug_to_user_story_v2.yml` — the optimized prompt (Few-shot required + at least 1 other technique)

## Files not to modify

`src/evaluate.py`, `src/metrics.py`, `src/utils.py`, `datasets/bug_to_user_story.jsonl`
