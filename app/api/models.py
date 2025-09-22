"""SQLAlchemy ORM models for MasCloner."""

from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, BigInteger, DateTime, ForeignKey
from datetime import datetime
from typing import Optional, List

Base = declarative_base()


class ConfigKV(Base):
    """Key-value configuration storage."""
    
    __tablename__ = "config"
    
    key: Mapped[str] = mapped_column(String(120), primary_key=True)
    value: Mapped[str] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Run(Base):
    """Sync run execution record."""
    
    __tablename__ = "runs"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(20))  # success|error|running|skipped
    num_added: Mapped[int] = mapped_column(Integer, default=0)
    num_updated: Mapped[int] = mapped_column(Integer, default=0)
    bytes_transferred: Mapped[int] = mapped_column(BigInteger, default=0)
    errors: Mapped[int] = mapped_column(Integer, default=0)
    log_path: Mapped[Optional[str]] = mapped_column(Text)
    
    # Relationship
    events: Mapped[List["FileEvent"]] = relationship(
        back_populates="run", 
        cascade="all, delete-orphan"
    )


class FileEvent(Base):
    """Individual file operation event."""
    
    __tablename__ = "file_events"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_id: Mapped[int] = mapped_column(Integer, ForeignKey("runs.id"))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    action: Mapped[str] = mapped_column(String(20))  # added|updated|skipped|error|conflict
    file_path: Mapped[str] = mapped_column(Text)
    file_size: Mapped[int] = mapped_column(BigInteger, default=0)
    file_hash: Mapped[Optional[str]] = mapped_column(String(128))
    message: Mapped[Optional[str]] = mapped_column(Text)
    
    # Relationship
    run: Mapped[Run] = relationship(back_populates="events")


# Create indexes for better query performance
from sqlalchemy import Index

# Index for querying recent runs
Index('idx_runs_started_at', Run.started_at.desc())

# Index for querying events by run
Index('idx_file_events_run_id', FileEvent.run_id)

# Index for querying events by timestamp
Index('idx_file_events_timestamp', FileEvent.timestamp.desc())

# Index for querying events by action
Index('idx_file_events_action', FileEvent.action)
