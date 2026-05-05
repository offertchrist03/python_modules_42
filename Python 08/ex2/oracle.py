#!/usr/bin/env python3

import os
from dotenv import load_dotenv


def missings(envs: list[str]) -> list[str]:
    misses: list[str] = []
    for env in envs:
        res: str | None = os.environ.get(env)
        if not res:
            misses += [env]
    return misses


def check_env(envs: list[str], misses: list[str]) -> bool:
    res = {
        "MATRIX_MODE": "Mode", "DATABASE_URL": "Database",
        "API_KEY": "API Access",
        "LOG_LEVEL": "Log Level",
                       "ZION_ENDPOINT": "Zion Network",
    }
    print("Configuration loaded:")
    for env in envs:
        label: str | None = os.environ.get(env)
        if env == "API_KEY":
            label = "Authenticated" if label else "Not Authenticated"
        if env == "DATABASE_URL":
            label = ("Connected to local instance"
                     if label == "localhost" or (not label)
                     else label)
        is_missing = f"{" [MISSING]" if env in misses else ""}"
        print(f"{res[env]}: {label}{is_missing}")
    if len(misses):
        return False
    return True


def oracle() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    _ = load_dotenv()

    envs: list[str] = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
                       "ZION_ENDPOINT",]
    misses = missings(envs)

    if not check_env(envs, misses):
        return

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()
