"""Core agent implementation using Claude Opus 4.6."""

from anthropic import Anthropic

from agentzero.config import API_KEY, MAX_TOKENS, MODEL_ID

SYSTEM_PROMPT = (
    "You are AgentZero, a capable AI assistant. "
    "You answer questions clearly and help with tasks efficiently."
)


def create_client() -> Anthropic:
    """Create an Anthropic API client."""
    if not API_KEY:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not set. "
            "Copy .env.example to .env and add your API key."
        )
    return Anthropic(api_key=API_KEY)


def chat(client: Anthropic, messages: list[dict], system: str = SYSTEM_PROMPT) -> str:
    """Send a message to Claude Opus 4.6 and return the response text."""
    response = client.messages.create(
        model=MODEL_ID,
        max_tokens=MAX_TOKENS,
        system=system,
        messages=messages,
    )
    return response.content[0].text


def run_conversation() -> None:
    """Run an interactive conversation loop with Claude Opus 4.6."""
    client = create_client()
    messages: list[dict] = []

    print(f"AgentZero (powered by {MODEL_ID})")
    print("Type 'quit' or 'exit' to end the conversation.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            reply = chat(client, messages)
            messages.append({"role": "assistant", "content": reply})
            print(f"\nAgent: {reply}\n")
        except Exception as e:
            print(f"\nError: {e}\n")
            messages.pop()  # remove the failed user message
