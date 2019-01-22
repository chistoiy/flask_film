from film import db,create_app
app = create_app()
app_ctx = app.app_context() # app_ctx = film/g
with app_ctx: # __enter__,通过LocalStack放入Local中
    db.create_all()
