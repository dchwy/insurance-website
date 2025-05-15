Create Database if not EXISTS insurance_db;
Use insurance_db;
CREATE TABLE Customers
(
  CustomerID VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  PhoneNumber VARCHAR(255) NOT NULL,
  Gender VARCHAR(255) NOT NULL,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  DOB DATE NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Occupation VARCHAR(255) NOT NULL,
  MaritalStatus VARCHAR(255) NOT NULL,
  PRIMARY KEY (CustomerID)
);

CREATE TABLE InsuranceTypes
(
  InsuranceTypeID VARCHAR(255) NOT NULL,
  InsuranceName VARCHAR(255) NOT NULL,
  Description VARCHAR(255) NOT NULL,
  PolicyTerms VARCHAR(255) NOT NULL,
  PRIMARY KEY (InsuranceTypeID)
);

CREATE TABLE PersonIncharge
(
  PersonInchargeID VARCHAR(255) NOT NULL,
  PhoneNumber VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  PersonInchargeName VARCHAR(255) NOT NULL,
  Role VARCHAR(255) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  PRIMARY KEY (PersonInchargeID)
);

CREATE TABLE Assessor
(
  AssessorID VARCHAR(255) NOT NULL,
  AssessorName VARCHAR(255) NOT NULL,
  PhoneNumber VARCHAR(255) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  YearsOfExperience INT NOT NULL,
  PRIMARY KEY (AssessorID)
);

