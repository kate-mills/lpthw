import web

urls = (' /hello', 'Index')

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")


class Index(object):
  def GET(self):
    return render.hello_form()  # going to display hello_form.html instead of index.html

  def POST(self):
    # gets input from the browser and converts it to a variable we can display
    form = web.input(name="Nobody", greet="Hola")
    greeting = " %s, %s " % (form.greet, form.name)
    return render.index(greeting=greeting)


if __name__ == "__main__":
  app.run()
