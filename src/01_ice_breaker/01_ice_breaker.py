from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from dotenv import load_dotenv

load_dotenv()

information = """
Nubia Muñoz (born 1940) is a Colombian medical scientist and epidemiologist, whose research has been instrumental in establishing that human papillomavirus (HPV) infection is the primary cause of cervical cancer which has led to the development of a vaccine that is capable of preventing 70% of all cervical cancers.

Biography
Her father, a farm worker in Cali died of diphtheria when she was six years old.[1] She would be the only one of her siblings to go to university when she was accepted into the medical school at Universidad del Valle,[citation needed] specializing in Pathology. After graduating, she completed a fellowship at the National Cancer Institute in Bethesda, Maryland, USA with an emphasis in pathology and virology. She then earned a Master's Degree in Public Health (Cancer Epidemiology) from Johns Hopkins University in Baltimore, Maryland, USA.

In 1969, she joined the International Agency for Research on Cancer (IARC) headquarters in Lyon, France, where she researched cancers formed due to pathogens. In the 1980s, she led her own unit at the IARC, where she studied the link between HPV and cervical cancer. In 1995, she was instrumental in the IARC's decision to classify HPVs 16 and 18 as group 1 human carcinogens.[2][3][4]

She retired from the IARC in 2001, but continues to work at the Catalan Institute of Oncology in Barcelona and the National Cancer Institute in Bogota where she is Emeritus Professor.[5]
"""

if __name__ == "__main__":
    print("Hello LancgChain!")

    summary_template = """
    given the information {information} about a person from. I want you to create:
    1. a short summary (2 sentences max)
    2. two interesting facts about them
  """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))
