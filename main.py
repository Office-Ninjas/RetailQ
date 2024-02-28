from flask import Flask, render_template, request
from flask.wrappers import Response
import openai
app = Flask(__name__)

def get_completion(prompt, model="gpt-3.5-turbo"):
    client = openai.OpenAI(api_key="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")
    
    response = client.chat.completions.create(
        model=model,
      messages = [{"role": "user", "content": prompt}],
        
    )
    return response.choices[0].message.content
@app.route("/")
def home():    
    return render_template("index.html")
  
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    #return str(bot.get_response(userText)) 
    # s = """
    #     An operating system (OS) is a software program that manages computer hardware and software resources and provides common services for computer programs. It acts as an intermediary between applications and the computer hardware, ensuring that they can communicate and function properly. Popular examples of operating systems include Microsoft Windows, macOS, and Linux.
    #     """
    # return Response(s,status=200)
    return Response(response,status=200)

if __name__ == '__main__':
    app.run(debug=True)