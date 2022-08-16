import aws_cdk as core
import aws_cdk.assertions as assertions

from multus_on_eks.multus_on_eks_stack import MultusOnEksStack

# example tests. To run these tests, uncomment this file along with the example
# resource in multus_on_eks/multus_on_eks_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MultusOnEksStack(app, "multus-on-eks")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