CREATE TABLE InsuranceContracts
(
  ContractID VARCHAR(255) NOT NULL,
  SignDate DATE NOT NULL,
  ExpirationDate DATE NOT NULL,
  EffectiveDate DATE NOT NULL,
  CustomerID VARCHAR(255) NOT NULL,
  InsuranceTypeID VARCHAR(255) NOT NULL,
  PersonInchargeID VARCHAR(255) NOT NULL,
  PRIMARY KEY (ContractID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (InsuranceTypeID) REFERENCES InsuranceTypes(InsuranceTypeID),
  FOREIGN KEY (PersonInchargeID) REFERENCES PersonIncharge(PersonInchargeID)
);

CREATE TABLE Payments
(
  PaymentID VARCHAR(255) NOT NULL,
  PaymentDate DATE NOT NULL,
  PaymentMethod VARCHAR(255) NOT NULL,
  Amount INT NOT NULL,
  PaymentStatus VARCHAR(255) NOT NULL,
  ContractID VARCHAR(255) NOT NULL,
  PRIMARY KEY (PaymentID),
  FOREIGN KEY (ContractID) REFERENCES InsuranceContracts(ContractID)
);

CREATE TABLE InsuranceClaim
(
  ClaimID VARCHAR(255) NOT NULL,
  ClaimDate DATE NOT NULL,
  ClaimStatus VARCHAR(255) NOT NULL,
  Amount INT NOT NULL,
  Description VARCHAR(255) NOT NULL,
  EventDate DATE NOT NULL,
  EventType VARCHAR(255) NOT NULL,
  PayoutMethod VARCHAR(255) NOT NULL,
  ContractID VARCHAR(255) NOT NULL,
  PRIMARY KEY (ClaimID),
  FOREIGN KEY (ContractID) REFERENCES InsuranceContracts(ContractID)
);

CREATE TABLE Beneficiaries
(
  BeneficiaryID VARCHAR(255) NOT NULL,
  FirstName VARCHAR(255) NOT NULL,
  Relationship VARCHAR(255) NOT NULL,
  PhoneNumber VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  DOB DATE NOT NULL,
  MaritalStatus VARCHAR(255) NOT NULL,
  Occupation VARCHAR(255) NOT NULL,
  Gender VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  PercentageOfBeneficiaries NUMERIC NOT NULL,
  ContractID VARCHAR(255) NOT NULL,
  PRIMARY KEY (BeneficiaryID),
  FOREIGN KEY (ContractID) REFERENCES InsuranceContracts(ContractID)
);

CREATE TABLE InsuredPerson
(
  InsuredID VARCHAR(255) NOT NULL,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  PhoneNumber VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  Gender VARCHAR(255) NOT NULL,
  DOB DATE NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Occupation VARCHAR(255) NOT NULL,
  MaritalStatus VARCHAR(255) NOT NULL,
  Relationship VARCHAR(255) NOT NULL,
  ContractID VARCHAR(255) NOT NULL,
  PRIMARY KEY (InsuredID),
  FOREIGN KEY (ContractID) REFERENCES InsuranceContracts(ContractID)
);

CREATE TABLE Assessments
(
  AssessmentID VARCHAR(255) PRIMARY KEY NOT NULL,
  AssessmentDate DATE NOT NULL,
  Result VARCHAR(255) NOT NULL,
  SeverityLevel VARCHAR(255) NOT NULL,
  ReviewDate DATE NOT NULL,
  AssessmentNotes VARCHAR(255) NOT NULL,
  ClaimID VARCHAR(255) NOT NULL,
  AssessorID VARCHAR(255) NOT NULL,
  FOREIGN KEY (ClaimID) REFERENCES InsuranceClaim(ClaimID),
  FOREIGN KEY (AssessorID) REFERENCES Assessor(AssessorID)
);

CREATE TABLE Payouts
(
  PayoutID VARCHAR(255) NOT NULL,
  Amount INT NOT NULL,
  PayoutDate DATE NOT NULL,
  PayoutStatus VARCHAR(255) NOT NULL,
  ClaimID VARCHAR(255) NOT NULL,
  PRIMARY KEY (PayoutID),
  FOREIGN KEY (ClaimID) REFERENCES InsuranceClaim(ClaimID)
);

INSERT INTO Customers (CustomerID, FirstName, LastName, Address, PhoneNumber, Gender, MaritalStatus, Email, DOB, Occupation)
VALUES
('CUS001', 'John', 'Doe', '123 Elm St', 1234567890, 'Male', 'Single', 'john.doe@example.com', '1985-02-15', 'Engineer'),
('CUS002', 'Jane', 'Smith', '456 Oak St', 2345678901, 'Female', 'Married', 'jane.smith@example.com', '1990-05-20', 'Teacher'),
('CUS003', 'Emily', 'Jones', '789 Pine St', 3456789012, 'Female', 'Single', 'emily.jones@example.com', '1987-08-25', 'Doctor'),
('CUS004', 'Michael', 'Brown', '101 Maple St', 4567890123, 'Male', 'Married', 'michael.brown@example.com', '1978-12-05', 'Lawyer'),
('CUS005', 'David', 'Williams', '202 Birch St', 5678901234, 'Male', 'Single', 'david.williams@example.com', '1992-03-10', 'Artist');

INSERT INTO InsuranceTypes (InsuranceTypeID, InsuranceName, Description, PolicyTerms)
VALUES
('IT001', 'Life Insurance', 'Covers life risks', 'Policy lasts for 20 years'),
('IT002', 'Health Insurance', 'Covers medical expenses', 'Policy lasts for 10 years'),
('IT003', 'Car Insurance', 'Covers vehicle damages', 'Policy lasts for 1 year'),
('IT004', 'Home Insurance', 'Covers property damage', 'Policy lasts for 5 years'),
('IT005', 'Travel Insurance', 'Covers travel risks', 'Policy lasts for 6 months');

INSERT INTO PersonIncharge (PersonInchargeID, PersonInchargeName, PhoneNumber, Address, Role, Email)
VALUES
('PI001', 'John Manager', 9876543210, '123 Elm St', 'Manager', 'john.manager@example.com'),
('PI002', 'Alice Manager', 8765432109, '456 Oak St', 'Manager', 'alice.manager@example.com'),
('PI003', 'Bob Supervisor', 7654321098, '789 Pine St', 'Supervisor', 'bob.supervisor@example.com'),
('PI004', 'Eve Assistant', 6543210987, '101 Maple St', 'Assistant', 'eve.assistant@example.com'),
('PI005', 'Grace Coordinator', 5432109876, '202 Birch St', 'Coordinator', 'grace.coordinator@example.com');

INSERT INTO Assessor (AssessorID, AssessorName, PhoneNumber, Email, YearsOfExperience)
VALUES
('A001', 'John Smith', '9876543210', 'john.smith@example.com', 10),
('A002', 'Jane Lee', '8765432109', 'jane.lee@example.com', 5),
('A003', 'David Kim', '7654321098', 'david.kim@example.com', 12),
('A004', 'Emma Brown', '6543210987', 'emma.brown@example.com', 8),
('A005', 'Michael Johnson', '5432109876', 'michael.johnson@example.com', 15);

INSERT INTO InsuranceContracts (ContractID, SignDate, ExpirationDate, EffectiveDate, CustomerID, InsuranceTypeID, PersonInchargeID)
VALUES
('C001', '2021-01-01', '2041-01-01', '2021-01-01', 'CUS001', 'IT001', 'PI001'),
('C002', '2021-02-01', '2031-02-01', '2021-02-01', 'CUS002', 'IT002', 'PI002'),
('C003', '2021-03-01', '2033-03-01', '2021-03-01', 'CUS003', 'IT003', 'PI003'),
('C004', '2021-04-01', '2034-04-01', '2021-04-01', 'CUS004', 'IT004', 'PI004'),
('C005', '2021-05-01', '2035-05-01', '2021-05-01', 'CUS005', 'IT005', 'PI005'),
('C006', '2021-06-01', '2036-06-01', '2021-06-01', 'CUS001', 'IT001', 'PI001'),
('C007', '2021-07-01', '2037-07-01', '2021-07-01', 'CUS002', 'IT002', 'PI002'),
('C008', '2021-08-01', '2038-08-01', '2021-08-01', 'CUS003', 'IT003', 'PI003'),
('C009', '2021-09-01', '2039-09-01', '2021-09-01', 'CUS004', 'IT004', 'PI004'),
('C010', '2021-10-01', '2040-10-01', '2021-10-01', 'CUS005', 'IT005', 'PI005');

INSERT INTO Payments (PaymentID, PaymentDate, PaymentMethod, Amount, PaymentStatus, ContractID)
VALUES
('P001', '2021-01-10', 'Credit Card', 500, 'Paid', 'C001'),
('P002', '2021-02-15', 'Debit Card', 400, 'Pending', 'C002'),
('P003', '2021-03-20', 'PayPal', 300, 'Paid', 'C003'),
('P004', '2021-04-10', 'Bank Transfer', 700, 'Pending', 'C004'),
('P005', '2021-05-01', 'Cheque', 200, 'Paid', 'C005'),
('P006', '2021-06-15', 'Credit Card', 150, 'Paid', 'C006'),
('P007', '2021-07-01', 'Debit Card', 450, 'Paid', 'C007'),
('P008', '2021-08-20', 'Bank Transfer', 600, 'Pending', 'C008'),
('P009', '2021-09-15', 'PayPal', 250, 'Paid', 'C009'),
('P010', '2021-10-05', 'Cheque', 350, 'Paid', 'C010');

INSERT INTO InsuranceClaim (ClaimID, ClaimDate, ClaimStatus, Amount, Description, EventDate, EventType, PayoutMethod, ContractID)
VALUES
('CL001', '2021-01-20', 'Approved', 2000, 'Car accident repair', '2021-01-19', 'Accident', 'Bank Transfer', 'C001'),
('CL002', '2021-02-25', 'Pending', 1500, 'Medical expenses', '2021-02-20', 'Health', 'Cheque', 'C002'),
('CL003', '2021-03-15', 'Rejected', 1000, 'Home damage', '2021-03-10', 'Home', 'Bank Transfer', 'C003'),
('CL004', '2021-04-10', 'Approved', 2500, 'Flood damage', '2021-04-05', 'Flood', 'PayPal', 'C004'),
('CL005', '2021-05-15', 'Pending', 2000, 'Fire damage', '2021-05-10', 'Fire', 'Cheque', 'C005'),
('CL006', '2021-06-10', 'Approved', 1800, 'Theft of personal items', '2021-06-05', 'Theft', 'Bank Transfer', 'C006'),
('CL007', '2021-07-20', 'Rejected', 1500, 'Broken windows', '2021-07-15', 'Accident', 'PayPal', 'C007'),
('CL008', '2021-08-10', 'Pending', 2200, 'Roof collapse', '2021-08-05', 'Accident', 'Bank Transfer', 'C008'),
('CL009', '2021-09-01', 'Approved', 1200, 'Medical surgery', '2021-08-25', 'Health', 'Cheque', 'C009'),
('CL010', '2021-10-10', 'Rejected', 1700, 'Car accident', '2021-10-05', 'Accident', 'PayPal', 'C010');

INSERT INTO Beneficiaries (BeneficiaryID, FirstName, LastName, Relationship, PhoneNumber, Occupation, MaritalStatus, DOB, Gender, Email, Address, PercentageOfBeneficiaries, ContractID)
VALUES
('B001', 'John', 'Doe', 'Spouse', 1234567890, 'Engineer', 'Married', '1985-02-15', 'Male', 'john.doe@example.com', '123 Elm St', 50.00, 'C001'),
('B002', 'Jane', 'Smith', 'Daughter', 2345678901, 'Student', 'Single', '2010-03-20', 'Female', 'jane.smith@example.com', '456 Oak St', 50.00, 'C002'),
('B003', 'Emily', 'Jones', 'Sister', 3456789012, 'Nurse', 'Single', '1995-01-10', 'Female', 'emily.jones@example.com', '789 Pine St', 50.00, 'C003'),
('B004', 'Michael', 'Brown', 'Father', 4567890123, 'Teacher', 'Married', '1970-11-10', 'Male', 'michael.brown@example.com', '101 Maple St', 50.00, 'C004'),
('B005', 'David', 'Williams', 'Brother', 5678901234, 'Artist', 'Single', '1992-03-10', 'Male', 'david.williams@example.com', '202 Birch St', 50.00, 'C005'),
('B006', 'Sarah', 'Miller', 'Wife', 6789012345, 'Doctor', 'Married', '1980-06-15', 'Female', 'sarah.miller@example.com', '303 Cedar St', 60.00, 'C006'),
('B007', 'Robert', 'Wilson', 'Friend', 7890123456, 'Software Developer', 'Single', '1990-04-25', 'Male', 'robert.wilson@example.com', '404 Willow St', 25.00, 'C007'),
('B008', 'Sophia', 'Moore', 'Daughter', 8901234567, 'Writer', 'Single', '1995-11-30', 'Female', 'sophia.moore@example.com', '505 Pine St', 50.00, 'C008'),
('B009', 'James', 'Taylor', 'Spouse', 9012345678, 'Chef', 'Married', '1980-02-18', 'Male', 'james.taylor@example.com', '606 Redwood St', 50.00, 'C009'),
('B010', 'Olivia', 'Anderson', 'Mother', 1234098765, 'Scientist', 'Married', '1988-09-14', 'Female', 'olivia.anderson@example.com', '707 Ash St', 50.00, 'C010');

INSERT INTO InsuredPerson (InsuredID, FirstName, LastName, PhoneNumber, Address, Gender, DOB, Email, Occupation, MaritalStatus, Relationship, ContractID)
VALUES
('I001', 'Mike', 'Johnson', 3456789012, '789 Pine St', 'Male', '1990-06-12', 'mike.johnson@example.com', 'Teacher', 'Single', 'Self', 'C001'),
('I002', 'Sara', 'Williams', 4567890123, '101 Maple St', 'Female', '1987-08-25', 'sara.williams@example.com', 'Doctor', 'Married', 'Spouse', 'C002'),
('I003', 'John', 'Doe', 5678901234, '202 Birch St', 'Male', '1985-02-15', 'john.doe@example.com', 'Engineer', 'Single', 'Self', 'C003'),
('I004', 'Emily', 'Jones', 6789012345, '303 Cedar St', 'Female', '1995-01-10', 'emily.jones@example.com', 'Nurse', 'Single', 'Sister', 'C004'),
('I005', 'Michael', 'Brown', 7890123456, '404 Willow St', 'Male', '1970-11-10', 'michael.brown@example.com', 'Teacher', 'Married', 'Father', 'C005'),
('I006', 'David', 'Williams', 8901234567, '505 Pine St', 'Male', '1992-03-10', 'david.williams@example.com', 'Artist', 'Single', 'Brother', 'C006'),
('I007', 'Sarah', 'Miller', 9012345678, '606 Redwood St', 'Female', '1980-06-15', 'sarah.miller@example.com', 'Doctor', 'Married', 'Wife', 'C007'),
('I008', 'Robert', 'Wilson', 1234567890, '707 Ash St', 'Male', '1990-04-25', 'robert.wilson@example.com', 'Software Developer', 'Single', 'Friend', 'C008'),
('I009', 'Sophia', 'Moore', 2345678901, '808 Maple St', 'Female', '1995-11-30', 'sophia.moore@example.com', 'Writer', 'Single', 'Daughter', 'C009'),
('I010', 'James', 'Taylor', 3456789012, '909 Cedar St', 'Male', '1980-02-18', 'james.taylor@example.com', 'Chef', 'Married', 'Spouse', 'C010');

INSERT INTO Assessments (AssessmentID, AssessmentDate, Result, SeverityLevel, ReviewDate, AssessmentNotes, ClaimID, AssessorID)
VALUES
('AS001', '2021-01-25', 'Passed', 'Minor', '2021-01-28', 'Initial assessment done', 'CL001', 'A001'),
('AS002', '2021-02-10', 'Approved', 'Major', '2021-02-12', 'Further examination required', 'CL002', 'A002'),
('AS003', '2021-03-05', 'Rejected', 'Critical', '2021-03-08', 'Final review conducted', 'CL003', 'A003'),
('AS004', '2021-04-01', 'Approved', 'Minor', '2021-04-05', 'Initial review complete', 'CL004', 'A004'),
('AS005', '2021-05-15', 'Approved', 'Moderate', '2021-05-18', 'Comprehensive assessment performed', 'CL005', 'A005'),
('AS006', '2021-06-10', 'Passed', 'Minor', '2021-06-12', 'Review pending further evaluation', 'CL006', 'A001'),
('AS007', '2021-07-20', 'Rejected', 'Severe', '2021-07-23', 'Inspection done and reviewed', 'CL007', 'A002'),
('AS008', '2021-08-05', 'Approved', 'Moderate', '2021-08-08', 'Detailed assessment completed', 'CL008', 'A003'),
('AS009', '2021-09-01', 'Approved', 'Low', '2021-09-04', 'Assessment concluded', 'CL009', 'A004'),
('AS010', '2021-10-10', 'Passed', 'High', '2021-10-13', 'Assessment review completed', 'CL010', 'A005');

INSERT INTO Payouts (PayoutID, Amount, PayoutDate, PayoutStatus, ClaimID)
VALUES
('PO001', 2000, '2021-02-01', 'Completed', 'CL001'),
('PO002', 1500, '2021-03-01', 'Pending', 'CL002'),
('PO003', 1200, '2021-04-01', 'Completed', 'CL003'),
('PO004', 2500, '2021-05-01', 'Completed', 'CL004'),
('PO005', 1800, '2021-06-01', 'Pending', 'CL005'),
('PO006', 2000, '2021-07-01', 'Completed', 'CL006'),
('PO007', 1500, '2021-08-01', 'Completed', 'CL007'),
('PO008', 2200, '2021-09-01', 'Pending', 'CL008'),
('PO009', 1700, '2021-10-01', 'Completed', 'CL009'),
('PO010', 1500, '2021-11-01', 'Completed', 'CL010');


-- ================================================
-- VIEWS: Báo cáo hệ thống (11 view)
-- ================================================

CREATE VIEW ActiveContracts AS
SELECT ContractID, CustomerID, InsuranceTypeID, SignDate, ExpirationDate, EffectiveDate
FROM InsuranceContracts
WHERE CURDATE() BETWEEN EffectiveDate AND ExpirationDate;

CREATE VIEW PendingClaims AS
SELECT ClaimID, ContractID, ClaimDate, EventDate, EventType, ClaimStatus, Amount, Description
FROM InsuranceClaim
WHERE ClaimStatus = 'Pending';

CREATE VIEW PayoutSummary AS
SELECT ic.ContractID, c.CustomerID, SUM(p.Amount) AS TotalPayout
FROM Payouts p
JOIN InsuranceClaim icl ON p.ClaimID = icl.ClaimID
JOIN InsuranceContracts ic ON icl.ContractID = ic.ContractID
JOIN Customers c ON ic.CustomerID = c.CustomerID
GROUP BY ic.ContractID, c.CustomerID;

CREATE VIEW PendingPayments AS
SELECT p.PaymentID, p.ContractID, c.CustomerID, p.PaymentDate, p.Amount, p.PaymentStatus
FROM Payments p
JOIN InsuranceContracts ic ON p.ContractID = ic.ContractID
JOIN Customers c ON ic.CustomerID = c.CustomerID
WHERE p.PaymentStatus = 'Pending';

CREATE VIEW CustomerContractCount AS
SELECT c.CustomerID, c.FirstName, c.LastName, COUNT(ic.ContractID) AS TotalContracts
FROM Customers c
LEFT JOIN InsuranceContracts ic ON c.CustomerID = ic.CustomerID
GROUP BY c.CustomerID;

CREATE VIEW ContractPaymentSummary AS
SELECT ic.ContractID, c.CustomerID, SUM(p.Amount) AS TotalPaid
FROM InsuranceContracts ic
JOIN Payments p ON ic.ContractID = p.ContractID
JOIN Customers c ON ic.CustomerID = c.CustomerID
GROUP BY ic.ContractID, c.CustomerID;

CREATE VIEW ExpiringContracts AS
SELECT ContractID, CustomerID, ExpirationDate
FROM InsuranceContracts
WHERE ExpirationDate BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 30 DAY);

