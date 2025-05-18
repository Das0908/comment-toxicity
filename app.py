from flask import Flask , request , url_for , redirect ,render_template

from run import score

app = Flask(__name__ , template_folder='templates')

@app.route('/' , methods = ['GET' , 'POST'])
def run():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        comment = request.form.get('comment')
        # i want to run the run.py file here , the score function 
        # , then pass the output to index.html 
        out = score(comment)

        return render_template('index.html' , output = out)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0' , debug=True) 

        




        

