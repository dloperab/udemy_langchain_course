from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from dotenv import load_dotenv

from src.integrations.linkedin import scrape_profile

load_dotenv()


if __name__ == "__main__":
    summary_template = """
      Given the LinkedIn information {information} about a person from, I want you to create:
      1. A short summary
      2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_profile(
        linkedin_profile_url="https://www.linkedin.com/in/dloperab/",
        mock_data=True,
    )

    print(chain.run(information=linkedin_data))
