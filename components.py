from diagrams import Cluster, Diagram
from diagrams.aws.network import VPC
from diagrams.aws.network import PrivateSubnet
from diagrams.aws.network import PublicSubnet
from diagrams.aws.network import ELB
from diagrams.aws.network import NATGateway
from diagrams.aws.security import ACM
from diagrams.aws.network import Route53
from diagrams.aws.compute import AutoScaling
from diagrams.aws.compute import EC2
from diagrams.k8s.network import Ingress
from diagrams.k8s.network import Service
from diagrams.k8s.compute import Pod
from diagrams.onprem.iac import Terraform
from diagrams.onprem.ci import GitlabCI
from diagrams.aws.storage import S3

with Diagram("EKS Cluster", show=False, direction="LR"):
    ssl_certificate = ACM("SSL cert")
    dns_name = Route53("DNS domain")
    load_balancer = ELB("Load balancer")
    with Cluster("Custom VPC"):
        with Cluster("Public network"):
            public_subnets = [
                PublicSubnet("Subnet zone a"),
                PublicSubnet("Subnet zone b"),
                PublicSubnet("Subnet zone c"),
                PublicSubnet("Subnet zone d"),
                ]
        nat_gateway = NATGateway("NAT gateway")
        with Cluster("Private network"):
            private_subnets = [
                PrivateSubnet("Subnet zone a"),
                PrivateSubnet("Subnet zone b"),
                PrivateSubnet("Subnet zone c"),
                PrivateSubnet("Subnet zone d"),
                ]
            with Cluster("Kubernetes cluster"):
                autoscaling_group = AutoScaling("Autoscaling group")
                autoscaling_group_instances = [
                    EC2("K8s worker zone a"),
                    EC2("K8s worker zone b"),
                    EC2("K8s worker zone c"),
                    EC2("K8s worker zone d"),
                ]
                ingress = Ingress("Ingress gateway")
                services = Service("Services")
                pods = Pod("Container pods")

    ci_pipeline = GitlabCI("CI pipeline")
    terraform_repo = Terraform("Infra as code")
    remote_state = S3("Remote state")

    ssl_certificate - dns_name
    dns_name - load_balancer
    load_balancer - public_subnets
    public_subnets - nat_gateway
    nat_gateway - private_subnets
    private_subnets - autoscaling_group
    autoscaling_group - autoscaling_group_instances
    autoscaling_group_instances - ingress
    ingress - services
    services - pods
    ci_pipeline - terraform_repo
    terraform_repo - remote_state
