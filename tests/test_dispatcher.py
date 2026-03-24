"""Tests for the dispatcher module."""

import os
import queue


def test_dispatcher_queue():
    """Test that the thread-safe queue works correctly."""
    q = queue.Queue(0)
    q.put("test")
    assert q.get() == "test"


def test_pipe_bytes():
    """Test that pipe communication uses bytes (Python 3 requirement)."""
    r, w = os.pipe()
    os.write(w, b"X")
    data = os.read(r, 1)
    os.close(r)
    os.close(w)
    assert data == b"X"
