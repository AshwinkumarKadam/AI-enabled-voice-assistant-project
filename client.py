


client = genai.Client(api_key="AIzaSyCW5oRD0g1lVbqc_SFsypck49CBNGS5W8o")

completion = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="role":"system","content":"you are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"
        
    

)