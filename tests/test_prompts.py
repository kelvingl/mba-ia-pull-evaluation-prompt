"""
Testes automatizados para validação de prompts.
"""
from utils import validate_prompt_structure
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


PROMPT_FILE = Path(__file__).parent.parent / "prompts" / "bug_to_user_story_v2.yml"


def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


class TestPrompts:
    @pytest.fixture(autouse=True)
    def setup(self):
        data = load_prompts(PROMPT_FILE)
        self.prompt = data["bug_to_user_story_v2"]
        self.system_prompt = self.prompt.get("system_prompt", "")

    def test_prompt_has_system_prompt(self):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        assert "system_prompt" in self.prompt, "Campo 'system_prompt' não encontrado no YAML"
        assert self.system_prompt.strip(), "system_prompt está vazio"

    def test_prompt_has_role_definition(self):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        role_indicators = ["você é", "you are", "act as", "aja como"]
        system_lower = self.system_prompt.lower()
        assert any(indicator in system_lower for indicator in role_indicators), (
            "system_prompt não define uma persona (ex: 'Você é um Product Manager')"
        )

    def test_prompt_mentions_format(self):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        format_indicators = ["markdown", "user story", "como um", "como o sistema"]
        system_lower = self.system_prompt.lower()
        assert any(indicator in system_lower for indicator in format_indicators), (
            "system_prompt não menciona formato de saída (Markdown ou User Story)"
        )

    def test_prompt_has_few_shot_examples(self):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        few_shot_indicators = ["exemplo", "entrada:", "saída:", "input:", "output:", "example"]
        system_lower = self.system_prompt.lower()
        assert any(indicator in system_lower for indicator in few_shot_indicators), (
            "system_prompt não contém exemplos few-shot (entrada/saída)"
        )

    def test_prompt_no_todos(self):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        full_text = yaml.dump(self.prompt, allow_unicode=True)
        assert "[TODO]" not in full_text, "Encontrado '[TODO]' no prompt — complete as seções pendentes"

    def test_minimum_techniques(self):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        techniques = self.prompt.get("techniques_applied", [])
        assert len(techniques) >= 2, (
            f"Mínimo de 2 técnicas requeridas, encontradas: {len(techniques)}"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
