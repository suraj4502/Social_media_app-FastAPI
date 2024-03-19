from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from Social_media.routers import post, user, auth, vote

# import models
# from database import engine
# models.Base.metadata.create_all(bind=engine) -> this is the command that tells sql alchemy to generate all the  tables.

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(response: Response):
    response.headers["Content-Type"] = "text/html"
    return (
        "<html>"
        "<head>"
        "<style>"
        "body { font-family: Arial, sans-serif; background-color: #f5f5f5; margin: 0; padding: 20px; }"
        "h1 { color: #333; }"
        "p, ol, ul { color: #555; }"
        "ol { margin-left: 20px; }"
        "li { margin-bottom: 10px; }"
        "a { color: #007bff; text-decoration: none; }"
        "</style>"
        "</head>"
        "<body>"
        "<h1>Greetings, Earthlings! Welcome to our Social Network Backend.</h1>"
        "<p><strong>How to use the app:</strong></p>"
        "<ol>"
        "<li>Go to <a href='https://social-media-app-fastapi.onrender.com/docs' target='_blank'>https://social-media-app-fastapi.onrender.com/docs</a></li>"
        "<li>Use the '/users' POST method to create a user (passwords are hashed, so no one can see them, not even the developers).</li>"
        "<li>Then login using the credentials.</li>"
        "<li>Explore the Posts section:-"
        "<ul>"
        "<li>Create a post, update it, and delete it (use the shown template to create and update posts).</li>"
        "</ul>"
        "</li>"
        "<li>Use the '/posts' POST method to like or dislike a post (provide post_id and direction, 1 = like, 0 = dislike).</li>"
        "</ol>"
        "</body>"
        "</html>"
    )


    

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(vote.router)





