from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    template = """Given the full name {person_name} I want you to get it me a link to the LinkedIn profile page.
    Your answer should only contain a URL"""

    agent_tools = [
        Tool(
            name="Crawl Google for LinkedIn profile",
            func="?",
            description="Useful for when you need the LinkedIn page url",
        )
    ]

    agent = initialize_agent(
        tools=agent_tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    promp_template = PromptTemplate(template=template, input_variables=["person_name"])

    linkedin_profile_url = agent.run(promp_template.format_prompt(person_name=name))

    return linkedin_profile_url
