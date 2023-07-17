from flask import Flask, render_template, request
from translator import englishToFrench, frenchToEnglish

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishtoFrench():
    textToTranslate = request.args.get('textToTranslate')
    NewText= englishToFrench(textToTranslate)
    return (NewText)

@app.route("/frenchToEnglish")
def frenchtoEnglish():
    textToTranslate = request.args.get('textToTranslate')
    NewText = frenchToEnglish(textToTranslate)
    return (NewText)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
