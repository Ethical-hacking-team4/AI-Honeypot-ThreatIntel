# AI Driven Honeypot for Threat Intelligence

## Project Overview
AI Driven Honeypot for Threat Intelligence is an **AI-driven multi-honeypot system** designed to collect and analyze attacker behavior in real-time. The project integrates T-Pot honeypots deployed on **AWS Free Tier** and an AI/ML pipeline that generates automated threat intelligence reports and visualizations.

Honey pots provide a controlled environment to study real attacks. High-interaction honeypots allow us to develop a higher understanding of attack signatures and bad actor goals. Implementing an AI agent to deploy honeypots and interact with bad actors will yield an indepth understanding of attack behaviors regarding phishing, exfiltrations, injection, DDOS, and other attacks.

This project is ideal for **ethical hacking, penetration testing practice, and threat intelligence learning**, providing a safe and controlled environment for analyzing attacks.

---

## Features
- Multi-honeypot deployment: Cowrie, Dionaea, Conpot, etc.
- Optional custom Python honeypot for hands-on experimentation
- AI/ML pipeline for attack clustering and anomaly detection
- LLM-based automated threat intelligence reports
- Kibana dashboards for visualization
- Safe ethical hacking exercises for learning purposes

---

## Repository Structure
```
AI-Honeypot-ThreatIntel/
│
├── setup/                     # Installation and setup instructions
│   ├── tpot-installation.md
│   ├── custom-honeypot.md
│   └── docker-compose.yml
│
├── honeypots/                 # Honeypot logs
│   ├── cowrie-logs/
│   ├── dionaea-samples/
│   └── conpot-logs/
│
├── ai-pipeline/               # AI/ML scripts and dashboards
│   ├── data_ingestion.py
│   ├── preprocessing.py
│   ├── ml_models.py
│   ├── llm_summaries.py
│   └── dashboards.ipynb
│
├── exercises/                 # Safe ethical hacking practice
│   ├── nmap_scans.md
│   ├── ssh_bruteforce.md
│   ├── web_attacks.md
│   └── traffic_analysis.md
│
├── reports/                   # AI-generated or sample reports
│   ├── weekly_report_template.md
│   ├── sample_report_week1.md
│   └── malware_analysis_notes.md
│
├── docs/                      # Documentation, diagrams, glossary
│   ├── architecture-diagram.png
│   ├── workflow.png
│   └── glossary.md
│
├── README.md                  # Project overview and instructions
└── LICENSE                    # MIT License
```

---

## Quick Start
See the `setup/` folder for step-by-step installation and configuration guides for T-Pot and optional custom honeypots.

---

## License
This project is licensed under the **MIT License**.

---

## Authors
- **Loksharan Saravanan**  
  LinkedIn: [linkedin.com/in/loksharan](https://linkedin.com/in/loksharan)  
  GitHub: [github.com/loksharan-soc](https://github.com/loksharan-soc)  
  Portfolio: [loksharan-soc.github.io](https://loksharan-soc.github.io)

- **Honore Mandiamy**  
  Email: hmandia000@citymail.cuny.edu  
  LinkedIn: [linkedin.com/in/honore-m-b18090245](https://linkedin.com/in/honore-m-b18090245)

