import logging
lines = [
    "INFO: Connection successful",
    "ERROR: Timeout",
    "INFO: Retry",
    "WARNING: High load",
    "ERROR: Disk failure"
]
x = []
processed = 0
failed = 0
print(lines)
for line in lines:
    try:
        processed += 1
        if "ERROR" in line:
            logging.error(line)
            x.append(line)
        elif "WARNING" in line:
            logging.warning(line)
            x.append(line)
        else:
            logging.info(line)
    except Exception as e:
        failed += 1
        logging.critical (f"Unexpected failure: {e}")
print("x Log:")
for a in x:
    print(a)
print("\nSummary:")
print("processed :",processed)
print("failed :",failed)
logging.basicConfig(
    filename="audit_log.txt",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

