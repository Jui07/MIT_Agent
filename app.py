import streamlit as st
from graph import graph

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MIT College Agent",
    page_icon="🎓",
    layout="centered",
)

# ── Header ─────────────────────────────────────────────────────────────────────
st.title("🎓 MIT College Agent")
st.caption("Ask anything about MIT — admissions, courses, or research.")

# ── Intent badge colours ────────────────────────────────────────────────────────
INTENT_COLORS = {
    "admission": "🟢 Admission",
    "courses":   "🔵 Courses",
    "research":  "🟣 Research",
}

# ── Chat history (session state) ────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []          # list of {"role", "content", "intent"}

# Render existing chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and msg.get("intent"):
            st.caption(INTENT_COLORS.get(msg["intent"], ""))
        st.markdown(msg["content"])

# ── Input ───────────────────────────────────────────────────────────────────────
if prompt := st.chat_input("Ask about MIT admissions, courses, or research…"):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run the LangGraph agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            result = graph.invoke({
                "question": prompt,
                "intent": "",
                "answer": "",
            })

        intent = result.get("intent", "")
        answer = result.get("answer", "No answer returned.")

        st.caption(INTENT_COLORS.get(intent, ""))
        st.markdown(answer)

    # Save assistant reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "intent": intent,
    })
