import io
import os

text='Hello from python\n'
file=io.StringIO(text)
file.read()
file.write('python is awesome')
file.seek(0)
print(file.read())

print(os.getcwd())
print(os.listdir())