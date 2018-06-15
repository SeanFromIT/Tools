# API Gateway Lambda Proxy
A YAML CloudFormation (CFN) template to deploy your lambda code and standup an API Gateway integration to it. In this example, we are building an API that takes a URL of `/products/{id}` and takes action on it.

Note: This template uses S3 to store the code. If your lambda is written in node or python and less than 4096 characters, you can alternatively include it directly in your CFN using [ZipFile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-zipfile).

## Usage:
1. Create an S3 Bucket in the desired region to hold the python Lambda code. Note its name.
2. Create an IAM role with permission to execute lambda (VPC/ENI permissions not required) and interact with any other AWS services your lambda uses. Note its ARN.
3. Zip your code and store it in the bucket. For example, `zip -r myCode.zip index.py` and `aws s3 cp myCode.zip s3://myBucket/`
4. Use CloudFormation with `build.yaml`.

The proxy path parameter is passed to your `handler` function in the `event` argument. To get at it in python, for example: `event['pathParameters']['proxy']`. You can add additional resources to support other URL paths. Note that `{proxy+}` stands for any path parameter, we just happen to be using it for `{id}`.
