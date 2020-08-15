class HTML_Document:
    """
    initialize some HTML for a new document.
    """

    def __init__(self):
        self.html_document = {
            "head": """
                    <html>
                        <head>
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
                        </head>
                        <body>
                  """,
            "body": """<div class="alert alert-primary" role="alert">
                        A simple primary alert—check it out!
                       </div>""",
            "end": """</body></html>"""
        }

    def add_to_body(self, tag, word):
        pass
