import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
def Generator(question,text_file_path):
    try:
        
        f = open(text_file_path)
        data = f.read()
        f.close()
        if question:
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{question} based on this provided data :-  {data[:6000]}",
            temperature=0.7,
            max_tokens = 1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
            msg = {"message":response.get("choices")[0].get("text")}
            return msg
        else:
            return {"message":"Please enter a question"}
    except Exception as e:
        return {"message": repr(e)}
    
    