# 🏙️ **RealEstate Research Tool**

A smart and user-friendly web app designed for seamless article analysis in the **real estate domain**—with the flexibility to adapt to **any field of research**.

Simply input article URLs and ask questions to receive accurate insights, powered by cutting-edge LLMs and vector-based search.




## 🚀 Features

* 🔗 **URL Input**: Load and analyze article content directly from the web.
* 🧠 **AI-Powered Processing**: Uses LangChain’s `UnstructuredURLLoader` to extract and parse content.
* 📚 **Vector Embeddings**: Converts content into embeddings via HuggingFace models and stores them in **ChromaDB** for fast and relevant retrieval.
* 💬 **LLM Interaction**: Ask questions and get insightful answers with sources, powered by **Llama 3 via Groq**.



## ⚙️ Set-Up Instructions

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Add your Groq credentials**:
   Create a `.env` file in the root directory and include the following:

   ```env
   GROQ_MODEL=MODEL_NAME_HERE
   GROQ_API_KEY=GROQ_API_KEY_HERE
   ```

3. **Run the Streamlit app**:

   ```bash
   streamlit run main.py
   ```



## 💡 How to Use

Once the app is launched:

* Use the **sidebar** to enter one or more news article URLs.
* Click **“Process URLs”** to extract, chunk, and embed the article content.
* Embeddings are generated using HuggingFace models and stored in ChromaDB.
* Ask any **natural language question** about the loaded articles.
* Receive an **answer** along with the **source URLs** where the information came from.



## 📰 Sample Articles Used

* [How the Federal Reserve’s rate policy affects mortgages](https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html)
* [Why mortgage rates jumped despite Fed interest rate cut](https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html)
* [Dividend-paying real estate stocks to watch in 2025](https://www.cnbc.com/2024/12/17/wall-street-sees-upside-in-2025-for-these-dividend-paying-real-estate-stocks.html)



## 📽️ Project Demo Video

![Watch the video](https://github.com/Rohesen/real-estate-tool-using-rag/blob/main/project_video.gif)



## 🖼️ Screenshots

| Home Page                          | Processing View                          | Q\&A Interface                   |
| ---------------------------------- | ---------------------------------------- | -------------------------------- |
| ![Home](resources/HomePage.png) | ![Processing](resources/ProcessingPage.png) | ![QA](resources/QnAPage.png) |



## 📄 License

This project is released under the **MIT License**, with the following additional terms:

* **Commercial use is strictly prohibited** without prior written permission from the author.
* Attribution must be given in all copies or substantial portions of the software.