CREATE VIEW ClaimSuccessRateSummary AS
SELECT ClaimStatus, COUNT(*) AS TotalClaims
FROM InsuranceClaim
GROUP BY ClaimStatus;

CREATE VIEW ContractPerformanceSummary AS
SELECT YEAR(SignDate) AS Year, MONTH(SignDate) AS Month, COUNT(*) AS TotalContracts
FROM InsuranceContracts
GROUP BY YEAR(SignDate), MONTH(SignDate);

CREATE VIEW ProductSalesSummary AS
SELECT ic.InsuranceTypeID, it.InsuranceName, COUNT(*) AS TotalContracts
FROM InsuranceContracts ic
LEFT JOIN InsuranceTypes it ON ic.InsuranceTypeID = it.InsuranceTypeID
GROUP BY ic.InsuranceTypeID, it.InsuranceName;

CREATE VIEW InsuranceTypePerformanceSummary AS
SELECT ic.InsuranceTypeID, it.InsuranceName, COUNT(icl.ClaimID) AS TotalClaims
FROM InsuranceContracts ic
JOIN InsuranceTypes it ON ic.InsuranceTypeID = it.InsuranceTypeID
LEFT JOIN InsuranceClaim icl ON ic.ContractID = icl.ContractID
GROUP BY ic.InsuranceTypeID, it.InsuranceName;

