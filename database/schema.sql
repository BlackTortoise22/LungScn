-- LungScan Database Schema
-- Version : 1.0
-- Author : Team LungScan

CREATE DATABASE IF NOT EXISTS lungscan_db;
USE lungscan_db;

-- USERS TABLE

CREATE TABLE IF NOT EXISTS users (

    user_id INT AUTO_INCREMENT PRIMARY KEY,

    full_name VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL,

    role ENUM('Admin', 'Doctor') NOT NULL,

    phone VARCHAR(15),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP

);


-- PATIENTS TABLE

CREATE TABLE IF NOT EXISTS patients (

    patient_id INT AUTO_INCREMENT PRIMARY KEY,

    patient_code VARCHAR(20) NOT NULL UNIQUE,

    full_name VARCHAR(100) NOT NULL,

    age INT NOT NULL,

    gender ENUM('Male', 'Female', 'Other') NOT NULL,

    phone VARCHAR(15) NOT NULL,

    email VARCHAR(100),

    address TEXT,

    symptoms TEXT,

    registered_by INT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_patient_user
        FOREIGN KEY (registered_by)
        REFERENCES users(user_id)

);


-- XRAY SCANS TABLE

CREATE TABLE IF NOT EXISTS xray_scans (

    scan_id INT AUTO_INCREMENT PRIMARY KEY,

    patient_id INT NOT NULL,

    uploaded_by INT NOT NULL,

    image_name VARCHAR(255) NOT NULL,

    image_path VARCHAR(255) NOT NULL,

    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_scan_patient
        FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    CONSTRAINT fk_scan_user
        FOREIGN KEY (uploaded_by)
        REFERENCES users(user_id)

);

-- PREDICTIONS TABLE

CREATE TABLE IF NOT EXISTS predictions (

    prediction_id INT AUTO_INCREMENT PRIMARY KEY,

    scan_id INT NOT NULL,

    disease ENUM(
        'Normal',
        'Viral Pneumonia',
        'Bacterial Pneumonia',
        'Tuberculosis',
        'COVID-19'
    ) NOT NULL,

    confidence DECIMAL(5,2) NOT NULL,

    heatmap_path VARCHAR(255),

    explanation TEXT,

    model_version VARCHAR(50),

    predicted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_prediction_scan
        FOREIGN KEY (scan_id)
        REFERENCES xray_scans(scan_id)

);

-- REPORTS TABLE

CREATE TABLE IF NOT EXISTS reports (

    report_id INT AUTO_INCREMENT PRIMARY KEY,

    prediction_id INT NOT NULL,

    report_path VARCHAR(255) NOT NULL,

    generated_by INT NOT NULL,

    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_report_prediction
        FOREIGN KEY (prediction_id)
        REFERENCES predictions(prediction_id),

    CONSTRAINT fk_report_user
        FOREIGN KEY (generated_by)
        REFERENCES users(user_id)

);

-- LOGIN LOGS TABLE

CREATE TABLE IF NOT EXISTS login_logs (

    log_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    logout_time TIMESTAMP NULL,

    ip_address VARCHAR(45),

    CONSTRAINT fk_login_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)

);

-- INDEXES

CREATE INDEX idx_users_email
ON users(email);

CREATE INDEX idx_patients_code
ON patients(patient_code);

CREATE INDEX idx_patients_phone
ON patients(phone);

CREATE INDEX idx_predictions_disease
ON predictions(disease);