import webapp2
# import os
# from google.appengine.ext.webapp import template
# import jinja2

page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script src="static/game-frame.js"></script>
    <link rel="stylesheet" href="static/game-frame-styles.css" />
  </head>
 
  <body id="level1">
    <img src="static/logos/level1.png">
      <div>
"""
 
page_footer = """
    </div>
  </body>
</html>
"""
 
main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""
 
class MainPage(webapp2.RequestHandler):
 
  def render_string(self, s):
    self.response.out.write(s)
 
  def get(self):
    # Disable the reflected XSS filter for demonstration purposes
    # self.response.headers.add_header("X-XSS-Protection", "1")
 
    # csp 2.0
    self.response.headers.add_header("Content-Security-Policy", "script-src 'self' style-src 'self'")
    
    # csp 3.0
    # self.response.headers.add_header("Content-Security-Policy", "script-src 'self' style-src 'self'")

    if not self.request.get('query'):
      # Show main search page
      self.render_string(page_header + main_page_markup + page_footer)
    else:
      query = self.request.get('query', '[empty]')
       
      # Our search engine broke, we found no results :-(
      message = "Sorry, no results were found for <b>" + query + "</b>."
      message += " <a href='?'>Try again</a>."
 
      # Display the results page
      self.render_string(page_header + message + page_footer)
     
    return
 
app = webapp2.WSGIApplication([ 
  ('/', MainPage), 
  ], debug= True)