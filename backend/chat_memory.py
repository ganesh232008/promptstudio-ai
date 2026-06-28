"""
Conversation Memory
Stores chat history and conversation stage.
"""

conversations = {}


def create_session(session_id):
    if session_id not in conversations:
        conversations[session_id] = {
            "stage": "requirements",
            "messages": []
        }


def get_history(session_id):
    create_session(session_id)
    return conversations[session_id]["messages"]


def save_message(session_id, role, content):
    create_session(session_id)

    conversations[session_id]["messages"].append(
        {
            "role": role,
            "content": content
        }
    )


def get_stage(session_id):
    create_session(session_id)
    return conversations[session_id]["stage"]


def set_stage(session_id, stage):
    create_session(session_id)
    conversations[session_id]["stage"] = stage


def clear_history(session_id):
    conversations[session_id] = {
        "stage": "requirements",
        "messages": []
    }