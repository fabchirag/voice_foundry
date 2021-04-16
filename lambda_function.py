import boto3
import vanitynumber

"""boto3 library is used for interacting with AWS services"""
"""variable table is selecting a table from the dynamoDB"""
"""variable phone is selecting a event document in JSON"""
"""Vanity library has been installed and used to convert the toll-free number to vanity number"""
def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("phone_number")
    phone = event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
    print("phonenumber:", phone)
    try:
        if len(phone) == 14:
            print(f"Length: {len(phone)}, Number accepted: ", phone)
        table_entry = {"phonenumber": phone}
        i = 1
        sample = vanitynumber.all_wordifications(phone, 5)
        print(sample)
        for s in sample:
            table_entry["vanity" + str(i)] = s
            i = i + 1
        table.put_item(Item=table_entry)
    except ValueError:
        print(f"Length: {len(phone)}, Only 14 are allowed..")