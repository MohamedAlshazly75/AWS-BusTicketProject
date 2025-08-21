# 🚌 Bus Ticket Booking System (Serverless on AWS)

A fully **serverless web application** for booking bus tickets online.\
This project demonstrates how to integrate **AWS Lambda**, **API
Gateway**, **DynamoDB**, and **S3** to build a scalable and
cost-efficient application.

------------------------------------------------------------------------

## 🚀 Features

-   Book bus tickets online with:
    -   Email
    -   Seat Number
    -   Ticket Type (Economy, Regular, VIP)
    -   Trip Details (From / To cities)
-   Serverless backend powered by **AWS Lambda**
-   Data storage in **DynamoDB**
-   Static frontend hosted in **S3**
-   API Gateway for communication between frontend & backend
-   Real-time confirmation message after booking

------------------------------------------------------------------------

## 🏗️ Architecture

    Frontend (HTML, CSS, JS) → S3 (Static Hosting)
                │
                ▼
          API Gateway (POST)
                │
                ▼
            AWS Lambda
                │
                ▼
           DynamoDB Table

------------------------------------------------------------------------

## 📂 Project Structure

    bus-ticket-project/
    │
    ├── frontend/
    │   └── index.html   # Web UI for booking tickets
    │
    ├── backend/
    │   └── lambda_function.py   # AWS Lambda function for handling requests
    │
    └── README.md

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1. DynamoDB

-   Create a table named **`BusTickets`**
-   Primary Key: `ticketID` (String)

### 2. Lambda Function

-   Create a new Lambda function in AWS Console (Python 3.12 runtime).

-   Upload `lambda_function.py` as a deployment package.

-   Attach an IAM Role with permission to write to DynamoDB.


### 3. API Gateway

-   Create a new **REST API**.
-   Add a resource `/`.
-   Create a **POST&GET method** integrated with the Lambda function.
-   Enable **CORS**.

### 4. Frontend (S3 Hosting)

-   Create an S3 bucket (enable static website hosting).
-   Upload `index.html` to the bucket.
-   Replace the `API_GATEWAY_URL` in `index.html` with your API
    endpoint.

------------------------------------------------------------------------

## 📸 Demo

-   User fills the booking form → Clicks **Submit**\
-   Backend (Lambda) stores booking details in DynamoDB\
-   User sees: **"Your booking is confirmed ✅ and TicketID"**
https://youtu.be/FxDFG_rqpY8
------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **AWS Lambda** (Serverless compute)
-   **Amazon API Gateway**
-   **Amazon DynamoDB**
-   **Amazon S3** (Static hosting)
-   **HTML, CSS, JavaScript**

------------------------------------------------------------------------

## 📜 License

This project is for **educational purposes** and can be extended for
real-world applications.
