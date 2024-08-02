## DMS-CDC-task-status-validator

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

  
