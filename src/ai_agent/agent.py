import google.generativeai as genai
import os

Ambil API KEY gratis dari aistudio.google.com
Jangan taruh key asli di GitHub, pakai Secrets
API_KEY = os.getenv("GEMINI_API_KEY") or "YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)

def tanya_ai_umk(pesan_pembeli):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    Kamu adalah AI asisten toko UMKM Padang yang ramah.
    Jawab pertanyaan pembeli ini dengan singkat & membantu:
    {pesan_pembeli}
    """
    response = model.generate_content(prompt)
    return response.text

if name == "main":
    print(tanya_ai_umk("Kopi apa yang paling enak dari Padang?"))
