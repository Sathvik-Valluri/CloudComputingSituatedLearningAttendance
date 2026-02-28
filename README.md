# CloudComputingSituatedLearningAttendance
# Cloud Computing Phase 2: Employee Attendance & Leave Portal

## Project Overview
This project is a lightweight, cloud-based web application designed to track employee attendance (Work From Home vs. Work From Office) and manage leave requests. It was developed to address the challenge of managing hybrid workforce data without incurring the high costs of enterprise-grade infrastructure. 

It uses a monolithic architecture deployed on a single AWS EC2 instance, utilizing a Python/Flask backend and an SQLite database, ensuring it remains highly cost-effective and entirely within the AWS Free Tier.

## Architecture
* **Cloud Provider:** Amazon Web Services (AWS)
* **Compute:** 1x EC2 Instance (`t2.micro` - Ubuntu Server 24.04 LTS)
* **Storage:** 8GB General Purpose EBS (Elastic Block Store)
* **Backend:** Python 3.10+, Flask
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3 (Bootstrap 5 CDN)

## Prerequisites to Execute the Work
To deploy and run this project, you will need:
1. An active AWS Account.
2. A basic understanding of SSH or access to AWS EC2 Instance Connect.
3. Git installed on the deployment server.

## Deployment Steps

### Step 1: Provision the Infrastructure
1. Log into the AWS Management Console and navigate to the **EC2 Dashboard**.
2. Click **Launch Instance**.
3. **Name:** `Attendance-System-Server`
4. **OS Image:** Select **Ubuntu Server**.
5. **Instance Type:** Select **t2.micro**.
6. **Key Pair:** Create or select an existing `.pem` key pair for SSH access.
7. **Network Settings:** Ensure the Security Group allows inbound traffic for:
   * **HTTP (Port 80)** from `0.0.0.0/0`
   * **SSH (Port 22)** from your IP (or `0.0.0.0/0`)
8. Click **Launch Instance**.

### Step 2: Connect to the Server
Once the instance is running, connect to it. You can use SSH from your local terminal:
`ssh -i "AttendanceKey.pem" ubuntu@<54.167.41.41>`
*(Alternatively, use the browser-based EC2 Instance Connect from the AWS Console).*

### Step 3: Install Dependencies
Run the following commands to update the server and install required packages:
```bash
sudo apt update
sudo apt install python3-pip python3-venv git -y
```

### Step 4: Clone the Repository
```bash
git clone https://github.com/Sathvik-Valluri/CloudComputingSituatedLearningAttendance
cd CloudComputingSituatedLearningAttendance
```

### Step 5: Install Python Packages
Install the required Flask libraries using the provided requirements.txt file:

```bash
sudo pip3 install -r requirements.txt --break-system-packages
```

###Step 6: Execute the Application
To ensure the application runs continuously in the background, even after you close the SSH session, use the nohup command:

```bash
sudo nohup python3 app.py &
```

Press Enter to return to the command prompt.
