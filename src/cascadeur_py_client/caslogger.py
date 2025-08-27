"""
Cascadeur Python Client Logging Module

This module provides centralized logging configuration for the Cascadeur Python client.
It supports dual output to both console and file, with configurable output directory.

Environment Variables:
    CASCADEUR_PYTHON_OUTPUT_DIR: Directory for log files. If not set, uses system temp directory.
    CASCADEUR_PYTHON_LOG_LEVEL: Default log level (debug, info, warning, error, critical). 
                                Case insensitive. Defaults to 'info' if not set.

Usage:
    from cascadeur_py_client.caslogger import logger
    logger.info("Message")
"""

import os
import sys
import logging
import tempfile
from pathlib import Path
from datetime import datetime
from typing import Optional, Union, Any
from logging.handlers import RotatingFileHandler


def _get_log_directory() -> Path:
    """
    Determine the directory for log files.
    
    Checks CASCADEUR_PYTHON_OUTPUT_DIR environment variable first,
    falls back to system temp directory if not set.
    
    Returns:
        Path object pointing to the log directory
    """
    env_dir = os.environ.get('CASCADEUR_PYTHON_OUTPUT_DIR')
    
    if env_dir:
        log_dir = Path(env_dir)
        # Create directory if it doesn't exist
        try:
            log_dir.mkdir(parents=True, exist_ok=True)
            return log_dir
        except Exception as e:
            # Fall back to temp dir if we can't create the specified directory
            print(f"Warning: Could not create log directory {env_dir}: {e}", file=sys.stderr)
            print("Falling back to system temp directory", file=sys.stderr)
    
    # Use system temp directory as fallback
    temp_dir = Path(tempfile.gettempdir())
    cascadeur_temp = temp_dir / "cascadeur_logs"
    cascadeur_temp.mkdir(parents=True, exist_ok=True)
    return cascadeur_temp


def _get_log_filename() -> str:
    """
    Generate log filename with current date and time.
    
    Returns:
        Filename in format: log_YYYYMMDD-HHMMSS.txt
    """
    datetime_str = datetime.now().strftime('%Y%m%d-%H%M%S')
    return f"log_{datetime_str}.txt"


def _get_default_log_level() -> int:
    """
    Get the default log level from environment variable CASCADEUR_PYTHON_LOG_LEVEL.
    
    Environment variable values (case insensitive):
        - "debug" or "DEBUG" -> logging.DEBUG
        - "info" or "INFO" -> logging.INFO
        - "warning" or "WARNING" or "warn" -> logging.WARNING
        - "error" or "ERROR" -> logging.ERROR
        - "critical" or "CRITICAL" -> logging.CRITICAL
        
    Returns:
        Log level integer constant from logging module. 
        Defaults to logging.INFO if env var is not set or invalid.
    """
    env_level = os.environ.get('CASCADEUR_PYTHON_LOG_LEVEL', '').strip()
    
    if not env_level:
        return logging.INFO
    
    # Map environment values to logging levels (case insensitive)
    level_map = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'warn': logging.WARNING,  # Common alias
        'error': logging.ERROR,
        'critical': logging.CRITICAL,
        'fatal': logging.CRITICAL,  # Common alias
    }
    
    # Convert to lowercase for case-insensitive comparison
    normalized_level = env_level.lower()
    
    # Return the mapped level or INFO as default
    level = level_map.get(normalized_level, logging.INFO)
    
    # Log if an invalid value was provided
    if normalized_level not in level_map:
        print(f"Warning: Invalid log level '{env_level}' in CASCADEUR_PYTHON_LOG_LEVEL. Using INFO.", file=sys.stderr)
    
    return level


