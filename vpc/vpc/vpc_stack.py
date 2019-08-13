from aws_cdk import (
    core,
    aws_ec2 as ec2
)


class VpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(self, "VPC", cidr=self.node.try_get_context("cidr"), subnet_configuration=[{"cidrMask": 24, "name": "ingress", "subnetType": ec2.SubnetType.PUBLIC}, {
                      "cidrMask": 24, "name": "application", "subnetType": ec2.SubnetType.PRIVATE}], max_azs=int(self.node.try_get_context("azs")))

        sg_public = ec2.SecurityGroup(
            self, "public", vpc=vpc, security_group_name="bytedance-public")

        sg_private = ec2.SecurityGroup(
            self, "private", vpc=vpc, security_group_name="bytedance-private")

        sg_public.add_ingress_rule(peer=ec2.Peer.ipv4("1.1.1.1/32"), connection=ec2.Port.tcp(
            8080), description="bytedance-public")

        sg_private.add_ingress_rule(peer=ec2.Peer.ipv4("2.2.2.2/32"), connection=ec2.Port.tcp(
            9090), description="bytedance-private")
