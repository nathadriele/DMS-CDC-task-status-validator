import boto3
import requests
from mage_ai.data_preparation.shared.secrets import get_secret_value
from mage_ai.data_preparation.decorators import data_loader, test

DMS_REGION = 'us-east-1'
NOTIFIER_URL = 'https://api.notifier.engineering.test.com/events'

# Dictionary of tasks and their ARNs.
TASKS = {
    'task-DMS-CDC-1': 'arn:aws:dms:cdc-1',
    'task-DMS-CDC-2': 'arn:aws:dms:cdc-2',
    'task-DMS-CDC-3': 'arn:aws:dms:cdc-3',
    'task-DMS-CDC-4': 'arn:aws:dms:cdc-4',
    'task-DMS-CDC-5': 'arn:aws:dms:cdc-5',
}

def get_dms_client():
    """Initialize and return a boto3 DMS client."""
    return boto3.client(
        'dms',
        aws_access_key_id=get_secret_value('aws_access_key_id'),
        aws_secret_access_key=get_secret_value('aws_secret_access_key'),
        region_name=DMS_REGION
    )

@data_loader
def load_data(*args, **kwargs):
    client = get_dms_client()
    results = []
    
    for task_name, task_arn in TASKS.items():
        try:
            client.describe_replication_tasks(Filters=[
                {'Name': 'replication-task-arn', 'Values': [task_arn]}
            ])
        except client.exceptions.ResourceNotFoundFault:
            print(f"{task_name}: Replication task not found")
            results.append((task_name, 'Replication task not found'))
            continue
        
        validation_details = client.describe_table_statistics(
            ReplicationTaskArn=task_arn
        )

        has_error = any(
            table_stat['ValidationState'] != 'Validated'
            for table_stat in validation_details['TableStatistics']
        )

        event_name = f"{task_name} dms mage"
        status = "Failed" if has_error else "Validated"
        
        response = requests.post(
            NOTIFIER_URL,
            json={'name': event_name, 'status': status}
        )
        response.raise_for_status()  # Ensure request was successful

        print(f"{task_name}: Status {status}!")
        results.append((task_name, status))
    
    return results

@test
def test_output(output, *args):
    assert output is not None, 'The output is undefined'
    assert isinstance(output, list), 'The output should be a list'
    for item in output:
        assert isinstance(item, tuple), 'Each item in the output list should be a tuple'
        assert len(item) == 2, 'Each tuple should contain two elements: task name and status message'
