from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, abort, reqparse, marshal_with, fields
from flask_cors import CORS

# Create a Flask app instance
app = Flask(__name__)
CORS(app)

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
    content = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f'<BlogPost {self.title}>'

with app.app_context():
    db.create_all()


resource_fields = {

    "id":fields.Integer,
    "title": fields.String,
    "type": fields.String,
    "content":fields.String
}


blog_put_args = reqparse.RequestParser()
blog_put_args.add_argument("title", type=str, help="title of the blog", required=True )
blog_put_args.add_argument("type", type=str, help="type of the blog(featured/top/there)", required=True )
blog_put_args.add_argument("content", type=str, help="this is the main part", required=True )



# Set up a Flask-Restful API
api = Api(app)

# Define a resource for getting all blog posts
class BlogPostList(Resource):
    def post(self, user_id):
        posts = BlogPost.query.filter_by(id=user_id).all()
        if not posts:
            abort(404, message="Could not find user with that id")
        return [{'id': post.id, 'title': post.title,'type': post.type, 'content': post.content} for post in posts]
         

    def get(self, user_id):
        posts = BlogPost.query.all()
        return [{'id': post.id, 'title': post.title,'type': post.type, 'content': post.content} for post in posts]   
    
    @marshal_with(resource_fields)
    def put(self, user_id):
        args = blog_put_args.parse_args()
        result = BlogPost.query.filter_by(id=user_id).first()
        if result:
            abort(409, message="User id taken...")

        user = BlogPost(id=user_id, title=args['title'], type=args['type'], content=args['content'])
        db.session.add(user)
        db.session.commit()
        return user, 201
# Register the resource with the API
api.add_resource(BlogPostList, '/blog/posts/<int:user_id>')

if __name__ == '__main__':
    app.run()
