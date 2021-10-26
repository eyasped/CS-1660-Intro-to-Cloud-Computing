#pip install boto3
import boto3

s3 = boto3.resource('s3',
                    aws_access_key_id='-----------',
                    aws_secret_access_key='----------------'
                    )
try:
    s3.create_bucket(Bucket='datacont-newbuck-eyas', CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'
    })
except Exception as e:
    print (e)

bucket = s3.Bucket("datacont-newbuck-eyas")
bucket.Acl().put(ACL='public-read')

body = open('C:/Users/jaspe/Desktop/Cloud_Computing/NoSQL_Database_Homework/files/exp1.csv', 'rb')
o = s3.Object('datacont-newbuck-eyas', 'exp1.csv').put(Body=body)
s3.Object('datacont-newbuck-eyas', 'exp1.csv').Acl().put(ACL='public-read')

dyndb = boto3.resource('dynamodb',
                       region_name='us-west-2',
                       aws_access_key_id='-----------------',
                       aws_secret_access_key='--------------------------'
                       )
try:
    table = dyndb.create_table(
        TableName='datat',
        KeySchema=[
            {
                'AttributeName': 'PartitionKey',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'RowKey',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PartitionKey',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'RowKey',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
except Exception as e:
    print (e)

    # if there is an exception, the table may already exist. if so...
    table = dyndb.Table("datat")

# wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName='datat')

print(table.item_count)

import csv

with open('C:/Users/jaspe/Desktop/Cloud_Computing/NoSQL_Database_Homework/files/experiments.csv', 'r', encoding='utf-8') as csvfile:
    csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
    for item in csvf:
        print (item)
        body = open('C:/Users/jaspe/Desktop/Cloud_Computing/NoSQL_Database_Homework/files/' + item[3], 'rb')
        s3.Object('datacont-newbuck-eyas', item[3]).put(Body=body)
        md = s3.Object('datacont-newbuck-eyas', item[3]).Acl().put(ACL='public-read')
        url = " https://s3-us-west-2.amazonaws.com/datacont-eyas/" + item[3]
        metadata_item = {'PartitionKey': item[0], 'RowKey': item[1], 'description': item[4], 'date': item[2],
                         'url': url}
        try:
            table.put_item( Item = metadata_item)
        except:
            print("item may already be there or another failure")

response = table.get_item(
    Key={
        'PartitionKey': 'experiment3',
        'RowKey': '3'
    }
)
print('response: %r', response)
item = response['Item']
print(item)
response
