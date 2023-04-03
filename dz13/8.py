def render_input(field ):
    def wrapped ():
     print ("<p>"+f'<input id ="id_{field }" name ="{field }">'+"</p>")
    wrapped ()

render_input("username ")