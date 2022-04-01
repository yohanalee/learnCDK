from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as ddb,
)
from constructs import Construct


class LearnCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_ddb_table = ddb.Table(
            self,
            "MyDDBTbl",
            partition_key=ddb.Attribute(name="id", type=ddb.AttributeType.STRING),
        )

        my_lambda = _lambda.Function(
            self,
            "MyLambda",
            code=_lambda.Code.from_asset("lambda"),
            handler="hello.handler",
            runtime=_lambda.Runtime.PYTHON_3_7,
            environment={"DDB_TABLE_NAME": my_ddb_table.table_name},
        )
        my_ddb_table.grant_read_write_data(my_lambda)

        apigw.LambdaRestApi(self, "myapi", handler=my_lambda)
