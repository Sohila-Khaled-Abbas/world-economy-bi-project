"""
Docker Environment Diagnostic Script
-----------------------------------
Runs a quick health check on Docker:
- Verifies daemon is running
- Displays current context
- Checks API version compatibility
"""

import subprocess
import json
import os
import sys


def run_command(cmd):
    """Run shell command and return stdout, or None on error."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return None
    except Exception:
        return None


def check_docker_daemon():
    print("🔎 Checking if Docker daemon is running...")
    ping = run_command("docker version --format '{{json .Server.Version}}'")
    if ping:
        print(f"✅ Docker is running. Version: {json.loads(ping)}")
        return True
    else:
        print("❌ Cannot connect to Docker daemon.")
        print("   → Start Docker Desktop or ensure the Docker service is running.")
        return False


def check_docker_context():
    print("\n🔎 Checking Docker context...")
    ctx_output = run_command("docker context ls --format '{{json .}}'")
    if ctx_output:
        print("✅ Docker contexts available.")
        print(ctx_output)
    else:
        print("⚠ Could not list Docker contexts. Try `docker context ls` manually.")


def check_api_version():
    print("\n🔎 Checking Docker API version...")
    api_version = run_command("docker version --format '{{.Client.APIVersion}}'")
    if api_version:
        print(f"✅ Docker API version: {api_version}")
        if float(api_version) < 1.41:
            print("⚠ API version is older than 1.41. Consider upgrading Docker Desktop.")
    else:
        print("⚠ Could not fetch API version.")


def main():
    print("🐳 Docker Diagnostic Tool")
    print("-" * 30)

    if not check_docker_daemon():
        sys.exit(1)

    check_docker_context()
    check_api_version()

    print("\n🚀 You are good to run `docker build`!")


if __name__ == "__main__":
    main()
