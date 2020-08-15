import boto3

s3_resource = boto3.resource('s3')


class AWS_Manager:
    """
    the connections to boto3 and some functions that let you save your file to S3.
    """

    def __init__(self):
        pass

    def upload_file(self):

        try:
            s3_resource.meta.client.upload_file(
                './simple_html.html', 'lmtd-class', 'kai_html.html')

        except:
            print('there is an err')
