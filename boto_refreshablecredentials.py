import botocore, boto3, datetime
from botocore.session import get_session

accounts = [
    {"name": "Account1", "id": "123456789000"},
    {"name": "Account2", "id": "987654321000"}
]

regions = [ "us-east-1", "us-east-2" ]

# Replace myRole with your local named profile
boto3.setup_default_session(profile_name='myRole')

# 3600 seconds in an hour, this value should match your role's
# maximum session duration (AWS default is 1 hour).
def refresh_external_credentials():
    # Assume role, get details
    client = boto3.client('sts')
    credentials = client.assume_role(
        RoleArn=roleArn,
        RoleSessionName="thisNameMattersNot",
        DurationSeconds=3600
    ).get("Credentials")
    return {
        "access_key": credentials.get('AccessKeyId'),
        "secret_key": credentials.get('SecretAccessKey'),
        "token": credentials.get('SessionToken'),
        "expiry_time": credentials.get('Expiration').isoformat()
    }

roleArn = ''

for account in accounts:
    id = account.get('id')
    accountName = account.get('name')
    
    # Replace roleToAssume with your target role
    roleArn = 'arn:aws:iam::' + str(id) + ':role/roleToAssume'
    
    credentials = botocore.credentials.RefreshableCredentials.create_from_metadata(
        metadata=refresh_external_credentials(),
        refresh_using=refresh_external_credentials,
        method="sts-assume-role",
    )
    
    for region in regions:
        session = get_session()
        session._credentials = credentials
        session.set_config_variable("region", region)
        autorefresh_session = boto3.session.Session(botocore_session=session)
        
        # Your boto3 calls, for example...
        rds = autorefresh_session.client('rds')
        databases = rds.describe_db_instances()
        
        # ...