def _setup_logger(
    name: str = "caslogger",
    level: Optional[Union[int, str]] = None,
    console_format: Optional[str] = None,
    file_format: Optional[str] = None,
    max_file_size: int = 10 * 1024 * 1024,  # 10MB default
    backup_count: int = 5
) -> logging.Logger:
    """
    Configure and return a logger with both console and file handlers.
    
    Args:
        name: Logger name
        level: Logging level (default: from CASCADEUR_PYTHON_LOG_LEVEL env var, or INFO)
        console_format: Format string for console output
        file_format: Format string for file output
        max_file_size: Maximum size of log file before rotation (bytes)
        backup_count: Number of backup files to keep
        
    Returns:
        Configured logger instance
    """
    # Use environment variable if level not explicitly provided
    if level is None:
        level = _get_default_log_level()
    elif isinstance(level, str):
        # Convert string level to logging constant
        level = getattr(logging, level.upper(), logging.INFO)
    
    # Create logger
    logger_instance = logging.getLogger(name)
    logger_instance.setLevel(level)
    
    # Prevent duplicate handlers if module is reloaded
    if logger_instance.handlers:
        return logger_instance
    
    # Default formats
    if console_format is None:
        console_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    if file_format is None:
        file_format = '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(funcName)s() - %(message)s'
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_formatter = logging.Formatter(console_format)
    console_handler.setFormatter(console_formatter)
    logger_instance.addHandler(console_handler)
    
    # File handler with rotation
    try:
        log_dir = _get_log_directory()
        log_file = log_dir / _get_log_filename()
        
        # Use RotatingFileHandler for automatic log rotation
        file_handler = RotatingFileHandler(
            filename=str(log_file),
            maxBytes=max_file_size,
            backupCount=backup_count,
            encoding='utf-8'
        )
        file_handler.setLevel(level)
        file_formatter = logging.Formatter(file_format)
        file_handler.setFormatter(file_formatter)
        logger_instance.addHandler(file_handler)
        
        # Log initial setup information
        logger_instance.info(f"Logging initialized. Log file: {log_file}")
        
    except Exception as e:
        # If file logging fails, continue with console only
        logger_instance.warning(f"Could not set up file logging: {e}")
        logger_instance.warning("Continuing with console logging only")
    
    return logger_instance


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance. If name is provided, returns a child logger.
    
    Args:
        name: Optional name for child logger (e.g., "caslogger.server")
        
    Returns:
        Logger instance
    """
    if name:
        return logging.getLogger(f"caslogger.{name}")
    return logging.getLogger("caslogger")


def set_log_level(level: Union[int, str]) -> None:
    """
    Change the logging level for all caslogger handlers.
    
    Args:
        level: New logging level (e.g., logging.DEBUG, "DEBUG")
    """
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)
    
    main_logger = logging.getLogger("caslogger")
    main_logger.setLevel(level)
    
    for handler in main_logger.handlers:
        handler.setLevel(level)


def add_context_to_log(
    record: logging.LogRecord,
    context: dict[str, Any]
) -> None:
    """
    Add contextual information to a log record.
    
    Args:
        record: The log record to modify
        context: Dictionary of context to add
    """
    for key, value in context.items():
        setattr(record, key, value)


class LogContext:
    """
    Context manager for temporarily adding context to all logs.
    
    Usage:
        with LogContext(logger, {"request_id": "123"}):
            logger.info("Processing request")  # Will include request_id in log
    """
    
    def __init__(self, logger_instance: logging.Logger, context: dict[str, Any]):
        """
        Initialize the log context manager.
        
        Args:
            logger_instance: The logger to add context to
            context: Dictionary of context values
        """
        self.logger = logger_instance
        self.context = context
        self.old_factory: Optional[Any] = None
    
    def __enter__(self) -> 'LogContext':
        """Enter the context manager."""
        old_factory = logging.getLogRecordFactory()
        
        def record_factory(*args: Any, **kwargs: Any) -> logging.LogRecord:
            record = old_factory(*args, **kwargs)
            add_context_to_log(record, self.context)
            return record
        
        logging.setLogRecordFactory(record_factory)
        self.old_factory = old_factory
        return self
    
    def __exit__(self, *args: Any) -> None:
        """Exit the context manager and restore the old factory."""
        if self.old_factory:
            logging.setLogRecordFactory(self.old_factory)


# Initialize the main logger instance
logger = _setup_logger()

# Export convenience functions at module level
debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical
exception = logger.exception


# Module initialization log
logger.debug("caslogger module initialized")


if __name__ == "__main__":
    # Test the logger when run directly
    print("Testing Cascadeur Logger...")
    print(f"Log directory: {_get_log_directory()}")
    print(f"Log filename: {_get_log_filename()}")
    print()
    
    # Test different log levels
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("This is an exception with traceback")
    
    # Test child logger
    child = get_logger("test_child")
    child.info("Message from child logger")
    
    # Test context manager
    with LogContext(logger, {"user_id": 42, "session": "abc123"}):
        logger.info("Message with context")
    
    print()
    print("Check the log file for detailed output")
    print(f"Log file location: {_get_log_directory() / _get_log_filename()}")