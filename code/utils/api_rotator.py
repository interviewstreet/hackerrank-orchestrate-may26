import os
import threading
from itertools import cycle
from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiRotator:
    """Thread-safe round-robin API key rotator for Gemini clients."""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(GeminiRotator, cls).__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self):
        with self._lock:
            if self._initialized:
                return
            
            # Collect keys from multiple possible environment variables
            keys = os.getenv("GEMINI_API_KEYS", "").split(",")
            # Also check for numbered keys GEMINI_API_KEY_1, _2, etc.
            idx = 1
            while True:
                k = os.getenv(f"GEMINI_API_KEY_{idx}")
                if not k: break
                if k not in keys: keys.append(k)
                idx += 1
            
            # Filter empty and initialize clients
            self.keys = [k.strip() for k in keys if k.strip()]
            self.clients = [genai.Client(api_key=k) for k in self.keys]
            self._index = 0
            self._initialized = True
            
            if not self.keys:
                print("[rotator] WARNING: No Gemini API keys found in .env!")

    def get_client(self) -> genai.Client:
        """Returns the current client (thread-safe)."""
        with self._lock:
            if not self.clients: return None
            return self.clients[self._index]

    def rotate(self):
        """Move to the next key (thread-safe)."""
        with self._lock:
            if self.clients:
                self._index = (self._index + 1) % len(self.clients)

    def key_count(self) -> int:
        return len(self.keys)

    def has_keys(self) -> bool:
        return len(self.keys) > 0


# Singleton instance
rotator = GeminiRotator()