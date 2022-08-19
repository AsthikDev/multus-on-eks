#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import Tags

from stacks.back_end.vpc_stack import VpcStack

from stacks.back_end.eks_cluster_stacks.eks_cluster_stack import EksClusterStack
from stacks.back_end.eks_cluster_stacks.eks_ssm_daemonset_stack.eks_ssm_daemonset_stack import EksSsmDaemonSetStack

app = cdk.App()

stack_uniqueness = f"001"


# VPC Stack for hosting Secure workloads & Other resources
vpc_stack = VpcStack(
    app,
    # f"{app.node.try_get_context('project')}-vpc-stack",
    f"eks-cluster-vpc-stack-{stack_uniqueness}",
    stack_log_level="INFO",
    description="Miztiik Automation: Custom Multi-AZ VPC"
)

# EKS Cluster to host multus containers
eks_cluster_stack = EksClusterStack(
    app,
    f"eks-cluster-stack-{stack_uniqueness}",
    stack_log_level="INFO",
    stack_uniqueness=stack_uniqueness,
    vpc=vpc_stack.vpc,
    description="Miztiik Automation: EKS Cluster to host multus containers"
)
# Bootstrap EKS Nodes with SSM Agents
ssm_agent_installer_daemonset = EksSsmDaemonSetStack(
    app,
    f"ssm-agent-installer-daemonset-stack-{stack_uniqueness}",
    stack_log_level="INFO",
    eks_cluster=eks_cluster_stack.eks_cluster_1,
    description="Miztiik Automation: Bootstrap EKS Nodes with SSM Agents"
)

# Stack Level Tagging
_tags_lst = app.node.try_get_context("tags")

if _tags_lst:
    for _t in _tags_lst:
        for k, v in _t.items():
            Tags.of(app).add(
                k, v, apply_to_launched_instances=True, priority=300)


app.synth()
