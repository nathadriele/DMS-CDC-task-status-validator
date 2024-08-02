## DMS CDC Task Status Validator

### Introduction

This project, developed using Mage.ai, aims to validate the status of AWS Database Migration Service (DMS) Change Data Capture (CDC) tasks. At the time of its creation, there was no existing monitoring solution for the status of these tasks. This code periodically checks the validation status of the CDC tasks and sends notifications if any issues are detected.
- **Mage.ai** is a data pipeline tool that enables rapid development, testing, and deployment of data processing workflows.
- **AWS DMS** is a service designed to simplify the process of migrating databases to AWS. One of its key features, **Change Data Capture (CDC)**, allows the continuous replication of changes from a source database to a target database in near real-time. This is particularly useful for maintaining data consistency and ensuring that the target database remains synchronized with the source.

### Overview

This project provides a solution to monitor and validate the status of AWS DMS CDC tasks. The script checks the status of each specified CDC task and sends notifications via an HTTP API if any validation issues are detected.

### Problem Description

The primary challenge addressed by this project is the lack of monitoring for AWS DMS CDC tasks. Without proper monitoring, any issues with the replication tasks could go unnoticed, potentially leading to data inconsistencies or loss.

### Objective

The objective of this project is to automate the monitoring of AWS DMS CDC tasks, validate their status, and notify the responsible team if any tasks are not in a validated state. This ensures that any issues are promptly addressed, maintaining data integrity and synchronization.

### Prerequisites

- `AWS` account with necessary permissions for DMS and Secrets Manager.
- `Mage.ai` installed and configured.
- `boto3` and requests libraries installed in your Python environment.

### Installation

1. Clone the repository:

```py
git clone https://github.com/yourusername/aws-dms-cdc-validator.git
cd aws-dms-cdc-validator
```

2. Install required Python libraries:

```py
pip install boto3 requests
```

### Code Explanation

#### Imports and Setup

The code begins by importing necessary libraries and setting up the AWS client. The boto3 library is used for interacting with AWS services, and requests is used for making HTTP requests to send notifications.

#### Configuration of Logging

Logging is configured to capture and display information about the process, including any errors encountered.

#### Data Loader Function

The load_data function is the core of the script. It retrieves the necessary AWS credentials using the get_secret_value function and initializes the DMS client.

### Validation Logic

The script iterates over each task, checks its replication status, and validates the table statistics. If any table is not validated, an error flag is set.

### Notification

Based on the validation results, the script sends notifications via an HTTP POST request. If validation errors are found, a failure notification is sent; otherwise, a success notification is sent.

### Testing

The `test_output` function is used to ensure that the load_data function produces a defined output, aiding in validation during development.

### Contribution to Data Engineering

This project automates the monitoring and validation of AWS DMS CDC tasks, a crucial aspect of maintaining data integrity and synchronization during database migrations. By providing automated notifications for validation issues, it ensures that data engineers are promptly informed of any problems, allowing for quick resolution and minimal disruption to data workflows.
