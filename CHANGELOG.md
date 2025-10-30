# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

- Adapt to an official version of the async clients for the [AWS SDK for Python](https://github.com/awslabs/aws-sdk-python/tree/develop) when the experimental one becomes official.
- [developer experience] Easier custom tool extension (through some framework)

## [0.1.5] - 2024-10-30

- Upgraded from aws_sdk_bedrock_runtime 0.0.2 to 0.1.1
- The new SDK version improved resource utilization which was a key issue for many users (see: https://github.com/awslabs/aws-sdk-python/issues/11)! You should see decreased CPU load with a bidirectional stream open. 🎉
- Removed old workaround for lack of ContainerCredentialsResolver which involved a lambda restarting tasks every 5 hours. 
- The new code dynamically picks between ContainerCredentialsResolver and EnvironmentCredentialsResolver depending on whether you are running the application locally or with backend deployed on ECS.
- Fixed bug where running locally would lead to a no region found error when initializing boto3 clients for the knowledge base search or user lookup tool


## [0.1.4] - 2024-10-23 (hotfix)

- Pinned AWS Smithy SDK dependencies to specific versions to prevent breaking changes from experimental 0.1.0 packages (`smithy-core==0.0.2`, `aws-sdk-signers==0.0.3`, `aws_sdk_bedrock_runtime==0.0.2`, `smithy-aws-core==0.0.3`, `smithy-http==0.0.1`, `smithy-json==0.0.1`, `smithy-aws-event-stream==0.0.1`)

See https://github.com/aws-samples/sample-sonic-cdk-agent/pull/36 for PR and https://github.com/aws-samples/sample-sonic-cdk-agent/issues/34 for issue

## [0.1.3] - 2025-05-22

- [developer experience] Tools are now defined using the popular Model Context Protocol (MCP) framework.

Integrated with the widely-adopted MCP standard for tool definitions, making it easier to share and reuse tools across different AI applications and environments.

## [0.1.3] - 2025-04-25

- [developer experience] You can now locally develop both frontend and backend before you deploy.

Iterating through tool addition and UI changes takes time to verify when you need to run ./deploy.sh every time for even the small changes. Now you don't have to wait for the deployment! Simply run `npm run dev` on the project root to spin up the frontend server that talks to the local backend container.

See https://github.com/aws-samples/sample-sonic-cdk-agent/issues/19 with an awesome PR: https://github.com/aws-samples/sample-sonic-cdk-agent/pull/20 for more details.

## [0.1.2] - 2025-04-20

- [bug fix] Tool use works after 6 hours.

Tool use stopped working after 6 hours due to AWS credential expiration. Because the bug fix for the experimental uses environment variables, the regular boto3 credential refresh with container metadata service stopped working. As a temporary solution, ECS tasks are stopped (and restarted) every 5 hours.

This change disrupts the backend connection every 5 hours, but we chose this simpler fix over a custom credentials retrieval logic that bloats the backend logic that makes it harder to add tools. This temporary fix will be removed after the experimental Python SDK becomes official. See https://github.com/aws-samples/sample-sonic-cdk-agent/pull/17 for details.

## [0.1.1] - 2025-04-16

- [bug fix] Sample application works after 6 hours.

Backend stopped working after 6 hours due to AWS credential expiration. The experimental Python SDK does not handle this credential refresh natively yet, so we built a manual credential fetching logic in the backend from the ECS role. See https://github.com/aws-samples/sample-sonic-cdk-agent/pull/8 for details.

- [developer experience] ECS logs don't contain confusing errors from NLB health checks.

NLB health checks sent empty TCP packets for health checks and the backend WebSocket process kept outputting logs so much every minute. It was hard to find the right logs for your tool invocation and build on top of this sample. Now, it contains essential logs only. See https://github.com/aws-samples/sample-sonic-cdk-agent/pull/9 for details.

- [chore] Updated outdated dependencies

## [0.1.0] - 2025-04-09

- Initial version released.
