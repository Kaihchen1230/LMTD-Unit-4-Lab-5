class HTML_Document:
    """
    initialize some HTML for a new document.
    """

    def __init__(self, html_start_tag, html_content, html_end_tag):

        self.html_start_tag = html_start_tag
        self.html_content = html_content
        self.html_end_tag = html_end_tag

    def get_html_info(self):
        return f"{self.html_start_tag} {self.html_content} {self.html_end_tag}"
