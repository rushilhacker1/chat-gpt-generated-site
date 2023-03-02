from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

# Create a Flask app instance
app = Flask(__name__)


# Set up a connection to a SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exaple.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['HOST'] = '192.168.1.8'
db = SQLAlchemy(app)


# Define a model for a blog post
class BlogPost(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    title   = db.Column(db.String(80), nullable=False)
    type    = db.Column(db.String(15), nullable=False)
    content = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<BlogPost {self.title}>'

with app.app_context():
    db.create_all()


# Set up a Flask-Restful API
api = Api(app)

# Define a resource for getting all blog posts
class BlogPostList(Resource):
    def get(self):
        posts = BlogPost.query.all()
        return [{'id': post.id, 'title': post.title,'type': post.type, 'content': post.content} for post in posts]

# Register the resource with the API
api.add_resource(BlogPostList, '/blog/posts')

if __name__ == '__main__':
    app.run()
