# Introduction to Google Cloud Dataproc
This file contains text you can copy and paste for the examples in Cloud Academy's _Introduction to Google Cloud Dataproc_ course.  

### Introduction
Google Cloud Platform Free Trial: https://cloud.google.com/free  

### Running a Simple Job
Jar file: file:///usr/lib/spark/examples/jars/spark-examples.jar  
Main class: org.apache.spark.examples.JavaWordCount  
Argument: gs://lesv-big-public-data/books/b1232  

### Scaling a Cluster
Jar file: file:///usr/lib/spark/examples/jars/spark-examples.jar  
Main class: org.apache.spark.examples.SparkPi  
Argument: 100000  
```
gcloud dataproc clusters create cluster2 --properties dataproc:dataproc.monitoring.stackdriver.enable=true
```

### Connecting to BigQuery
BigQuery Connector: https://cloud.google.com/dataproc/docs/connectors/bigquery#using_the_connector  
Github repo: https://github.com/cloudacademy/dataproc-intro.git  
```
cd dataproc-intro
export GCLOUD_PROJECT=<Project ID>
python natality.py
```
```
Main python file: gs://ca-dataproc/natality-ml.py
Jar files: gs://hadoop-lib/bigquery/bigquery-connector-hadoop2-latest.jar
```
### Customization
```
gcloud compute ssh --zone=<zone> \
--ssh-flag="-D 1080" --ssh-flag="-N" --ssh-flag="-n" <master node>
```
Proxy server: localhost:8088  

Cluster properties: https://cloud.google.com/dataproc/docs/concepts/cluster-properties  
Initialization actions: https://github.com/GoogleCloudPlatform/dataproc-initialization-actions  

### Conclusion
Cloud Dataproc documentation: https://cloud.google.com/dataproc/docs  
Cloud Academy community forums: http://cloudacademy.com/community  
Support: support@cloudacademy.com
