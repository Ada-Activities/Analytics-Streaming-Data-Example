# Analytics-Streaming-Data-Example

This repository contains an example of streaming data analytics using Amazon Kinesis Data Streams to be used in the Analytics round table live exploration section.

## Overview

In this example, we will simulate a streaming data source by generating random event data and sending it to an Amazon Kinesis Data Stream. The Amazon Data Firehose attached to the stream will then deliver the data to an Amazon S3 bucket for storage and further analysis.

## Prerequisites

- An AWS account with permissions to create and manage Kinesis Data Streams, Data Firehose, and S3.
- AWS CLI installed and configured on your local machine.
- Python 3.x installed on your local machine.

## Setup

The requirements for this project are listed in the `requirements.txt` file. After setting up a `venv` to contain the project dependencies, you can install them using pip:

```bash
pip install -r requirements.txt
```

## Usage

After setting up the required resources in AWS, this script needs to be updated with the appropriate stream name and AWS region.

Look for the `STREAM_NAME` and `REGION` variables in the script and update them with your Kinesis Data Stream name and AWS region.

Once you have updated the script, you can run it to start generating and sending data to your Kinesis Data Stream:

```bash
python main.py
```

As written, the script will generate 100 events 0.2s apart and send them to the Kinesis Data Stream.

## Limitations

Since the script generates random data, it may not reflect real-world scenarios accurately. FOr example, you might see products being returned that were never purchased. The point of this script is to generate a sufficient volume of data with a reasonable structure to allow for a basic exploration of the cloud tools for ingesting, storing, and visualizing the streaming data. There are no expectations that the insights produced from this data will be meaningful or actionable, nor is it a focus of this demonstration. The visualizations eventually chosen are more for visual appeal and to demonstrated the capabilities of the tools rather than to produce meaningful insights.
