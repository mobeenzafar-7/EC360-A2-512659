import hashlib
import os


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return salt.hex() + ":" + digest.hex()


def register_user(email: str, password: str) -> dict:
    if len(password) < 12:
        raise ValueError("Password must be at least 12 characters")
    return {
        "email": email,
        "password_hash": hash_password(password),
        "status": "pending_verification",
    }