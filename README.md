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

