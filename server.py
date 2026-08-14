from fastapi import FastAPI,HTTPException,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai import ask_ai
from memory import get_messages,save_message,clear_history
from files import save_upload,read_file_text
from search import web_search
app=FastAPI(title="JARVIS AI v2")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
class ChatRequest(BaseModel):
    conversation_id:str
    message:str
    files:list[str]=[]
@app.get("/health")
def health():return {"status":"online","name":"JARVIS","version":"2.0"}
@app.get("/history/{cid}")
def history(cid:str):return {"messages":get_messages(cid)}
@app.delete("/history/{cid}")
def delete(cid:str):clear_history(cid);return {"ok":True}
@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    data=await file.read()
    if len(data)>10*1024*1024:raise HTTPException(413,"File is larger than 10 MB")
    p=save_upload(file.filename,data);return {"name":p.name,"size":len(data)}
@app.post("/chat")
def chat(req:ChatRequest):
    if not req.message.strip():raise HTTPException(400,"Message cannot be empty")
    history=get_messages(req.conversation_id);save_message(req.conversation_id,"user",req.message)
    context=""
    for name in req.files[-5:]:
        try:context+=f"\nFILE {name}:\n{read_file_text(name)[:12000]}\n"
        except Exception:pass
    if req.message.lower().startswith(("search ","look up ","find online ","latest news","what is the latest")):
        try:
            results=web_search(req.message)
            context+="\nWEB RESULTS:\n"+"\n".join(f"- {x['title']}: {x['snippet']} ({x['url']})" for x in results)
        except Exception:pass
    try:reply=ask_ai(history,req.message,context)
    except Exception as e:raise HTTPException(500,str(e))
    save_message(req.conversation_id,"assistant",reply);return {"reply":reply}
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
