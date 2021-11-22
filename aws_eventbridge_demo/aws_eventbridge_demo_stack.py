import aws_cdk.core as cdk # pylint: disable=import-error 
import aws_cdk.aws_events as events # pylint: disable=import-error 
import aws_cdk.aws_logs as logs # pylint: disable=import-error 
import aws_cdk.aws_events_targets as targets    # pylint: disable=import-error 

class AwsEventbridgeDemoStack(cdk.Stack):
    """
    sample stack
    """
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _eventBus = events.EventBus(self, id="demo-event-bus", event_bus_name="samplebus")
        _logGroup = logs.LogGroup(self, id="demologgroup", log_group_name="testloggroup")
        testRule = events.Rule(self, id="testrule", description="test", event_bus=_eventBus, event_pattern={"source":["test"]})
        testRule.add_target(target=targets.CloudWatchLogGroup(log_group=_logGroup))



        
