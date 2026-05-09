"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

load_dotenv()


def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    try:
        system_prompt = prompt_data.get("system_prompt", "")
        user_prompt = prompt_data.get("user_prompt", "")

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", user_prompt)
        ])

        username = os.getenv("USERNAME_LANGSMITH_HUB", "")
        full_prompt_name = f"{username}/{prompt_name}"

        print(f"🚀 Pushing prompt '{full_prompt_name}' to LangSmith Hub...")

        hub.push(full_prompt_name, prompt_template, new_repo_is_public=True)

        print(f"✓ Prompt '{full_prompt_name}' pushed successfully!")

        return True
    except Exception as e:
        print(f"❌ Error pushing prompt to LangSmith Hub: {e}")
        return False


def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    errors = []

    required_fields = ["description", "system_prompt", "version"]
    for field in required_fields:
        if field not in prompt_data:
            errors.append(f"Campo obrigatório faltando: {field}")

    system_prompt = prompt_data.get("system_prompt", "").strip()
    if not system_prompt:
        errors.append("system_prompt está vazio")

    if "[TODO]" in system_prompt:
        errors.append("system_prompt ainda contém TODOs")

    techniques = prompt_data.get("techniques_applied", [])
    if len(techniques) < 2:
        errors.append(f"Mínimo de 2 técnicas requeridas, encontradas: {len(techniques)}")

    return (len(errors) == 0, errors)


def main():
    """Função principal"""
    if not check_env_vars(["LANGSMITH_API_KEY", "USERNAME_LANGSMITH_HUB"]):
        return 1

    prompt_key = "bug_to_user_story_v2"

    yaml_path = f"prompts/{prompt_key}.yml"
    data = load_yaml(yaml_path)
    if not data:
        return 1

    prompt_data = data.get(prompt_key, {})
    if not prompt_data:
        print(f"❌ Prompt '{prompt_key}' not found in YAML file.")
        return 1

    is_valid, errors = validate_prompt(prompt_data)
    if not is_valid:
        print(f"❌ Prompt '{prompt_key}' with errors:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"✓ Prompt '{prompt_key}' passed validation with no errors.")

    if not push_prompt_to_langsmith(prompt_key, prompt_data):
        return 1

    print(f"🎉 Prompt '{prompt_key}' successfully pushed to LangSmith Hub!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
