from flask import Flask, render_template
import traversal

app = Flask(__name__)


@app.route('/')
def index():
    inorder, preorder, postorder = traversal.aufruf()

    return render_template('index.html', inorder=inorder, preorder=preorder, postorder=postorder)


if __name__ == '__main__':
    app.run()
