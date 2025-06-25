# Miki-Bank-App

The Mikis Banking App is a secure, modern mobile application built using React Native for the frontend and Flask (Python) for the backend API. This full-stack project simulates a real-world mobile banking experience, offering users a seamless way to manage their accounts, perform transactions, and view financial history—right from their phone.

Designed for performance and scalability, the app uses secure API calls, local + cloud storage, and responsive layouts based Figma designs. 

User Authentication: JWT-secured login and registration

Account Dashboard: View multiple accounts and real-time balances

Transactions: Deposit, withdraw, and transfer between accounts

History Log: Scrollable list of transactions

UI Mode: Responsive layout, dark/light theme toggle

API-Driven: All logic (auth, money handling) runs on a Python backend

Layer	Tech Used	Version / Notes
Frontend	React Native	Expo or CLI (your choice)
Design	Figma	For prototyping screens and flows
State Mgmt	React Context / Redux	Manages auth and app state
Backend	Flask (Python)	REST API for all data and auth
Database	SQLite / PostgreSQL	Stores users, accounts, and transactions
Auth	JWT (PyJWT)	Secure user sessions
API Comm	Axios (React Native)	Frontend ↔ Backend via HTTP
Deployment	Render / Fly.io / Railway	Deploy Flask backend
Testing	Postman + Jest	API and UI testing
Versioning	Git + GitHub	For source control and collaboration
