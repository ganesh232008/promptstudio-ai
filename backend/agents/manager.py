from backend.agents.requirement_agent import collect_requirements
from backend.agents.prompt_generator import generate_prompt
from backend.agents.reviewer_agent import review_prompt
from backend.agents.optimizer_agent import optimize_prompt
from backend.agents.formatter_agent import format_prompt

from backend.chat_memory import (
    get_stage,
    set_stage,
)


def process_request(session_id, history):
    """
    PromptForge AI Manager Agent

    Controls the complete multi-agent workflow.
    """

    stage = get_stage(session_id)

    # Convert conversation history into plain text
    conversation = "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in history
        ]
    )

    # =====================================
    # Stage 1 : Requirement Collection
    # =====================================

    if stage == "requirements":

        result = collect_requirements(conversation)

        # Gemini may return slightly different formats.
        # Check more safely.
        if "ENOUGH_INFORMATION" in result.upper():
            set_stage(session_id, "generate")
            stage = "generate"
        else:
            return result

    # =====================================
    # Stage 2 : Prompt Generation Pipeline
    # =====================================

    if stage == "generate":

        # Agent 1 - Prompt Generator
        prompt = generate_prompt(conversation)

        # Agent 2 - Reviewer
        reviewed_prompt = review_prompt(prompt)

        # Agent 3 - Optimizer
        optimized_prompt = optimize_prompt(reviewed_prompt)

        # Agent 4 - Formatter
        final_prompt = format_prompt(optimized_prompt)

        set_stage(session_id, "completed")

        return final_prompt

    # =====================================
    # Stage 3 : Conversation Completed
    # =====================================

    if stage == "completed":

        return (
            "✅ Your prompt has already been generated.\n\n"
            "Click **New Chat** to create another prompt."
        )

    # =====================================
    # Fallback
    # =====================================

    return "Something went wrong. Please start a new chat."