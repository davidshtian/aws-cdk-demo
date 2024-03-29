#!/usr/bin/env python3

from aws_cdk import core

from vpc.vpc_stack import VpcStack


app = core.App()
VpcStack(app, "vpc", env={"region": "us-east-2"})

app.synth()
