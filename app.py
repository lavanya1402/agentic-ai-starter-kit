import streamlit as st
from agents.first_agent import run_first_agent
from tools.text_analyzer import basic_text_stats

st.set_page_config(
    page_title="Agentic AI Starter Kit",
    layout="wide"
)

# ======================================================
# HEADER
# ======================================================

st.title("🤖 Agentic AI Starter Kit")

st.write(
    """
Enterprise AI Agent demonstrating intelligent reasoning, planning, 
tool selection, and workflow thinking.
"""
)

# ======================================================
# USER INPUT
# ======================================================

user_problem = st.text_area(
    "📝 Describe a business or technical problem:",
    value="Our DevOps team spends too much time reading failed Jenkins logs and identifying root causes.",
    height=150
)

# ======================================================
# BUTTON
# ======================================================

if st.button("🚀 Run First Agent"):

    if not user_problem.strip():
        st.warning("⚠️ Please enter a problem first.")

    else:

        with st.spinner("🧠 Agent is thinking..."):

            # Local text analysis tool
            stats = basic_text_stats(user_problem)

            # Run AI Agent
            result = run_first_agent(user_problem)

        # ======================================================
        # INPUT ANALYSIS
        # ======================================================

        st.subheader("📊 Input Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Characters", stats["character_count"])

        with col2:
            st.metric("Words", stats["word_count"])

        with col3:
            st.metric("Sentences", stats["sentence_count"])

        st.divider()

        # ======================================================
        # AGENT THINKING FLOW
        # ======================================================

        st.subheader("🧠 How the AI Agent Thought")

        # Step 1
        st.markdown("## 🔍 Step 1 — Problem Understood")

        st.info(result.problem_summary)

        # Step 2
        st.markdown("## 🏢 Step 2 — Business Domain Identified")

        st.success(result.domain)

        # Step 3
        st.markdown("## 🤖 Step 3 — AI Opportunity Detected")

        st.write(result.agent_opportunity)

        # Step 4
        st.markdown("## 🧩 Step 4 — Recommended AI Agent")

        st.success(f"✅ {result.recommended_agent_type}")

        # Step 5
        st.markdown("## 🛠️ Step 5 — Tools the Agent Thinks It Needs")

        for tool in result.tools_needed:
            st.markdown(f"- ⚙️ {tool}")

        # Step 6
        st.markdown("## 🪜 Step 6 — Suggested Execution Plan")

        for i, step in enumerate(result.next_steps, start=1):
            st.markdown(f"{i}. 🚀 {step}")

        # Step 7
        st.markdown("## ⚠️ Step 7 — Risks / Constraints")

        st.warning(result.risk_or_constraint)

        # Step 8
        st.markdown("## 📊 Step 8 — Confidence Score")

        confidence = float(result.confidence_score)

        st.progress(confidence)

        st.success(f"🟢 Confidence Score: {confidence}")

        st.divider()

        # ======================================================
        # AGENT FLOW EXPLANATION
        # ======================================================

        st.subheader("🔄 Agent Reasoning Flow")

        st.markdown(
            """
1️⃣ Understand the business problem  

2️⃣ Identify the domain  

3️⃣ Detect automation opportunity  

4️⃣ Recommend suitable AI agent  

5️⃣ Select required tools  

6️⃣ Generate execution roadmap  

7️⃣ Identify risks and constraints  

8️⃣ Estimate confidence level
"""
        )

        st.divider()

        # ======================================================
        # LEARNING POINT
        # ======================================================

        st.subheader("🎯 Learning Point")

        st.markdown(
            """
This AI agent is not simply chatting.

It is behaving like an intelligent enterprise solution architect by:

- understanding operational pain points,
- identifying AI opportunities,
- planning implementation,
- recommending tools,
- and evaluating risks before execution.

This demonstrates how:

✅ Prompt Engineering  
✅ LLM Reasoning  
✅ Structured Output  
✅ Tool Thinking  
✅ Enterprise Workflow Design  
✅ Agentic AI  

can work together inside a real AI system.
"""
        )

        st.divider()

        # ======================================================
        # OPTIONAL RAW JSON OUTPUT
        # ======================================================

        with st.expander("🧾 View Raw Structured JSON Output"):
            st.json(result.model_dump())