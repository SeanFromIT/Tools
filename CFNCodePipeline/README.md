# CFN Code Pipeline:
A CodePipeline for CloudFormation (CFN) deployment. The pipeline lives in your non-prod account, and upon manual approvals could deploy to both your non-prod and prod accounts.

Assumptions:
* You have two AWS accounts (denoted here as non-prod and prod)
* You like manual gates in your pipeline
* You are using CodeCommit as the repo for your CFN and it lives in the non-prod account. (You could easily adapt this for S3 as source instead.)

Instructions:
1. One time, run “1 NPCPKMSKey.yaml” in non-prod account to create the KMS encryption key. Note the output.
2. One time, run “ProdPipelineRoles.yaml” in prod account to create the necessary roles. It will require the output from step 1. Note the outputs again.
3. For each CFN you want to run through a pipeline, deploy “NPCFNCodePipeline.yaml” in non-prod account and give it details about the CodeCommit repo and filenames. It will also require the outputs from step 2.

Notes:
* It’s setup so all manual approvals go to the same email distro. That can be easily changed and/or broken apart non-prod/prod if desired.
* KMS, and specifically the Deny statements on the S3 artifact bucket, are required for cross-account CodePipeline deployments.