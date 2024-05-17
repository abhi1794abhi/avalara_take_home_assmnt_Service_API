# avalara_take_home_assmnt_Service_API
This exercise is your chance to show us how you would design a small JSON based API service. For this exercise, we need to develop a small service that will help our engineers schedule running jobs ensuring their runtimes do not overlap. Given two date ranges, this service should return a response letting the caller know if these ranges overlap.


# Date Overlap Service

This project implements a simple JSON-based API service to check if two date ranges overlap.

## API Endpoint

`POST /api/check_overlap`

### Request Body

```json
{
  "range1": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  },
  "range2": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
}


Deployment on AWS Elastic Beanstalk
Initialize Elastic Beanstalk application: eb init
Create environment: eb create
Deploy application: eb deploy
markdown
Copy code

### Deployment Steps on AWS

1. **Initialize Elastic Beanstalk Application**:
   - In your project directory, run:

     ```bash
     eb init -p python-3.9 date-overlap-service
     ```

   - Follow the prompts to configure your application and select your region.

2. **Create an Elastic Beanstalk Environment**:
   - Create an environment and deploy the application:

     ```bash
     eb create date-overlap-env
     ```

3. **Deploy Application**:
   - Deploy your application using:

     ```bash
     eb deploy
     ```

4. **Access Your Application**:
   - Once deployed, you can access your application using the URL provided by Elastic Beanstalk, typically in the format `http://<environment-name>.<region>.elasticbeanstalk.com`.

### Directory Structure

date-overlap-service/
├── date_overlap_service.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── Makefile
└── README.md



This setup should provide a robust foundation for deploying the date overlap service on AWS Elastic Beanstalk.
