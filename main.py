

# In[3]:


import getpass
import os
import streamlit as st

# ### 1. Load and Split Document

# In[12]:


# Load the text file

from langchain_community.document_loaders import TextLoader
file_path = "chapter7.txt"
loader = TextLoader(file_path)
docs = loader.load()

# ### 2. Embed Document

# In[ ]:


from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()


# ### 3. Vectorstore

# In[ ]:


from langchain_community.vectorstores import FAISS

vector_store = FAISS.from_documents(docs, embeddings)


# ### 4. Retrieve

# In[ ]:


retriever = vector_store.as_retriever()


# ### 5. Question and Answer



from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.output_parsers import StrOutputParser



llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""Answer the following question in English based only on the provided context. If you cannot find any relavant information in the provided context, say "I'm sorry, I could not find relavant information in Book 7 of Gallic War.":
<context>
{context}
</context>
Question: {input}""")

combine_docs_chain = create_stuff_documents_chain(
    llm=llm,
    prompt=prompt,
  #  output_parser=StrOutputParser()
)
rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

#UI


st.markdown("""
# Gallic War Query Assistant 
Ask any question about Commentaries on Gallic War by Julius Caesar, and I will provide information! 
※The current version can only answer questions regarding Book 7, as this is the only chapter the programmer has read so far, and so he cannot verify the accuracy of its responses about the other books

---

### How to use
1. Get your OpenAI API Key (https://platform.openai.com/api-keys) and enter it in the first input box.
2. Enter your question in the second input box and click Submit.

""")


# Set the API key as an environment variable if provided
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    st.success("API key has been set successfully!")
else:
    st.warning("Please enter your OpenAI API key to proceed.")

user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    if user_input:
        response = rag_chain.invoke({"input":user_input})
        st.write(response["answer"])
    else:
        st.write("Please enter a query.")