-- ================================================
-- PHÂN QUYỀN: Roles, Users, Permissions, Mapping
-- ================================================

CREATE TABLE Roles (
  RoleID INT AUTO_INCREMENT PRIMARY KEY,
  RoleName VARCHAR(100) NOT NULL UNIQUE,
  Description VARCHAR(255)
);

CREATE TABLE Users (
  UserID VARCHAR(255) PRIMARY KEY,
  Username VARCHAR(255) NOT NULL UNIQUE,
  PasswordHash VARCHAR(255) NOT NULL,
  FullName VARCHAR(255),
  Email VARCHAR(255) NOT NULL UNIQUE,
  PhoneNumber VARCHAR(255),
  RoleID INT NOT NULL,
  Status ENUM('active', 'inactive') DEFAULT 'active',
  CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);

CREATE TABLE Permissions (
  PermissionID INT AUTO_INCREMENT PRIMARY KEY,
  ActionCode VARCHAR(100) UNIQUE,
  Description VARCHAR(255)
);

CREATE TABLE RolePermissions (
  RoleID INT NOT NULL,
  PermissionID INT NOT NULL,
  PRIMARY KEY (RoleID, PermissionID),
  FOREIGN KEY (RoleID) REFERENCES Roles(RoleID),
  FOREIGN KEY (PermissionID) REFERENCES Permissions(PermissionID)
);

