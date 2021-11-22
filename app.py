#!/usr/bin/env python3
import boto3
import json

from aws_cdk import core as cdk # pylint: disable=import-error

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.

from aws_eventbridge_demo.aws_eventbridge_demo_stack import AwsEventbridgeDemoStack


app = cdk.App()
AwsEventbridgeDemoStack(app, "AwsEventbridgeDemoStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=core.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account='486610745382', region='us-east-1')

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()

# create events client
def event_push(client, detail_type, data):
    
    response=client.put_events(
        Entries=[
            {
                'Source': 'test',
                'DetailType': detail_type,
                'Detail': data,
                'EventBusName': "samplebus"
            }
        ]
    )

    return response

raw_payload=[
	{
		"color": "red",
		"value": "#f00"
	},
	{
		"color": "green",
		"value": "#0f0"
	},
	{
		"color": "blue",
		"value": "#00f"
	},
	{
		"color": "cyan",
		"value": "#0ff"
	},
	{
		"color": "magenta",
		"value": "#f0f"
	},
	{
		"color": "yellow",
		"value": "#ff0"
	},
	{
		"color": "black",
		"value": "#000"
	}
]

eb_client = boto3.client('events', region_name='us-east-1')

for item in raw_payload:
    event_push(eb_client, item['color'], json.dumps(item))
