from risk_classifier import classify_risk
from database import save_report

print("Running Risk Classification...")
classify_risk()

print("Saving Report to Database...")
save_report()

print("System Completed")