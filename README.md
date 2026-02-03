# Job Applications Dashboard – Google Cloud
Project Overview

The Job Applications Dashboard is a centralized platform designed to help users efficiently manage and track their job applications. The system automatically fetches job-related emails from Gmail, including application confirmations, interview schedules, assessments, and rejection notifications. By consolidating this information into a single dashboard, the application provides users with clear visibility into their job search progress.

Built using Google Cloud services, the dashboard ensures scalability, security, and reliable data processing while reducing the manual effort involved in tracking applications.

1. Features

- Automatic retrieval of job-related emails from Gmail
- Classification of emails into applications, interviews, assessments, and rejections
- Visual summary of job application status
- Detailed tabular view of all applications
- Centralized tracking of job search progress
- User-friendly dashboard for efficient job hunt management

2. Technologies Used
- Cloud Platform: Google Cloud Platform (GCP)
- Email Integration: Gmail API
- Backend: Python / Node.js
- Frontend: HTML, CSS, JavaScript
- Data Processing: Cloud Functions / Cloud Run
- Database: Firestore / Cloud SQL

3. How It Works
- The user grants permission to access Gmail using secure OAuth authentication
- The system scans incoming and existing emails for job-related content
- Emails are categorized based on keywords and patterns
- Application data is stored and updated in the database
- The dashboard displays visual summaries and a detailed application table

4. Use Cases
Tracking multiple job applications in one place
Monitoring interview and assessment updates
Reducing manual job application tracking
Improving job search organization and productivity

5.Future Enhancements
AI-based email classification for higher accuracy
Resume-to-job application linking
Deadline reminders and notification alerts
Analytics on application success rates
Support for multiple email accounts
