# Udemy - LangChain- Develop LLM powered applications with LangChain

Content-based on the [LangChain- Develop LLM powered applications with LangChain](https://www.udemy.com/course/langchain/) course by [Eden Marco](https://www.udemy.com/course/langchain/#instructor-1) on Udemy.

## Course to learn and practice
- Python
- LangChain framework
- LLMs (Large Language Models)

## Run

### 1. Clone the project

### 2. Create and activate the Python virtual environment

```
python -m venv venv

venv\Scripts\activate
```

[More info for virtual environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

### 4. Install the requirements

```
pip install -r requirements.txt
```

### 4. Create an .env file and configure the following values

```
OPENAI_API_KEY=<YOUR-API-KEY-HERE>
PROXYCURL_API_KEY=<YOUR-API-KEY-HERE>
SERPAPI_API_KEY=<YOUR-API-KEY-HERE>
PINECONE_API_KEY=<YOUR-API-KEY-HERE>
PINECONE_ENVIRONMENT_REGION=<YOUR-API-KEY-HERE>
```

### 5. Run the desired project
 * Ice Breaker based on LinkedIn information:
   ```bash
    cd 01_ice_breaker
    python app.py
   ```

 * Documentation Helper (Based on Langchain Docs):
    * Download Langchain docs: ```wget -r -A.html -P langchain-docs https://api.python.langchain.com/en/latest/api_reference.html```
    * Data ingestion to Vector Store:
      ```bash
        cd 02_documentation_helper/ingestion
        python ingest.py
      ```