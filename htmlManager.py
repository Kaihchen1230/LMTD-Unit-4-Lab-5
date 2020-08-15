from htmlDocument import HTML_Document
from awsManager import AWS_Manager


class HTML_Manager:

    """
    defines functions that let you create a new HTML document, and save the document to your files.
    """

    def __init__(self):
        self.html_documents = {
            "html_head":
            """
            <html>
                <head>
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
                </head>
                <body>
            """,
            "body": """<form>""",
            "end": """</form></body></html>"""
        }

        self.aws_manager = AWS_Manager()

        self.aws_manager.download_file()

        self.options = {
            "1": self.create_header,
            "2": self.create_email_field,
            "3": self.create_password_field,
            "4": self.create_select_field,
            "5": self.create_text_area,
            "6": self.create_button
        }

    def display_options(self):
        print("""
            ************* MAIN MENU *************
             Welcome to HTML Form Generator!

             Please choose one of the options below:

             1. Create A Header

             2. Create A Email Field

             3. Create A Password Field

             4. Create Select Field

             5. Create Textarea

             6. Create Button

             Q. Quit and Generate HTML File

             """)

    def run(self):

        while True:

            self.display_options()

            option = input("Enter your option: ")

            if option.lower() == "q":
                print("HTML file is generated, bye")
                self.save_to_file()
                break

            action = self.options.get(option)

            if action:
                action()

            else:
                print(f"{option} is not valid.....")

    def create_header(self):

        start_tag = """ <div class="form-group"><h2 class="text-center">"""
        header_text = input("Plase enter the header to display on the form: ")
        end_tag = """</h2></div>"""

        html_document = HTML_Document(start_tag, header_text, end_tag)

        self.html_documents["body"] += html_document.get_html_info()

    def create_email_field(self):
        start_tag = """<div class="form-group text-center"><label for="email-field" class="p-r-2">Email address:</label>"""
        content = """<input type="email" class="form-control d-inline w-50" id="email-field">
                    """
        end_tag = """</div>"""

        html_document = HTML_Document(start_tag, content, end_tag)

        self.html_documents["body"] += html_document.get_html_info()

    def create_password_field(self):

        start_tag = """<div class="form-group text-center"><label for="password-field" class="p-r-2">Password: </label>"""
        content = """<input type="password" class="form-control d-inline w-50" id="password-field">
                            """
        end_tag = """</div>"""

        html_document = HTML_Document(start_tag, content, end_tag)

        self.html_documents["body"] += html_document.get_html_info()

    def create_select_field(self):

        select_section_name = input("Enter the name for this select section: ")
        select_options = set()

        while True:

            option = input(
                "Please enter the option to display on the form or Q to finish: ")

            if option.lower() == "q":
                print("the options that you entered so far: ", select_options)
                break

            select_options.add(option)

        start_tag = f"""<div class="form-group text-center">
                            <label for="select-field" class="p-r-2">{select_section_name}</label>
                            <select class="form-control d-inline w-50" id="select-field"> """

        content = ""

        for option in select_options:
            content += f""" <option>{option}</option>"""

        end_tag = """</select></div>"""

        html_document = HTML_Document(start_tag, content, end_tag)

        self.html_documents["body"] += html_document.get_html_info()

        print("Select element generated successfully")

    def create_text_area(self):

        section_name = input("Enter the name for this section: ")

        start_tag = f"""<div class="form-group text-center">
                            <label for="{section_name}" class="p-r-2"> {section_name} </label>"""

        content = f"""<textarea class="form-control d-inline w-50" id="{section_name}" rows="3"></textarea>"""
        end_tag = """</div>"""

        html_document = HTML_Document(start_tag, content, end_tag)

        self.html_documents["body"] += html_document.get_html_info()

        print("Textarea generated successfully")

    def create_button(self):

        button_name = input("Enter the name for this button: ")

        start_tag = """<div class="form-group text-center">"""

        content = f"""<button type="button" class="btn btn-primary">{button_name}</button>"""

        end_tag = """</div>"""
        html_document = HTML_Document(start_tag, content, end_tag)

        self.html_documents["body"] += html_document.get_html_info()

        print("Button generated successfully")

    def save_to_file(self):

        with open("simple_html.html", "w") as simple_html:

            html_page = ""

            for content in self.html_documents.values():

                html_page += content

            simple_html.write(html_page)

            self.aws_manager.upload_file()
