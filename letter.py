from flask import Flask, render_template

letter = Flask(__name__)


def count_letters(filename):
    with open(filename, "r") as file:  
        text = file.read()  
    letter_count = sum(1 for char in text if char.isalpha())  
    return letter_count, text  

@letter.route("/")
def home():
    filename = "sample.txt"  
    letter_count, file_content = count_letters(filename)  
    return render_template("index.html", filename=filename, letter_count=letter_count, file_content=file_content)

if __name__ == "__main__":
    letter.run(debug=True)
