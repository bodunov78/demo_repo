f=open("url2.txt",encoding="utf8")
w=open("ur2.html","w+",encoding="utf8")

w.write('<html><head><meta charset="UTF-8"></head><body>')
for s in f:
    m =s.strip().split()
    print (m)
    w.write(f'<li><a href="{m[1]}" target={m[0]}><h1>{m[0]}<h1></a></li>')

w.write("</body></html>")
