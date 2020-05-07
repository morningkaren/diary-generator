from flask import Flask, request, send_file, render_template
import tensorflow as tf
import os
import tensorflow as tf
import gpt_2_simple as gpt2

app = Flask(__name__)


@app.route('/')
def function():
    #if request.method == 'POST':
    return render_template('index.html')

@app.route('/', methods=["POST"])
def result():
    sess = gpt2.start_tf_sess(threads=1)
    gpt2.load_gpt2(sess)
    text = gpt2.generate(sess,return_as_list=True)[0]
    return text


if __name__ == '__main__':
    app.run('0.0.0.0', os.environ.get('PORT', 8080))
