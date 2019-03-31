import eel

# Set web files folder and optionally specify which file types to check for eel.expose()
eel.init('web', allowed_extensions=['.js', '.html'])

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

eel.say_hello_js('Python World')   # Call a Javascript function

eel.start('hello.html')    # Start  , size=(300, 200)
