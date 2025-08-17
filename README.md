# Big Data Project Master's

## Introduction
This project was carried out during an Erasmus exchange for the master’s course in Big Data.  
The main idea was to simulate working with a large-scale environment. Even though the dataset itself was not enormous, we built the project in a way that remains scalable.  
We used a virtual machine to simulate data ingestion (hypothetically streamlined — in practice, the CSV was uploaded to the VM).  
The main tools applied were **Spark, Hadoop HDFS, MongoDB, and Scikit-learn**.

## Accessing the Virtual Machine
We connected to the VM via SSH using a private key provided for the course.  
Typical steps included:
1. SSH into the VM (port 2222, user `ubuntu`).  
2. Activate the environment.  
3. Start Jupyter Notebook inside the VM.  

## Project Workflow
We worked with a CSV dataset and tested several hypotheses (see below).  
The workflow was as follows:
1. Ingest CSV into the VM.  
2. Store the data in **HDFS**.  
3. Perform cleaning and preprocessing with Spark.  
4. Save the cleaned data into MongoDB as JSON (our “fridge” for ready-to-use data).  
5. Run analyses and experiments using HDFS as a sandbox (our “cooking pan”).  

A full diagram is available in `schema.png`.

## Dataset
The dataset comes from Kaggle (“OkCupid”).  
Link: https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles
It contains about 60k profiles with both structured attributes (age, sex, ethnicity, etc.) and unstructured text (personal descriptions).  
During preprocessing, we concatenated the text fields for analysis.

## Hypotheses
- **Hypothesis 1:** Women write longer profile descriptions than men → PySpark  
- **Hypothesis 2:** Homosexual and bisexual people mention artistic activities more often → PySpark + keyword search  
- **Hypothesis 3:** Women mention wanting children more often than men → MongoDB + MapReduce  
- **Hypothesis 4:** People with higher education identify less often with organized religions → MongoDB + MapReduce / Aggregation  

The minimalistic presentation with the result is attached - "presentation".