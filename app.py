print("HI")
name = input("ENter your name: ")
print(name)

flask = __import__('flask')
app = flask.Flask(__name__)
@app.route('/')
def hello_world():
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)