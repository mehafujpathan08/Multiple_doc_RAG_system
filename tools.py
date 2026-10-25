def email_tool(task: str):
    return f"""
Subject: Important Update

Dear Client,

{task}

Best regards,  
Your Team
"""


def linkedin_tool(task: str):
    return f"""
🚀 {task}

#AI #Automation #Future
"""


def summary_tool(text: str):
    return text[:200] + "..."