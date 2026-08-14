import json,os,urllib.request
URL=os.getenv("JARVIS_OLLAMA_URL","http://127.0.0.1:11434/api/chat")
MODEL=os.getenv("JARVIS_MODEL","qwen2.5:0.5b")
SYSTEM='''You are JARVIS, a helpful AI assistant. Answer clearly and honestly. Help with programming, explanations, writing and general questions. Use supplied file and web context when present. Do not invent missing facts.'''
def ask_ai(history,user_message,context=""):
    msgs=[{"role":"system","content":SYSTEM}]
    for x in history[-20:]:msgs.append({"role":x["role"],"content":x["content"]})
    content=user_message+("\n\nAdditional context:\n"+context if context else "")
    msgs.append({"role":"user","content":content})
    body=json.dumps({"model":MODEL,"messages":msgs,"stream":False}).encode()
    req=urllib.request.Request(URL,data=body,headers={"Content-Type":"application/json"},method="POST")
    with urllib.request.urlopen(req,timeout=180) as r:data=json.loads(r.read().decode())
    return data["message"]["content"]
