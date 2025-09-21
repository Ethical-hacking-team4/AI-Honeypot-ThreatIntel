# T-Pot Installation on AWS Free Tier

This guide explains how to deploy **T-Pot honeypot** on an AWS Free Tier EC2 instance for ethical hacking and threat intelligence purposes.

---

## Prerequisites
- AWS account (Free Tier eligible)
- Basic knowledge of SSH and Linux commands
- Git installed locally (optional, for cloning T-Pot repo)

---

## Step 1: Launch an AWS EC2 Instance
1. Log in to AWS Management Console.
2. Navigate to **EC2 → Launch Instances**.
3. Select **Ubuntu Server 22.04 LTS** (Free Tier eligible).
4. Choose **t2.micro** or **t3.micro** instance type.
5. Configure security group:
   - **SSH (22)** → Your IP only
   - **Custom TCP 64297** → Your IP (Hive dashboard)
   - **Custom TCP 5601** → Your IP (Kibana dashboard)
6. Launch the instance and download the key pair (.pem file).

---

## Step 2: Connect to the Instance via SSH
```bash
ssh -i "your-key.pem" ubuntu@<EC2-Public-IP>
```

---

## Step 3: Update and Upgrade the System
```bash
sudo apt update && sudo apt upgrade -y
```

---

## Step 4: Install Docker and Dependencies
```bash
sudo apt install docker.io docker-compose git -y
sudo systemctl enable docker
sudo systemctl start docker
```

---

## Step 5: Install T-Pot
```bash
git clone https://github.com/telekom-security/tpotce.git
cd tpotce
sudo ./install.sh
```
- Choose **default Docker installation** during prompts (~30–45 mins).
- Wait until all containers are up and running.

---

## Step 6: Access the Dashboards
- **Hive Dashboard:** `http://<EC2-Public-IP>:64297`
- **Kibana Dashboard:** `http://<EC2-Public-IP>:5601`

> Note: Make sure the security group allows your IP access to these ports.

---

## Step 7: Verify Honeypot is Logging
1. SSH into the instance.
2. Check running containers:
```bash
docker ps
```
3. Check honeypot logs:
```bash
docker logs <container-name>
```

---

## Step 8: Next Steps
- Pull logs into your **AI pipeline** for analysis (`ai-pipeline/`).
- Document traffic samples in `honeypots/`.
- Start ethical hacking exercises in a **safe environment**.

---

## References
- [T-Pot GitHub Repository](https://github.com/telekom-security/tpotce)
- [T-Pot Wiki & Documentation](https://github.com/telekom-security/tpotce/wiki)

