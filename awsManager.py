import boto3

s3_client = boto3.client('s3')


class AWS_Manager:
    """
    the connections to boto3 and some functions that let you save your file to S3.
    """

    def __init__(self):
        pass

    def upload_file(self):

        try:
            s3_client.upload_file(
                Filename="simple_html.html", Bucket="lmtd-class", Key="kai_html_testing.html")

        except:
            print('there is an err')

    def download_file(self):
        try:
            s3_client.download_file(
                'lmtd-class', 'kai_html_testing.html', 'kai_html_testing.html')

        except:
            print('there is an error')
