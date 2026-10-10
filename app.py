import gradio as gr
import fitz
import ollama

def explain_doc(file, dialect):
    doc = fitz.open(file.name)
    text = "".join([page.get_text() for page in doc])[:4000]
    prompt = f"Explain this legal document simply in {dialect}, list key dates, risks and next steps. Document: {text}"
    response = ollama.chat(model='apertus-8b-instruct', messages=[{'role':'user','content':prompt}])
    return response['message']['content']

demo = gr.Interface(
    fn=explain_doc,
    inputs=[gr.File(label="Upload PDF"), gr.Dropdown(["Swiss-German","French","Urdu","Punjabi","English"], value="Urdu", label="Choose dialect")],
    outputs=gr.Textbox(label="Simple Explanation"),
    title="Nyaya Saathi on Apertus",
    description="Sovereign offline AI - explains legal docs in your dialect, no cloud."
)
demo.launch()
