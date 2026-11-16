import subprocess
import glob
import time

for f in sorted(glob.glob("./../red-scare/data/*.txt")):
    with open(f) as fh:
        try:
            start = time.perf_counter()

            r = subprocess.run(
                ["python", "Few.py"],
                stdin=fh,
                capture_output=True,
                text=True,
                timeout=10
            )

            elapsed = time.perf_counter() - start

            print(f, r.stdout.strip() or r.stderr.strip(),
                  f"Time: {elapsed:.4f} seconds")

        except subprocess.TimeoutExpired:
            print(f, "TIMEOUT (>10 seconds)")