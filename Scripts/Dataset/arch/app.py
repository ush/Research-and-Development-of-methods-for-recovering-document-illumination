import sys
from docscan.doc import scan

sys.stdout.buffer.write(scan(sys.stdin.buffer.read()))

#cat 17.jpg | python app.py > out.jpg