CREATE TABLE AuditLog (
  LogID INT AUTO_INCREMENT PRIMARY KEY,
  UserID VARCHAR(255) NOT NULL,
  Action VARCHAR(100) NOT NULL,
  Details TEXT,
  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (UserID) REFERENCES Users(UserID)
);


-- THÊM 11 VAI TRÒ
INSERT INTO Roles (RoleName, Description) VALUES
('insurance_agent', 'Insurance Agents'),
('claim_assessor', 'Claim Assessors'),
('finance_staff', 'Finance Department'),
('manager_ceo', 'Managers and Executives'),
('customer_support', 'Customer Support'),
('underwriting', 'Underwriting Department'),
('sales_marketing', 'Sales and Marketing'),
('product_development', 'Product Development'),
('compliance_audit', 'Compliance and Audit'),
('business_analyst', 'Business Analyst and Reporting'),
('it_admin', 'IT / Database Admins');

-- THÊM PERMISSIONS TƯƠNG ỨNG VỚI VIEW
INSERT INTO Permissions (ActionCode, Description) VALUES
('VIEW_ActiveContracts', 'Xem hợp đồng đang hoạt động'),
('VIEW_PendingClaims', 'Xem yêu cầu bồi thường đang chờ xử lý'),
('VIEW_PayoutSummary', 'Xem tổng hợp chi trả theo hợp đồng'),
('VIEW_PendingPayments', 'Xem thanh toán đang chờ'),
('VIEW_CustomerContractCount', 'Xem số hợp đồng theo khách hàng'),
('VIEW_ContractPaymentSummary', 'Xem tổng thanh toán theo hợp đồng'),
('VIEW_ExpiringContracts', 'Xem hợp đồng sắp hết hạn'),
('VIEW_ClaimSuccessRateSummary', 'Xem tỷ lệ xử lý yêu cầu bồi thường'),
('VIEW_ContractPerformanceSummary', 'Xem hiệu suất hợp đồng theo tháng'),
('VIEW_ProductSalesSummary', 'Xem số hợp đồng theo loại bảo hiểm'),
('VIEW_InsuranceTypePerformanceSummary', 'Hiệu suất loại bảo hiểm');

