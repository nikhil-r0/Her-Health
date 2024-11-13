# Rural Women's Health Platform

Our project is a health-centric platform designed to connect rural women, local healthcare centers, and donors through real-time data and AI-driven support. This app and website provide essential features to assist women in tracking their health, give healthcare centers tools for early intervention, and enable donors to offer direct, verified support transparently.

While the frontend of the app is fully developed, the backend is still under construction. Currently, the app and website are best run locally to experience the available features, especially the chatbot.

## Features

### Women
- **Symptom and Cycle Tracking**: Allows women to monitor symptoms, medications, and menstrual cycles, enabling quicker and more accurate diagnoses.
- **Up-to-Date Health Information**: Provides reliable information on health concerns and preventive measures.
- **AI Health Assistant**: Gemini-based chatbot offering symptom guidance and early diagnosis suggestions to highlight possible severe cases, with personalized insights based on user health profiles.
- **Funding Requests**: Enables women to seek funds for serious health issues, facilitating continuous communication with local healthcare centers for immediate support.

### Healthcare Centers
- **Community Health Tracking**: Allows healthcare centers to monitor women within their locality, enabling early outreach to those showing severe symptoms.
- **AI-Based Diagnosis**: Assists in initial diagnoses and flags critical cases, ensuring timely intervention.
- **Funding Support**: Platform for healthcare centers to verify women’s health issues and request funds for treatment and equipment.

### Donors
- **Transparent Donation Platform**: Provides real-time data on funding needs, verified by local healthcare centers for clarity and transparency.
- **Detailed Fund Utilization**: Offers donors detailed reports on how and where their contributions are utilized, enhancing accountability.

## Project Structure and Under-Development Features

### Current Implementation
- Fully developed frontend for both the mobile app and website.
- Chatbot using a Gemini model to provide preliminary medical guidance.
- Basic Firebase Firestore integration for storing health profiles and symptoms data.
- Cycle tracking module with an intuitive calendar view and health profile entry.

### To-Do List
1. **Backend Deployment**:
   - Set up Firebase backend for user data persistence, with authentication, Firestore database, and storage.
   - Deploy Flask API for processing chatbot interactions, connected to the app’s Firebase database.

2. **Enhanced Authentication and User Management**:
   - Implement secure Firebase Authentication for user accounts and access control.
   - Expand user database integration for tracking health profiles, login status, and health data securely.

3. **AI Model Improvements**:
   - Optimize the chatbot’s response accuracy and speed, incorporating user-specific health data to refine suggestions.
   - Add follow-up question prompts based on the initial input and health profile.

4. **Healthcare and Donor Features**:
   - Develop a robust backend to support healthcare centers with patient management tools, enabling early intervention and improved patient outcomes.
   - Complete the donor dashboard with real-time updates, enabling transparent fund allocation, tracking, and reporting.

5. **Web App Deployment**:
   - Deploy the website to a production environment, linking the donor, healthcare, and patient interfaces with Firebase for real-time updates.

6. **Testing and QA**:
   - Comprehensive testing of all backend integrations, user workflows, and UI elements.
   - Establish a framework for Quality Assurance testing to ensure smooth functionality and bug resolution.

## Future Potential
This project is envisioned to transform how rural communities access healthcare by:
- Enabling healthcare centers to leverage AI for early diagnoses and resource allocation.
- Offering a single, trustworthy platform for donors to support rural health initiatives directly.
- Bringing critical health information and funding opportunities to rural women who otherwise face limited healthcare access.

As development progresses, we aim to integrate additional data visualization tools for donors, enhance diagnostic accuracy, and explore partnerships with healthcare NGOs and rural clinics for extended reach.

## Running the Project Locally
Due to ongoing backend development, please run the app locally with the following steps:
1. Clone this repository.
2. Install all dependencies (`npm install` or `yarn install`).
3. Start the local server and mobile app.
4. Ensure Firebase and Flask API connections are correctly configured.

Contributions and feedback are welcome as we continue building out this impactful project!
