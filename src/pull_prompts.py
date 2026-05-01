"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()

REMOTE_PROMPT = "leonanluppi/bug_to_user_story_v1"
LOCAL_OUTPUT = Path("prompts/raw_prompts.yml")


def pull_prompts_from_langsmith():
    """Faz pull dos prompts do LangSmith Hub e retorna os dados formatados."""
    if not check_env_vars(["LANGCHAIN_HUB_API_KEY"]):
        print("❌ Missing required environment variables. Please check your .env file.")
        return

    try:
        # Pull do prompt do Hub
        prompt = hub.pull(REMOTE_PROMPT)
        print(f"✓ Prompt '{REMOTE_PROMPT}' pulled successfully from LangSmith Hub.")

        return prompt

    except Exception as e:
        print(f"❌ Error pulling prompt from LangSmith Hub: {e}")
        return None


def main():
    """Função principal"""
    data = pull_prompts_from_langsmith()

    if data is None:
        print("❌ Failed to pull prompts from LangSmith Hub.")
        return

    LOCAL_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    if save_yaml(data.to_json(), LOCAL_OUTPUT):
        print(f"✓ Prompt saved to: {LOCAL_OUTPUT}")
    else:
        print("❌ Failed to save prompt locally.")


if __name__ == "__main__":
    sys.exit(main())