-- GÁN QUYỀN CHO MỖI ROLE
-- Mỗi vai trò từ 1 đến 11 (RoleID tương ứng với thứ tự trong bảng Roles)

-- Insurance Agents
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 1, PermissionID FROM Permissions
WHERE ActionCode IN ('VIEW_ActiveContracts', 'VIEW_PendingPayments', 'VIEW_CustomerContractCount');

-- Claim Assessors
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 2, PermissionID FROM Permissions
WHERE ActionCode IN ('VIEW_PendingClaims', 'VIEW_PayoutSummary');

-- Finance Staff
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 3, PermissionID FROM Permissions
WHERE ActionCode IN ('VIEW_ContractPaymentSummary', 'VIEW_PayoutSummary');

-- Managers / CEO
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 4, PermissionID FROM Permissions
WHERE ActionCode IN ('VIEW_ContractPerformanceSummary', 'VIEW_ExpiringContracts', 'VIEW_ClaimSuccessRateSummary', 'VIEW_PayoutSummary');

-- Customer Support
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 5, PermissionID FROM Permissions
WHERE ActionCode IN ('VIEW_ActiveContracts', 'VIEW_PendingPayments', 'VIEW_CustomerContractCount');

-- Underwriting
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 6, PermissionID FROM Permissions
WHERE ActionCode IN ('VIEW_CustomerContractCount', 'VIEW_ClaimSuccessRateSummary');

