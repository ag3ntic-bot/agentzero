"""Entry point for AgentZero."""

from agentzero.agent import run_conversation
from agentzero.config import get_model_info


def main() -> None:
    """Main entry point."""
    info = get_model_info()
    print(f"Model: {info['model_name']} ({info['model_id']})")
    print(f"Provider: {info['provider']}")
    print(f"Context window: {info['context_window']:,} tokens")
    print(f"Pricing: ${info['pricing']['input_per_million']}/M input, "
          f"${info['pricing']['output_per_million']}/M output")
    print("-" * 50)
    run_conversation()


if __name__ == "__main__":
    main()
