# aws-cdk-demo

### Description
This demo is used to show the basic usage of aws cdk with Python (>=3.6) on a Linux or MacOs platform. Initially, the project includes VPC creation.

### Preparation
The demo assumes that you've already configured AWS CLI and AWS Credentials.
See [AWS Command Line Interface installation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) for details.

And also the node.js is required (The AWS CDK uses Node.js (>= 8.12.0)), see [nodejs website](https://nodejs.org/) for details.

To check your node.js version:
```
node --version
```

The version need to be >= 8.12.0:
```
v8.12.0
```

Install the required aws cdk toolkit packages via npm:
```
npm install -g aws-cdk
```

To check your cdk version:
```
cdk --version
```


### Usage
First, activate the virtualenv for later actions:
```
source .env/bin/activate
```

Now install the required Python libraries:
```
pip install -r requirements.txt
```

Install the aws_cdk.aws_ec2 for VPC demo:
```
pip install aws_cdk.aws_ec2
```

Check the cdk application:
```
cdk ls
```

Now synthesize the stack:
```
cdk synth vpc
```

To set up the VPC with defalut parameters, with cidr 10.0.0.0/16 and 1 public subnet and 1 private subnet per AZ:
```
cdk deploy
```

To set up the VPC with custom parameters (VPC cidr and max deployed subnet/AZ):
```
cdk deploy -c cidr=12.0.0.0/16 -c azs 1
```

### Note:
- The default AWS region used is us-east-2.

- Now the actual max AZ taken effect is 2, even you set it much more tha 2 (like 99). Might be the issue for aws-cdk Python.