-- Sales & Marketing
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 7, PermissionID FROM Permissions
WHERE ActionCode IN ('VIEW_ContractPerformanceSummary', 'VIEW_CustomerContractCount', 'VIEW_ProductSalesSummary');

-- Product Development
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 8, PermissionID FROM Permissions
WHERE ActionCode IN ('VIEW_PayoutSummary', 'VIEW_ClaimSuccessRateSummary', 'VIEW_InsuranceTypePerformanceSummary');

-- Compliance & Audit
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 9, PermissionID FROM Permissions
WHERE ActionCode IN ('VIEW_PendingClaims', 'VIEW_ClaimSuccessRateSummary', 'VIEW_ContractPaymentSummary');

-- Business Analyst / Reporting
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 10, PermissionID FROM Permissions
WHERE ActionCode IN (
  'VIEW_ContractPerformanceSummary', 'VIEW_PayoutSummary',
  'VIEW_ClaimSuccessRateSummary', 'VIEW_ProductSalesSummary',
  'VIEW_InsuranceTypePerformanceSummary');

-- IT / Admins: full quyền
INSERT INTO RolePermissions (RoleID, PermissionID)
SELECT 11, PermissionID FROM Permissions;

-- USERS MẪU CHO MỖI ROLE
INSERT INTO Users (UserID, Username, PasswordHash, FullName, Email, PhoneNumber, RoleID)
VALUES 
('U001', 'agent01', SHA2('agent123', 256), 'Alice Agent', 'alice.agent@example.com', '0123456789', 1),
('U002', 'assessor01', SHA2('assess123', 256), 'Bob Assessor', 'bob.assessor@example.com', '0123456790', 2),
('U003', 'finance01', SHA2('finance123', 256), 'Carol Finance', 'carol.finance@example.com', '0123456791', 3),
('U004', 'ceo01', SHA2('ceo123', 256), 'David CEO', 'david.ceo@example.com', '0123456792', 4),
('U005', 'support01', SHA2('support123', 256), 'Eva Support', 'eva.support@example.com', '0123456793', 5),
('U006', 'underwrite01', SHA2('under123', 256), 'Frank UW', 'frank.uw@example.com', '0123456794', 6),
('U007', 'sales01', SHA2('sales123', 256), 'Grace Sales', 'grace.sales@example.com', '0123456795', 7),
('U008', 'product01', SHA2('product123', 256), 'Henry Product', 'henry.product@example.com', '0123456796', 8),
('U009', 'audit01', SHA2('audit123', 256), 'Ivy Audit', 'ivy.audit@example.com', '0123456797', 9),
('U010', 'analyst01', SHA2('analyst123', 256), 'Jack Analyst', 'jack.analyst@example.com', '0123456798', 10),
('U011', 'admin01', SHA2('admin123', 256), 'Kate IT Admin', 'kate.it@example.com', '0123456799', 11);




