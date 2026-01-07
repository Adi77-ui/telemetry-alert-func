# Azure Telemetry Alert Processing Pipeline (Serverless)

## Overview

This project demonstrates a **real-world alert ingestion and observability pipeline** built on Azure using a **serverless architecture**.

It simulates how **platform, SRE, and data teams** receive monitoring alerts (CPU, failures, anomalies), process them via an HTTP endpoint, and persist them for **analysis, auditing, and downstream automation**.

The system is **event-driven**, **stateless**, and **cloud-native**.

---

## Architecture

Azure Monitor / Alert Source  
&nbsp;&nbsp;&nbsp;&nbsp;⬇  
HTTP Triggered Azure Function  
&nbsp;&nbsp;&nbsp;&nbsp;⬇  
Application Insights (Logs & Traces)  
&nbsp;&nbsp;&nbsp;&nbsp;⬇  
KQL Queries (Alert Analysis / Validation)

---

## Azure Services Used

- **Azure Functions (Linux Consumption Plan)**
- **Application Insights**
- **Azure Monitor (alert-style payload simulation)**
- **Azure Resource Group (isolated project scope)**

---

## What This Project Proves

- Event-driven alert ingestion design
- Azure Functions HTTP triggers and authentication handling
- Structured telemetry logging
- Querying production-grade logs using KQL
- Debugging real Azure deployment and authorization issues

This is **not** a demo CRUD app.  
It reflects how alerts are handled in **real production systems**.

---

## Function Details

### Function Name
`AlertHttp`

### Trigger
- HTTP Trigger
- Authorization Level: **Anonymous** (webhook / Azure Monitor compatible)

### Example Input Payload

```json
{
  "data": {
    "essentials": {
      "alertRule": "HighCPU-ProdVM",
      "severity": "Sev2",
      "firedDateTime": "2026-01-07T10:00:00Z"
    }
  }
}
