import boto3

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
    event_push(eb_client, item['color'], item)
