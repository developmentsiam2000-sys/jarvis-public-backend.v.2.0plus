import urllib.parse,urllib.request,json
def web_search(query,limit=5):
    q=urllib.parse.quote(query);url=f"https://api.duckduckgo.com/?q={q}&format=json&no_html=1&skip_disambig=1"
    req=urllib.request.Request(url,headers={"User-Agent":"JARVIS/2.0"})
    with urllib.request.urlopen(req,timeout=10) as r:data=json.loads(r.read().decode())
    out=[]
    if data.get("AbstractText"):out.append({"title":data.get("Heading","Result"),"snippet":data["AbstractText"],"url":data.get("AbstractURL","")})
    for x in data.get("RelatedTopics",[]):
        if "Text"in x and "FirstURL"in x:out.append({"title":x["Text"][:80],"snippet":x["Text"],"url":x["FirstURL"]})
        if len(out)>=limit:break
    return out[:limit]
