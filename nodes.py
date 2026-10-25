from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

from tools import email_tool, linkedin_tool, summary_tool

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env", override=True)

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# 🧠 1. PLANNER AGENT
def planner_agent(state):
    user_input = state["input"]

    prompt = f"""
    You are a planner agent.

    Break this task into clear steps:

    Task: {user_input}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"plan": response.content}


# 🔧 2. TOOL SELECTION AGENT
def tool_agent(state):
    user_input = state["input"]

    prompt = f"""
    Decide which tool to use:

    Task: {user_input}

    Options:
    - email
    - linkedin
    - summary
    - general

    Return only one word.
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"tool": response.content.strip().lower()}

# ⚙️ 3. EXECUTOR AGENT (MULTI-AGENT COLLABORATION)
def executor_agent(state):
    user_input = state["input"]
    tool = state["tool"]
    plan = state["plan"]   # 🔥 IMPORTANT (coming from planner)

    # 🔥 Base prompt (this is where collaboration happens)
    base_prompt = f"""
    You are an execution agent.

    Task:
    {user_input}

    Plan created by planner agent:
    {plan}

    Follow the plan and generate the best possible output.
    """

    # 🔥 Tool-specific instructions
    if "email" in tool:
        prompt = base_prompt + """
        Write a professional email.

        Requirements:
        - Formal tone
        - Clear structure
        - Do NOT assume fake details
        - Use placeholders if needed
        - No extra explanation outside email
        - Use realistic human signature
        """

        response = llm.invoke([HumanMessage(content=prompt)])
        result = response.content

    elif "linkedin" in tool:
        prompt = base_prompt + """
        Write a viral LinkedIn post.
        Make it:
        - Engaging
        - Short and impactful
        - Include relevant hashtags
        """

        response = llm.invoke([HumanMessage(content=prompt)])
        result = response.content

    elif "summary" in tool:
        prompt = base_prompt + """
        Write a concise summary.
        """

        response = llm.invoke([HumanMessage(content=prompt)])
        result = response.content

    else:
        prompt = base_prompt

        response = llm.invoke([HumanMessage(content=prompt)])
        result = response.content

    return {"output": result}