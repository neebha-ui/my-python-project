# import pypdf
# import gtts

# from pypdf import PdfReader

# reader = PdfReader("python.pdf")



from gtts import gTTS
tts = gTTS('hello iam swetha currently learning python programming language', lang='en')
tts.save('hello.mp3')
