import logging

import boto3
from bokeh.plotting import output_file, save
from botocore.exceptions import ClientError

from plot_helpers import produce_plot


def lambda_handler(event, context):
    plot = produce_plot()
    output_file('/tmp/index.html')
    save(plot, title="Matt's Subway Stats")
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file('/tmp/index.html', "subwaytripswebsite", 'index.html',
                                         ExtraArgs={'ContentType': 'text/html'})
    except ClientError as e:
        logging.error(e)
