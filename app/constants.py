"""Application-wide constants for consistency and maintainability."""

# API routing
API_V1_PREFIX = "/api/v1"

# I/O buffer sizes (tuned for performance)
UPLOAD_CHUNK_SIZE = 8192  # Chunk size for reading multipart uploads
FILE_READ_BUFFER_SIZE = 65536  # 64KB - optimal for most systems
HASH_CHUNK_SIZE = 4096  # For file hashing

# File validation
MAX_FILENAME_LENGTH = 255
DANGEROUS_FILENAME_CHARS = '<>:"|?*\x00'
