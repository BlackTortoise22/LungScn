USE lungscan_db;

-- Default Admin

INSERT INTO users
(full_name,email,password,role,phone)

VALUES

(
'System Administrator',
'admin@lungscan.com',
'$2b$12$radawnel1Qy1/E55RrhaQ.LR/8KLneniXv/h1/5skoy5sGEZLq7nS',
'Admin',
'9999999999'
);

-- Default Doctor

INSERT INTO users
(full_name,email,password,role,phone)

VALUES

(
'Dr. John Smith',
'doctor@lungscan.com',
'$2b$12$radawnel1Qy1/E55RrhaQ.LR/8KLneniXv/h1/5skoy5sGEZLq7nS',
'Doctor',
'8888888888'
);