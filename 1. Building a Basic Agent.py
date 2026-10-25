# Here we implement the python parallel of the code in Agents 101, by setting an Agent to only follow Prompts

import os #We import os, to access the local .env file which contains the API Key
from dotenv import load_dotenv #We import the tool that reads our .env file and loads its contents
from openai import OpenAI #Although we route our request to Groq, we use Open AI's Library, as Groq has the same API structure

 
load_dotenv() #Loads our local .env file, to access the API Key

class Agent:
    def __init__(self, name: str, instructions: str, model: str):
        self.name = name
        self.instructions = instructions
        self.model = model

        #The above 3 lines, save the passed-in values into the agent object so it remembers who and what it is.
        
        # Initialize the client inside the agent
        self.client = OpenAI( #Creates a connection client to talk to the AI provider.
            api_key=os.getenv("GROQ_API_KEY"), #GROQ_API_KEY is the variable in the .env file which has the API Key
            base_url="https://api.groq.com/openai/v1" #Points Open AI library, from its server, to Groq's server
        )

    def run(self, user_message: str):
        #Sends the message to the model using the agent's instructions
        response = self.client.chat.completions.create( #Sends the request to the model
            model=self.model, 
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content

my_agent = Agent(   #Calls our agent
    name="my-agent",
    instructions="You are a helpful AI assistant learning about building AI agents.",
    model="openai/gpt-oss-20b"
)

print(f"[{my_agent.name}] is thinking...")
answer = my_agent.run("In one short sentence, what makes an AI agent special?") #Our Prompt

print("\n--- Agent Response ---")
print(answer)
