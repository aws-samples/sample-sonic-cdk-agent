#!/usr/bin/env python3

#
# Copyright 2025 Amazon.com, Inc. and its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#   http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
#

import os
import boto3
from botocore.exceptions import NoCredentialsError


def get_aws_region():
    """
    Get AWS region from multiple sources in order of preference:
    1. AWS_REGION environment variable
    2. AWS_DEFAULT_REGION environment variable  
    3. boto3 session default region
    4. Fall back to us-east-1
    
    Returns:
        str: AWS region name
    """
    # Check environment variables first
    region = os.environ.get('AWS_REGION')
    if region:
        return region
        
    region = os.environ.get('AWS_DEFAULT_REGION')
    if region:
        return region
    
    # Try to get from boto3 session
    try:
        session = boto3.Session()
        region = session.region_name
        if region:
            return region
    except (NoCredentialsError, Exception):
        pass
    
    # Fall back to us-east-1 (same as your main app)
    return "us-east-1"


def create_boto3_client(service_name, **kwargs):
    """
    Create a boto3 client with automatic region detection.
    
    Args:
        service_name (str): AWS service name (e.g., 'dynamodb', 'bedrock-agent-runtime')
        **kwargs: Additional arguments to pass to boto3.client()
    
    Returns:
        boto3 client object
    """
    if 'region_name' not in kwargs:
        kwargs['region_name'] = get_aws_region()
    
    return boto3.client(service_name, **kwargs)


def create_boto3_resource(service_name, **kwargs):
    """
    Create a boto3 resource with automatic region detection.
    
    Args:
        service_name (str): AWS service name (e.g., 'dynamodb')
        **kwargs: Additional arguments to pass to boto3.resource()
    
    Returns:
        boto3 resource object
    """
    if 'region_name' not in kwargs:
        kwargs['region_name'] = get_aws_region()
    
    return boto3.resource(service_name, **kwargs)