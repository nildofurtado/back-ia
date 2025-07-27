class TranscriberException(Exception):
    """Base exception for transcriber service"""
    pass

class AudioProcessingError(TranscriberException):
    """Raised when audio processing fails"""
    pass

class TranscriptionError(TranscriberException):
    """Raised when transcription fails"""
    pass

class SummarizationError(TranscriberException):
    """Raised when summarization fails"""
    pass

class VectorStoreError(TranscriberException):
    """Raised when vector store operations fail"""
    pass

class APIError(TranscriberException):
    """Raised when external API calls fail"""
    pass