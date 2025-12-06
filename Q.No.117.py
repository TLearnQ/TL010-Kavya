data = {
    "claims": [
        {"name": "A", "status": "open"},
        {"name": "B", "status": "closed"}
    ]
}
out = {}
for c in data["claims"]:
    k = c["status"]
    out.setdefault(k, []).append(c)
print(out)
