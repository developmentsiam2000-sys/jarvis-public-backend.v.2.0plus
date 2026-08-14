import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent/"data"/"chats";ROOT.mkdir(parents=True,exist_ok=True)
def path(cid):
    safe="".join(c for c in cid if c.isalnum() or c in "-_");return ROOT/f"{safe}.json"
def get_messages(cid):
    p=path(cid)
    if not p.exists():return []
    try:return json.loads(p.read_text(encoding="utf-8"))
    except:return []
def save_message(cid,role,content):
    x=get_messages(cid);x.append({"role":role,"content":content});path(cid).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding="utf-8")
def clear_history(cid):
    p=path(cid)
    if p.exists():p.unlink()
