# ToDo

To fix the error of _Unable to view cluster resources in AWS Console and you receive an error in the AWS Management Console_,

1. Setup Cluster Role and Rolebinding and Group using the Yaml[1]
1. In `kube-system` namespace update `configmap/aws-auth` to add your role 
1. ```json
    {
    "rolearn": "arn:aws:iam::111122223333:role/ROLE_NAME",
    "username": "arn:aws:iam::111122223333:role/ROLE_NAME",
    "groups": [
      "system:bootstrappers",
      "system:nodes",
      "eks-console-dashboard-full-access-group"
    ]
    }
   ```


### 👋 Buy me a coffee

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Q5Q41QDGK) Buy me a [coffee ☕][900].

### 📚 References

1. [AWS Docs: EKS Get Console Access to Cluster Resources][1]
1. [AWS Support: EKS Object Access Error][2]
2. [AWS Support: EKS Troubleshooting IAM][3]

### 🏷️ Metadata

![miztiik-success-green](https://img.shields.io/badge/Miztiik:Automation:Level-200-blue)

**Level**: 200

[1]: https://docs.aws.amazon.com/eks/latest/userguide/view-kubernetes-resources.html#view-kubernetes-resources-permissions
[2]: https://aws.amazon.com/premiumsupport/knowledge-center/eks-kubernetes-object-access-error/
[3]: https://docs.aws.amazon.com/eks/latest/userguide/troubleshooting_iam.html
[100]: https://www.udemy.com/course/aws-cloud-security/?referralCode=B7F1B6C78B45ADAF77A9
[101]: https://www.udemy.com/course/aws-cloud-security-proactive-way/?referralCode=71DC542AD4481309A441
[102]: https://www.udemy.com/course/aws-cloud-development-kit-from-beginner-to-professional/?referralCode=E15D7FB64E417C547579
[103]: https://www.udemy.com/course/aws-cloudformation-basics?referralCode=93AD3B1530BC871093D6
[899]: https://www.udemy.com/user/n-kumar/
[900]: https://ko-fi.com/miztiik
[901]: https://ko-fi.com/Q5Q41QDGK
