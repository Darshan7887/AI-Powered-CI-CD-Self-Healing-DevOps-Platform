<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>AI-Powered CI/CD & Self-Healing DevOps Platform</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      background: #0f172a;
      color: #e5e7eb;
      margin: 0;
      padding: 30px;
    }
    .slide {
      max-width: 1100px;
      margin: auto;
      background: #020617;
      border-radius: 12px;
      padding: 30px 40px;
      box-shadow: 0 0 25px rgba(0,0,0,0.4);
    }
    h1 {
      margin-top: 0;
      color: #38bdf8;
      font-size: 32px;
    }
    h2 {
      color: #a5b4fc;
      font-size: 18px;
      margin-bottom: 6px;
    }
    p {
      font-size: 15px;
      line-height: 1.6;
      margin-top: 4px;
    }
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 25px;
      margin-top: 20px;
    }
    .box {
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 15px;
    }
    ul {
      padding-left: 18px;
      margin: 6px 0;
    }
    li {
      font-size: 14px;
      margin-bottom: 6px;
    }
    .flow {
      font-family: monospace;
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 12px;
      margin-top: 8px;
      font-size: 14px;
      color: #93c5fd;
    }
    .footer {
      margin-top: 18px;
      padding-top: 10px;
      border-top: 1px solid #1e293b;
      font-size: 14px;
      color: #c7d2fe;
    }
  </style>
</head>

<body>
  <div class="slide">
    <h1>AI-Powered CI/CD & Self-Healing DevOps Platform</h1>

    <p>
      A <strong>production-style DevOps & SRE platform</strong> that automates CI/CD,
      deploys applications on Kubernetes, detects failures, analyzes root causes using
      AI-assisted logic, and performs <strong>safe self-healing actions</strong>.
    </p>

    <div class="grid">
      <div class="box">
        <h2>What it demonstrates</h2>
        <ul>
          <li>Fail-fast CI/CD using GitHub Actions</li>
          <li>Secure, reproducible Docker builds</li>
          <li>Kubernetes operations (Deployment, Service, ConfigMap, HPA)</li>
          <li>Self-healing via probes, restarts, rollbacks, autoscaling</li>
          <li>AI-driven incident analysis (RCA)</li>
          <li>SRE mindset: reliability, recovery, explainability</li>
        </ul>
      </div>

      <div class="box">
        <h2>High-level flow</h2>
        <div class="flow">
          Code Push<br/>
          → CI/CD Pipeline<br/>
          → Docker Image<br/>
          → Kubernetes Deployment<br/>
          → Failure Detection<br/>
          → AI Root Cause Analysis<br/>
          → Automated Recovery
        </div>
      </div>
    </div>

    <div class="grid">
      <div class="box">
        <h2>Repository structure</h2>
        <div class="flow">
          app/        Flask app + failure simulation<br/>
          docker/     Production Dockerfile<br/>
          .github/    CI/CD pipeline<br/>
          k8s/        Deployment, Service, ConfigMap, HPA<br/>
          ai-engine/  Failure patterns + RCA logic<br/>
          scripts/    Self-healing automation
        </div>
      </div>

      <div class="box">
        <h2>Self-healing behavior</h2>
        <ul>
          <li><strong>Pod crash</strong> → Restart</li>
          <li><strong>Repeated failure</strong> → Rollback</li>
          <li><strong>High CPU</strong> → Scale replicas</li>
          <li><strong>Unknown issue</strong> → Report only</li>
        </ul>
      </div>
    </div>

    <div class="footer">
      <strong>One-line interview summary:</strong><br/>
      An AI-assisted self-healing DevOps platform that automates CI/CD, operates Kubernetes workloads,
      analyzes failures, and performs SRE-style recovery actions.
    </div>
  </div>
</body>
</html>
